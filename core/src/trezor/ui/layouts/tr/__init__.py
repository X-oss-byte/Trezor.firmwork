from typing import TYPE_CHECKING, Sequence

from trezor import io, loop, ui, workflow
from trezor.enums import ButtonRequestType
from trezor.utils import DISABLE_ANIMATION
from trezor.wire import ActionCancelled

import trezorui2

from ..common import button_request, interact

if TYPE_CHECKING:
    from typing import Any, NoReturn, Awaitable, Iterable, TypeVar

    from trezor.wire import GenericContext, Context
    from ..common import PropertyType, ExceptionType, ProgressLayout

    T = TypeVar("T")


BR_TYPE_OTHER = ButtonRequestType.Other  # global_import_cache


if __debug__:
    trezorui2.disable_animation(bool(DISABLE_ANIMATION))

    class RustLayoutContent:
        """Providing shortcuts to the data returned by layouts.

        Used only in debug mode.
        """

        # TODO: used only because of `page_count`
        # We could do it some other way
        # TT does this:
        # def page_count(self) -> int:
        #     return self.layout.page_count()

        def __init__(self, raw_content: list[str]) -> None:
            self.raw_content = raw_content
            self.str_content = " ".join(raw_content).replace("  ", " ")

        def page_count(self) -> int:
            """Overall number of pages in this screen. Should always be there."""
            return (
                self.kw_pair_int("scrollbar_page_count")
                or self.kw_pair_int("page_count")
                or 1
            )

        def kw_pair_int(self, key: str) -> int | None:
            """Getting the value of a key-value pair as an integer. None if missing."""
            val = self.kw_pair(key)
            if val is None:
                return None
            return int(val)

        def kw_pair(self, key: str) -> str | None:
            """Getting the value of a key-value pair. None if missing."""
            # Pairs are sent in this format in the list:
            # [..., "key", "::", "value", ...]
            for key_index, item in enumerate(self.raw_content):
                if item == key:
                    if self.raw_content[key_index + 1] == "::":
                        return self.raw_content[key_index + 2]

            return None


