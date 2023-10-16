# This file is part of the Trezor project.
#
# Copyright (C) 2012-2022 SatoshiLabs and contributors
#
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License version 3
# as published by the Free Software Foundation.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the License along with this library.
# If not, see <https://www.gnu.org/licenses/lgpl-3.0.html>.

from dataclasses import dataclass
from typing import Collection, Optional, Tuple

from . import mapping

UsbId = Tuple[int, int]

VENDORS = ("bitcointrezor.com", "trezor.io")


@dataclass(eq=True, frozen=True)
class TrezorModel:
    name: str
    internal_name: str
    minimum_version: Tuple[int, int, int]
    vendors: Collection[str]
    usb_ids: Collection[UsbId]
    default_mapping: mapping.ProtobufMapping
    chunk_size: int


TREZOR_ONE = TrezorModel(
    name="1",
    internal_name="T1B1",
    minimum_version=(1, 8, 0),
    vendors=VENDORS,
    usb_ids=((0x534C, 0x0001),),
    default_mapping=mapping.DEFAULT_MAPPING,
    chunk_size=64 * 1024,
)

TREZOR_T = TrezorModel(
    name="T",
    internal_name="T2T1",
    minimum_version=(2, 1, 0),
    vendors=VENDORS,
    usb_ids=((0x1209, 0x53C1), (0x1209, 0x53C0)),
    default_mapping=mapping.DEFAULT_MAPPING,
    chunk_size=128 * 1024,
)

TREZOR_R = TrezorModel(
    name="Safe 3",
    internal_name="T2B1",
    minimum_version=(2, 1, 0),
    vendors=VENDORS,
    usb_ids=((0x1209, 0x53C1), (0x1209, 0x53C0)),
    default_mapping=mapping.DEFAULT_MAPPING,
    chunk_size=128 * 1024,
)

TREZOR_DISC1 = TrezorModel(
    name="DISC1",
    internal_name="D001",
    minimum_version=(2, 1, 0),
    vendors=VENDORS,
    usb_ids=((0x1209, 0x53C1), (0x1209, 0x53C0)),
    default_mapping=mapping.DEFAULT_MAPPING,
    chunk_size=128 * 1024,
)

TREZORS = {TREZOR_ONE, TREZOR_T, TREZOR_R, TREZOR_DISC1}


def by_name(name: Optional[str]) -> Optional[TrezorModel]:
    if name is None:
        return TREZOR_ONE
    for model in TREZORS:
        if model.name == name:
            return model
    return None


def by_internal_name(name: Optional[str]) -> Optional[TrezorModel]:
    if name is None:
        return None
    for model in TREZORS:
        if model.internal_name == name:
            return model
    return None