class RustLayout(ui.Layout):
    # pylint: disable=super-init-not-called
    def __init__(self, layout: Any):
        self.layout = layout
        self.timer = loop.Timer()
        self.layout.attach_timer_fn(self.set_timer)

    def set_timer(self, token: int, deadline: int) -> None:
        self.timer.schedule(deadline, token)

    def request_complete_repaint(self) -> None:
        msg = self.layout.request_complete_repaint()
        assert msg is None

    def _paint(self) -> None:
        import storage.cache as storage_cache

        painted = self.layout.paint()
        if storage_cache.homescreen_shown is not None and painted:
            storage_cache.homescreen_shown = None

    def _first_paint(self) -> None:
        # Clear the screen of any leftovers.
        ui.backlight_fade(ui.style.BACKLIGHT_DIM)
        ui.display.clear()
        self._paint()

        if __debug__ and self.should_notify_layout_change:
            from apps.debug import notify_layout_change

            # notify about change and do not notify again until next await.
            # (handle_rendering might be called multiple times in a single await,
            # because of the endless loop in __iter__)
            self.should_notify_layout_change = False
            notify_layout_change(self)

        # Turn the brightness on again.
        ui.backlight_fade(self.BACKLIGHT_LEVEL)

    if __debug__:
        from trezor.enums import DebugPhysicalButton

        def create_tasks(self) -> tuple[loop.AwaitableTask, ...]:  # type: ignore [obscured-by-same-name]
            from apps.debug import confirm_signal, input_signal

            return (
                self.handle_input_and_rendering(),
                self.handle_timers(),
                self.handle_swipe(),
                self.handle_button_click(),
                confirm_signal(),
                input_signal(),
            )

        def read_content(self) -> list[str]:
            """Gets the visible content of the screen."""
            self._place_layout()
            raw = self._read_content_raw()
            return " ".join(raw).split("\n")

        def _place_layout(self) -> None:
            """It is necessary to place the layout to get data about its screen content."""
            self.layout.place()

        def _read_content_raw(self) -> list[str]:
            """Reads raw trace content from Rust layout."""
            result: list[str] = []

            def callback(*args: str):
                for arg in args:
                    result.append(str(arg))

            self.layout.trace(callback)
            return result

        def _content_obj(self) -> RustLayoutContent:  # type: ignore [is possibly unbound]
            """Gets object with user-friendly methods on Rust layout content."""
            return RustLayoutContent(self._read_content_raw())

        def _press_left(self) -> Any:
            """Triggers left button press."""
            self.layout.button_event(io.BUTTON_PRESSED, io.BUTTON_LEFT)
            return self.layout.button_event(io.BUTTON_RELEASED, io.BUTTON_LEFT)

        def _press_right(self) -> Any:
            """Triggers right button press."""
            self.layout.button_event(io.BUTTON_PRESSED, io.BUTTON_RIGHT)
            return self.layout.button_event(io.BUTTON_RELEASED, io.BUTTON_RIGHT)

        def _press_middle(self) -> Any:
            """Triggers middle button press."""
            self.layout.button_event(io.BUTTON_PRESSED, io.BUTTON_LEFT)
            self.layout.button_event(io.BUTTON_PRESSED, io.BUTTON_RIGHT)
            self.layout.button_event(io.BUTTON_RELEASED, io.BUTTON_LEFT)
            return self.layout.button_event(io.BUTTON_RELEASED, io.BUTTON_RIGHT)

        def _press_button(self, btn_to_press: DebugPhysicalButton) -> Any:
            from trezor.enums import DebugPhysicalButton
            from apps.debug import notify_layout_change

            if btn_to_press == DebugPhysicalButton.LEFT_BTN:
                msg = self._press_left()
            elif btn_to_press == DebugPhysicalButton.MIDDLE_BTN:
                msg = self._press_middle()
            elif btn_to_press == DebugPhysicalButton.RIGHT_BTN:
                msg = self._press_right()
            else:
                raise Exception(f"Unknown button: {btn_to_press}")

            self.layout.paint()
            if msg is not None:
                raise ui.Result(msg)

            ui.refresh()  # so that a screenshot is taken
            notify_layout_change(self)

        def _swipe(self, direction: int) -> None:
            """Triggers swipe in the given direction.

            Only `UP` and `DOWN` directions are supported.
            """
            from trezor.ui import (
                SWIPE_UP,
                SWIPE_DOWN,
            )
            from trezor.enums import DebugPhysicalButton

            if direction == SWIPE_UP:
                btn_to_press = DebugPhysicalButton.RIGHT_BTN
            elif direction == SWIPE_DOWN:
                btn_to_press = DebugPhysicalButton.LEFT_BTN
            else:
                raise Exception(f"Unsupported direction: {direction}")

            self._press_button(btn_to_press)

        async def handle_swipe(self) -> None:
            """Enables pagination through the current page/flow page.

            Waits for `swipe_signal` and carries it out.
            """
            from apps.debug import swipe_signal

            while True:
                direction = await swipe_signal()
                self._swipe(direction)

        async def handle_button_click(self) -> None:
            """Enables clicking arbitrary of the three buttons.

            Waits for `model_r_btn_signal` and carries it out.
            """
            from apps.debug import model_r_btn_signal

            while True:
                btn = await model_r_btn_signal()
                self._press_button(btn)

        def page_count(self) -> int:
            """How many paginated pages current screen has."""
            self._place_layout()
            return self._content_obj().page_count()

    else:

        def create_tasks(self) -> tuple[loop.Task, ...]:
            return self.handle_timers(), self.handle_input_and_rendering()

    def handle_input_and_rendering(self) -> loop.Task:  # type: ignore [awaitable-is-generator]
        button = loop.wait(io.BUTTON)
        self._first_paint()
        while True:
            if __debug__:
                # Printing debugging info, just temporary
                RustLayoutContent(self._read_content_raw())
            # Using `yield` instead of `await` to avoid allocations.
            event, button_num = yield button
            workflow.idle_timer.touch()
            msg = None
            if event in (io.BUTTON_PRESSED, io.BUTTON_RELEASED):
                msg = self.layout.button_event(event, button_num)
            if msg is not None:
                raise ui.Result(msg)
            self._paint()

    def handle_timers(self) -> loop.Task:  # type: ignore [awaitable-is-generator]
        while True:
            # Using `yield` instead of `await` to avoid allocations.
            token = yield self.timer
            msg = self.layout.timer(token)
            if msg is not None:
                raise ui.Result(msg)
            self._paint()


def draw_simple(layout: Any) -> None:
    # Simple drawing not supported for layouts that set timers.
    def dummy_set_timer(token: int, deadline: int) -> None:
        raise RuntimeError

    layout.attach_timer_fn(dummy_set_timer)
    ui.backlight_fade(ui.style.BACKLIGHT_DIM)
    ui.display.clear()
    layout.paint()
    ui.refresh()
    ui.backlight_fade(ui.style.BACKLIGHT_NORMAL)


# Temporary function, so we know where it is used
# Should be gradually replaced by custom designs/layouts
async def _placeholder_confirm(
    ctx: GenericContext,
    br_type: str,
    title: str,
    data: str | None = None,
    description: str | None = None,
    *,
    verb: str = "CONFIRM",
    verb_cancel: str | None = "",
    hold: bool = False,
    br_code: ButtonRequestType = BR_TYPE_OTHER,
) -> Any:
    return await confirm_action(
        ctx,
        br_type,
        title.upper(),
        data,
        description,
        verb=verb,
        verb_cancel=verb_cancel,
        hold=hold,
        reverse=True,
        br_code=br_code,
    )


async def get_bool(
    ctx: GenericContext,
    br_type: str,
    title: str,
    data: str | None = None,
    description: str | None = None,
    verb: str = "CONFIRM",
    verb_cancel: str | None = "",
    hold: bool = False,
    br_code: ButtonRequestType = BR_TYPE_OTHER,
) -> bool:
    result = await interact(
        ctx,
        RustLayout(
            trezorui2.confirm_action(
                title=title.upper(),
                action=data,
                description=description,
                verb=verb,
                verb_cancel=verb_cancel,
                hold=hold,
            )
        ),
        br_type,
        br_code,
    )

    return result is trezorui2.CONFIRMED


async def raise_if_not_confirmed(a: Awaitable[T], exc: Any = ActionCancelled) -> T:
    result = await a
    if result is not trezorui2.CONFIRMED:
        raise exc
    return result


async def confirm_action(
    ctx: GenericContext,
    br_type: str,
    title: str,
    action: str | None = None,
    description: str | None = None,
    description_param: str | None = None,
    verb: str = "CONFIRM",
    verb_cancel: str | None = "",
    hold: bool = False,
    hold_danger: bool = False,
    reverse: bool = False,
    exc: ExceptionType = ActionCancelled,
    br_code: ButtonRequestType = BR_TYPE_OTHER,
) -> None:
    if verb_cancel is not None:
        verb_cancel = verb_cancel.upper()

    if description is not None and description_param is not None:
        description = description.format(description_param)

    await raise_if_not_confirmed(
        interact(
            ctx,
            RustLayout(
                trezorui2.confirm_action(
                    title=title.upper(),
                    action=action,
                    description=description,
                    verb=verb.upper(),
                    verb_cancel=verb_cancel,
                    hold=hold,
                    reverse=reverse,
                )
            ),
            br_type,
            br_code,
        ),
        exc,
    )


async def confirm_reset_device(
    ctx: GenericContext,
    prompt: str,
    recovery: bool = False,
    show_tutorial: bool = True,
) -> None:
    # Showing the tutorial, as this is the entry point of
    # both the creation of new wallet and recovery of existing seed
    # - the first user interactions with Trezor.
    # (it is also special for model R, so not having to clutter the
    # common code)

    if show_tutorial:
        await tutorial(ctx)

    await raise_if_not_confirmed(
        interact(
            ctx,
            RustLayout(
                trezorui2.confirm_reset_device(
                    recovery=recovery,
                    prompt=prompt.replace("\n", " "),
                )
            ),
            "recover_device" if recovery else "setup_device",
            ButtonRequestType.ProtectCall
            if recovery
            else ButtonRequestType.ResetDevice,
        )
    )


# TODO cleanup @ redesign
async def confirm_backup(ctx: GenericContext) -> bool:
    if await get_bool(
        ctx,
        "backup_device",
        "SUCCESS",
        description="New wallet has been created.\nIt should be backed up now!",
        verb="BACK UP",
        verb_cancel="SKIP",
        br_code=ButtonRequestType.ResetDevice,
    ):
        return True

    return await get_bool(
        ctx,
        "backup_device",
        "WARNING",
        "Are you sure you want to skip the backup?\n",
        "You can back up your Trezor once, at any time.",
        verb="BACK UP",
        verb_cancel="SKIP",
        br_code=ButtonRequestType.ResetDevice,
    )


async def confirm_path_warning(
    ctx: GenericContext,
    path: str,
    path_type: str | None = None,
) -> None:
    if path_type:
        title = f"Unknown {path_type}"
    else:
        title = "Unknown path"
    return await _placeholder_confirm(
        ctx,
        "path_warning",
        title.upper(),
        description=path,
        br_code=ButtonRequestType.UnknownDerivationPath,
    )


async def confirm_homescreen(
    ctx: GenericContext,
    image: bytes,
) -> None:
    # TODO: show homescreen preview?
    await confirm_action(
        ctx,
        "set_homescreen",
        "Set homescreen",
        description="Do you really want to set new homescreen image?",
        br_code=ButtonRequestType.ProtectCall,
    )


def _show_xpub(xpub: str, title: str, cancel: str | None) -> ui.Layout:
    return RustLayout(
        trezorui2.confirm_blob(
            title=title.upper(),
            data=xpub,
            verb_cancel=cancel,
            description=None,
            extra=None,
        )
    )


async def show_xpub(ctx: GenericContext, xpub: str, title: str) -> None:
    await raise_if_not_confirmed(
        interact(
            ctx,
            _show_xpub(xpub, title, None),
            "show_xpub",
            ButtonRequestType.PublicKey,
        )
    )


async def show_address(
    ctx: GenericContext,
    address: str,
    *,
    case_sensitive: bool = True,
    address_qr: str | None = None,
    title: str | None = None,
    network: str | None = None,
    multisig_index: int | None = None,
    xpubs: Sequence[str] = (),
    address_extra: str | None = None,
    title_qr: str | None = None,
    derivation_path: str | None = None,
    account: str | None = None,
) -> None:
    account = account or "Unknown"
    derivation_path = derivation_path or "Unknown"
    title = title or "Receive address"

    await raise_if_not_confirmed(
        interact(
            ctx,
            RustLayout(
                trezorui2.show_receive_address(
                    title=title.upper(),
                    address=address,
                    address_qr=address if address_qr is None else address_qr,
                    account=account,
                    derivation_path=derivation_path,
                    case_sensitive=case_sensitive,
                )
            ),
            "show_address",
            ButtonRequestType.Address,
        )
    )

    # TODO: support showing multisig xpubs?
    # TODO: send button requests in the flow above?


def show_pubkey(
    ctx: Context, pubkey: str, title: str = "Confirm public key"
) -> Awaitable[None]:
    return confirm_blob(
        ctx,
        "show_pubkey",
        title.upper(),
        pubkey,
        br_code=ButtonRequestType.PublicKey,
    )


async def _show_modal(
    ctx: GenericContext,
    br_type: str,
    header: str,
    subheader: str | None,
    content: str,
    button_confirm: str | None,
    button_cancel: str | None,
    br_code: ButtonRequestType,
    exc: ExceptionType = ActionCancelled,
) -> None:
    await confirm_action(
        ctx,
        br_type,
        header.upper(),
        subheader,
        content,
        verb=button_confirm or "",
        verb_cancel=button_cancel,
        exc=exc,
        br_code=br_code,
    )


async def show_error_and_raise(
    ctx: GenericContext,
    br_type: str,
    content: str,
    header: str = "Error",
    subheader: str | None = None,
    button: str = "Close",
    red: bool = False,
    exc: ExceptionType = ActionCancelled,
) -> NoReturn:
    await _show_modal(
        ctx,
        br_type,
        header,
        subheader,
        content,
        button_confirm=None,
        button_cancel=button,
        br_code=BR_TYPE_OTHER,
        exc=exc,
    )
    raise exc


def show_warning(
    ctx: GenericContext,
    br_type: str,
    content: str,
    subheader: str | None = None,
    button: str = "Try again",
    br_code: ButtonRequestType = ButtonRequestType.Warning,
) -> Awaitable[None]:
    return _show_modal(
        ctx,
        br_type,
        "",
        subheader or "WARNING",
        content,
        button_confirm=button,
        button_cancel=None,
        br_code=br_code,
    )


def show_success(
    ctx: GenericContext,
    br_type: str,
    content: str,
    subheader: str | None = None,
    button: str = "Continue",
) -> Awaitable[None]:
    title = "Success"

    # In case only subheader is supplied, showing it
    # in regular font, not bold.
    if not content and subheader:
        content = subheader
        subheader = None

    # Special case for Shamir backup - to show everything just on one page
    # in regular font.
    if "Continue with" in content:
        content = f"{subheader}\n{content}"
        subheader = None
        title = ""

    return _show_modal(
        ctx,
        br_type,
        title,
        subheader,
        content,
        button_confirm=button,
        button_cancel=None,
        br_code=ButtonRequestType.Success,
    )


async def confirm_output(
    ctx: GenericContext,
    address: str,
    amount: str,
    title: str = "Confirm sending",
    index: int | None = None,
    br_code: ButtonRequestType = ButtonRequestType.ConfirmOutput,
) -> None:
    address_title = "RECIPIENT" if index is None else f"RECIPIENT #{index + 1}"
    amount_title = "AMOUNT" if index is None else f"AMOUNT #{index + 1}"
    await raise_if_not_confirmed(
        interact(
            ctx,
            RustLayout(
                trezorui2.confirm_output(
                    address=address,
                    address_title=address_title,
                    amount_title=amount_title,
                    amount=amount,
                )
            ),
            "confirm_output",
            br_code,
        )
    )


async def tutorial(
    ctx: GenericContext,
    br_code: ButtonRequestType = BR_TYPE_OTHER,
) -> None:
    """Showing users how to interact with the device."""
    await interact(
        ctx,
        RustLayout(trezorui2.tutorial()),
        "tutorial",
        br_code,
    )


async def confirm_payment_request(
    ctx: GenericContext,
    recipient_name: str,
    amount: str,
    memos: list[str],
) -> Any:
    memos_str = "\n".join(memos)
    return await _placeholder_confirm(
        ctx,
        "confirm_payment_request",
        "CONFIRM SENDING",
        description=f"{amount} to\n{recipient_name}\n{memos_str}",
        br_code=ButtonRequestType.ConfirmOutput,
    )


async def should_show_more(
    ctx: GenericContext,
    title: str,
    para: Iterable[tuple[int, str]],
    button_text: str = "Show all",
    br_type: str = "should_show_more",
    br_code: ButtonRequestType = BR_TYPE_OTHER,
    confirm: str | bytes | None = None,
) -> bool:
    return await get_bool(
        ctx,
        br_type,
        title.upper(),
        button_text,
        br_code=br_code,
    )


async def confirm_blob(
    ctx: GenericContext,
    br_type: str,
    title: str,
    data: bytes | str,
    description: str | None = None,
    hold: bool = False,
    br_code: ButtonRequestType = BR_TYPE_OTHER,
    ask_pagination: bool = False,
) -> None:
    title = title.upper()
    description = description or ""
    layout = RustLayout(
        trezorui2.confirm_blob(
            title=title,
            description=description,
            data=data,
            extra=None,
            hold=hold,
        )
    )

    await raise_if_not_confirmed(
        interact(
            ctx,
            layout,
            br_type,
            br_code,
        )
    )


async def confirm_address(
    ctx: GenericContext,
    title: str,
    address: str,
    description: str | None = "Address:",
    br_type: str = "confirm_address",
    br_code: ButtonRequestType = BR_TYPE_OTHER,
) -> Awaitable[None]:
    return confirm_blob(
        ctx,
        br_type,
        title.upper(),
        address,
        description,
        br_code=br_code,
    )


async def confirm_text(
    ctx: GenericContext,
    br_type: str,
    title: str,
    data: str,
    description: str | None = None,
    br_code: ButtonRequestType = BR_TYPE_OTHER,
) -> Any:
    return await _placeholder_confirm(
        ctx,
        br_type,
        title,
        data,
        description,
        br_code=br_code,
    )


def confirm_amount(
    ctx: GenericContext,
    title: str,
    amount: str,
    description: str = "Amount:",
    br_type: str = "confirm_amount",
    br_code: ButtonRequestType = BR_TYPE_OTHER,
) -> Awaitable[None]:
    return confirm_blob(
        ctx,
        br_type,
        title.upper(),
        amount,
        description,
        br_code=br_code,
    )


async def confirm_properties(
    ctx: GenericContext,
    br_type: str,
    title: str,
    props: Iterable[PropertyType],
    hold: bool = False,
    br_code: ButtonRequestType = ButtonRequestType.ConfirmOutput,
) -> None:
    from ubinascii import hexlify

    def handle_bytes(prop: PropertyType):
        if isinstance(prop[1], bytes):
            return (prop[0], hexlify(prop[1]).decode(), True)
        else:
            # When there is not space in the text, taking it as data
            # to not include hyphens
            is_data = prop[1] and " " not in prop[1]
            return (prop[0], prop[1], is_data)

    await raise_if_not_confirmed(
        interact(
            ctx,
            RustLayout(
                trezorui2.confirm_properties(
                    title=title.upper(),
                    items=map(handle_bytes, props),  # type: ignore [cannot be assigned to parameter "items"]
                    hold=hold,
                )
            ),
            br_type,
            br_code,
        )
    )


def confirm_value(
    ctx: GenericContext,
    title: str,
    value: str,
    description: str,
    br_type: str,
    br_code: ButtonRequestType = BR_TYPE_OTHER,
    *,
    verb: str | None = None,
    hold: bool = False,
) -> Awaitable[None]:
    """General confirmation dialog, used by many other confirm_* functions."""

    if not verb and not hold:
        raise ValueError("Either verb or hold=True must be set")

    return raise_if_not_confirmed(
        interact(
            ctx,
            RustLayout(
                trezorui2.confirm_value(
                    title=title.upper(),
                    description=description,
                    value=value,
                    verb=verb or "HOLD TO CONFIRM",
                    hold=hold,
                )
            ),
            br_type,
            br_code,
        )
    )


async def confirm_total(
    ctx: GenericContext,
    total_amount: str,
    fee_amount: str,
    fee_rate_amount: str | None = None,
    total_label: str = "Total amount",
    fee_label: str = "Including fee",
    br_type: str = "confirm_total",
    br_code: ButtonRequestType = ButtonRequestType.SignTx,
) -> None:
    await raise_if_not_confirmed(
        interact(
            ctx,
            RustLayout(
                trezorui2.confirm_total(
                    total_amount=total_amount,
                    fee_amount=fee_amount,
                    fee_rate_amount=fee_rate_amount,
                    total_label=total_label.upper(),
                    fee_label=fee_label.upper(),
                )
            ),
            br_type,
            br_code,
        )
    )


async def confirm_joint_total(
    ctx: GenericContext, spending_amount: str, total_amount: str
) -> None:

    await raise_if_not_confirmed(
        interact(
            ctx,
            RustLayout(
                trezorui2.confirm_joint_total(
                    spending_amount=spending_amount,
                    total_amount=total_amount,
                )
            ),
            "confirm_joint_total",
            ButtonRequestType.SignTx,
        )
    )


async def confirm_metadata(
    ctx: GenericContext,
    br_type: str,
    title: str,
    content: str,
    param: str | None = None,
    br_code: ButtonRequestType = ButtonRequestType.SignTx,
    hold: bool = False,
) -> None:
    await _placeholder_confirm(
        ctx,
        br_type,
        title.upper(),
        description=content.format(param),
        hold=hold,
        br_code=br_code,
    )


async def confirm_replacement(ctx: GenericContext, description: str, txid: str) -> None:
    await confirm_value(
        ctx,
        description.upper(),
        txid,
        "Confirm transaction ID:",
        "confirm_replacement",
        ButtonRequestType.SignTx,
        verb="CONFIRM",
    )


async def confirm_modify_output(
    ctx: GenericContext,
    address: str,
    sign: int,
    amount_change: str,
    amount_new: str,
) -> None:
    await raise_if_not_confirmed(
        interact(
            ctx,
            RustLayout(
                trezorui2.confirm_modify_output(
                    address=address,
                    sign=sign,
                    amount_change=amount_change,
                    amount_new=amount_new,
                )
            ),
            "modify_output",
            ButtonRequestType.ConfirmOutput,
        )
    )


async def confirm_modify_fee(
    ctx: GenericContext,
    sign: int,
    user_fee_change: str,
    total_fee_new: str,
    fee_rate_amount: str | None = None,
) -> None:
    await raise_if_not_confirmed(
        interact(
            ctx,
            RustLayout(
                trezorui2.confirm_modify_fee(
                    sign=sign,
                    user_fee_change=user_fee_change,
                    total_fee_new=total_fee_new,
                    fee_rate_amount=fee_rate_amount,
                )
            ),
            "modify_fee",
            ButtonRequestType.SignTx,
        )
    )


async def confirm_coinjoin(
    ctx: GenericContext, max_rounds: int, max_fee_per_vbyte: str
) -> None:
    await raise_if_not_confirmed(
        interact(
            ctx,
            RustLayout(
                trezorui2.confirm_coinjoin(
                    max_rounds=str(max_rounds),
                    max_feerate=max_fee_per_vbyte,
                )
            ),
            "coinjoin_final",
            BR_TYPE_OTHER,
        )
    )


# TODO cleanup @ redesign
async def confirm_sign_identity(
    ctx: GenericContext, proto: str, identity: str, challenge_visual: str | None
) -> None:
    text = ""
    if challenge_visual:
        text += f"{challenge_visual}\n\n"
    text += identity

    await _placeholder_confirm(
        ctx,
        "confirm_sign_identity",
        f"Sign {proto}".upper(),
        text,
        br_code=BR_TYPE_OTHER,
    )


async def confirm_signverify(
    ctx: GenericContext, coin: str, message: str, address: str, verify: bool
) -> None:
    if verify:
        header = f"Verify {coin} message"
        br_type = "verify_message"
    else:
        header = f"Sign {coin} message"
        br_type = "sign_message"

    await confirm_blob(
        ctx,
        br_type,
        header.upper(),
        address,
        "Confirm address:",
        br_code=BR_TYPE_OTHER,
    )

    await confirm_value(
        ctx,
        header.upper(),
        message,
        "Confirm message:",
        br_type,
        BR_TYPE_OTHER,
        verb="CONFIRM",
    )


async def show_popup(
    title: str,
    description: str,
    subtitle: str | None = None,
    description_param: str = "",
    timeout_ms: int = 3000,
) -> None:
    description = description.format(description_param)
    if subtitle:
        description = f"{subtitle}\n{description}"
    await RustLayout(
        trezorui2.show_info(
            title=title,
            description=description,
            time_ms=timeout_ms,
        )
    )


def request_passphrase_on_host() -> None:
    draw_simple(
        trezorui2.show_info(
            title="HIDDEN WALLET",
            description="Please type your passphrase on the connected host.",
        )
    )


async def request_passphrase_on_device(ctx: GenericContext, max_len: int) -> str:
    await button_request(
        ctx, "passphrase_device", code=ButtonRequestType.PassphraseEntry
    )

    result = await ctx.wait(
        RustLayout(
            trezorui2.request_passphrase(
                prompt="ENTER PASSPHRASE",
                max_len=max_len,
            )
        )
    )
    if result is trezorui2.CANCELLED:
        raise ActionCancelled("Passphrase entry cancelled")

    assert isinstance(result, str)
    return result


async def request_pin_on_device(
    ctx: GenericContext,
    prompt: str,
    attempts_remaining: int | None,
    allow_cancel: bool,
    wrong_pin: bool = False,
) -> str:
    from trezor import wire

    # Not showing the prompt in case user did not enter it badly yet
    # (has full 16 attempts left)
    if attempts_remaining is None or attempts_remaining == 16:
        subprompt = ""
    elif attempts_remaining == 1:
        subprompt = "Last attempt"
    else:
        subprompt = f"{attempts_remaining} tries left"

    await button_request(ctx, "pin_device", code=ButtonRequestType.PinEntry)

    dialog = RustLayout(
        trezorui2.request_pin(
            prompt=prompt,
            subprompt=subprompt,
            allow_cancel=allow_cancel,
            wrong_pin=wrong_pin,
        )
    )

    result = await ctx.wait(dialog)
    if result is trezorui2.CANCELLED:
        raise wire.PinCancelled
    assert isinstance(result, str)
    return result


async def confirm_reenter_pin(
    ctx: GenericContext,
    br_type: str = "set_pin",
    br_code: ButtonRequestType = BR_TYPE_OTHER,
) -> None:
    return await confirm_action(
        ctx,
        br_type,
        "CHECK PIN",
        description="Please re-enter PIN to confirm.",
        verb="BEGIN",
        br_code=br_code,
    )


async def pin_mismatch(
    ctx: GenericContext,
    br_type: str = "set_pin",
    br_code: ButtonRequestType = BR_TYPE_OTHER,
) -> None:
    return await confirm_action(
        ctx,
        br_type,
        "PIN MISMATCH",
        description="The PINs you entered do not match.\nPlease try again.",
        verb="TRY AGAIN",
        verb_cancel=None,
        br_code=br_code,
    )


async def confirm_pin_action(
    ctx: GenericContext,
    br_type: str,
    title: str,
    action: str | None,
    description: str | None = "Do you really want to",
    br_code: ButtonRequestType = BR_TYPE_OTHER,
) -> None:
    return await confirm_action(
        ctx,
        br_type,
        title,
        description=f"{description} {action}",
        br_code=br_code,
    )


async def confirm_set_new_pin(
    ctx: GenericContext,
    br_type: str,
    title: str,
    action: str,
    information: list[str],
    description: str = "Do you want to",
    br_code: ButtonRequestType = BR_TYPE_OTHER,
) -> None:
    await confirm_action(
        ctx,
        br_type,
        title,
        description=f"{description} {action}",
        verb="ENABLE",
        br_code=br_code,
    )

    # Additional information for the user to know about PIN/WIPE CODE

    if "wipe_code" in br_type:
        title = "WIPE CODE INFO"
        verb = "HODL TO BEGIN"  # Easter egg from @Hannsek
    else:
        title = "PIN INFORMATION"
        information.append(
            "Position of individual numbers will change between entries for enhanced security."
        )
        verb = "HOLD TO BEGIN"

    return await confirm_action(
        ctx,
        br_type,
        title,
        description="\n".join(information),
        verb=verb,
        hold=True,
        br_code=br_code,
    )


class RustProgress:
    def __init__(
        self,
        title: str,
        description: str | None = None,
        indeterminate: bool = False,
    ):
        self.layout: Any = trezorui2.show_progress(
            title=title.upper(),
            indeterminate=indeterminate,
            description=description or "",
        )
        ui.backlight_fade(ui.style.BACKLIGHT_DIM)
        ui.display.clear()
        self.layout.attach_timer_fn(self.set_timer)
        self.layout.paint()
        ui.backlight_fade(ui.style.BACKLIGHT_NORMAL)

    def set_timer(self, token: int, deadline: int) -> None:
        raise RuntimeError  # progress layouts should not set timers

    def report(self, value: int, description: str | None = None):
        msg = self.layout.progress_event(value, description or "")
        assert msg is None
        self.layout.paint()
        ui.refresh()


def progress(message: str = "PLEASE WAIT") -> ProgressLayout:
    return RustProgress(message.upper())


def bitcoin_progress(message: str) -> ProgressLayout:
    return RustProgress(message.upper())


def pin_progress(message: str, description: str) -> ProgressLayout:
    return RustProgress(message.upper(), description=description)


def monero_keyimage_sync_progress() -> ProgressLayout:
    return RustProgress("SYNCING")


def monero_live_refresh_progress() -> ProgressLayout:
    return RustProgress("REFRESHING", description="", indeterminate=True)


def monero_transaction_progress_inner() -> ProgressLayout:
    return RustProgress("SIGNING TRANSACTION", description="")
