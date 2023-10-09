from typing import *


# rust/src/ui/translations/export.rs
def language_name() -> str:
    """Get the name of the current language."""


# rust/src/ui/translations/export.rs
class TR:
    """Translation object with attributes."""
    addr_mismatch__contact_support: str
    addr_mismatch__key_mismatch: str
    addr_mismatch__mismatch: str
    addr_mismatch__support_url: str
    addr_mismatch__title: str
    addr_mismatch__title_key_mismatch: str
    addr_mismatch__wrong_derication_path: str
    addr_mismatch__xpub_mismatch: str
    address__address: str
    address__public_key: str
    address__title_cosigner: str
    address__title_receive_address: str
    address__title_yours: str
    address_details__account: str
    address_details__derivation_path: str
    address_details__title_receive_address: str
    address_details__title_receiving_to: str
    authenticate__confirm_template: str
    authenticate__header: str
    auto_lock__change_template: str
    auto_lock__title: str
    backup__can_back_up_anytime: str
    backup__it_should_be_backed_up: str
    backup__it_should_be_backed_up_now: str
    backup__new_wallet_created: str
    backup__new_wallet_successfully_created: str
    backup__recover_anytime: str
    backup__title_backup_wallet: str
    backup__title_skip: str
    backup__want_to_skip: str
    binance__buy: str
    binance__confirm_cancel: str
    binance__confirm_input: str
    binance__confirm_order: str
    binance__confirm_output: str
    binance__order_id: str
    binance__pair: str
    binance__price: str
    binance__quantity: str
    binance__sell: str
    binance__sender_address: str
    binance__side: str
    binance__unknown: str
    bitcoin__commitment_data: str
    bitcoin__confirm_locktime: str
    bitcoin__create_proof_of_ownership: str
    bitcoin__high_mining_fee_template: str
    bitcoin__locktime_no_effect: str
    bitcoin__locktime_set_to: str
    bitcoin__locktime_set_to_blockheight: str
    bitcoin__lot_of_change_outputs: str
    bitcoin__multiple_accounts: str
    bitcoin__new_fee_rate: str
    bitcoin__simple_send_of: str
    bitcoin__ticket_amount: str
    bitcoin__title_confirm_details: str
    bitcoin__title_finalize_transaction: str
    bitcoin__title_high_mining_fee: str
    bitcoin__title_meld_transaction: str
    bitcoin__title_modify_amount: str
    bitcoin__title_payjoin: str
    bitcoin__title_proof_of_ownership: str
    bitcoin__title_purchase_ticket: str
    bitcoin__title_update_transaction: str
    bitcoin__unknown_path: str
    bitcoin__unknown_transaction: str
    bitcoin__unusually_high_fee: str
    bitcoin__unverified_external_inputs: str
    bitcoin__valid_signature: str
    bitcoin__voting_rights: str
    buttons__abort: str
    buttons__access: str
    buttons__again: str
    buttons__allow: str
    buttons__back_up: str
    buttons__cancel: str
    buttons__change: str
    buttons__check: str
    buttons__check_again: str
    buttons__close: str
    buttons__confirm: str
    buttons__continue: str
    buttons__details: str
    buttons__enable: str
    buttons__enter: str
    buttons__enter_share: str
    buttons__export: str
    buttons__format: str
    buttons__go_back: str
    buttons__hold_to_confirm: str
    buttons__info: str
    buttons__more_info: str
    buttons__ok_i_understand: str
    buttons__purchase: str
    buttons__quit: str
    buttons__restart: str
    buttons__retry: str
    buttons__select: str
    buttons__set: str
    buttons__show_all: str
    buttons__show_words: str
    buttons__skip: str
    buttons__try_again: str
    buttons__turn_off: str
    buttons__turn_on: str
    cardano__addr_base: str
    cardano__addr_enterprise: str
    cardano__addr_legacy: str
    cardano__addr_pointer: str
    cardano__addr_reward: str
    cardano__address_no_staking: str
    cardano__amount: str
    cardano__amount_burned: str
    cardano__amount_minted: str
    cardano__amount_sent: str
    cardano__anonymous_pool: str
    cardano__asset_fingerprint: str
    cardano__auxiliary_data_hash: str
    cardano__block: str
    cardano__catalyst: str
    cardano__certificate: str
    cardano__certificate_path: str
    cardano__change_output: str
    cardano__change_output_path: str
    cardano__change_output_staking_path: str
    cardano__check_all_items: str
    cardano__choose_level_of_details: str
    cardano__collateral_input_id: str
    cardano__collateral_input_index: str
    cardano__collateral_output_contains_tokens: str
    cardano__collateral_return: str
    cardano__confirm: str
    cardano__confirm_signing_stake_pool: str
    cardano__confirm_transaction: str
    cardano__confirming_a_multisig_transaction: str
    cardano__confirming_pool_registration: str
    cardano__confirming_transction: str
    cardano__cost: str
    cardano__credential_mismatch: str
    cardano__datum_hash: str
    cardano__delegating_to: str
    cardano__for_account: str
    cardano__for_key_hash: str
    cardano__for_script: str
    cardano__inline_datum: str
    cardano__input_id: str
    cardano__input_index: str
    cardano__intro_text_address: str
    cardano__intro_text_change: str
    cardano__intro_text_owned_by_device: str
    cardano__intro_text_registration_payment: str
    cardano__key_hash: str
    cardano__margin: str
    cardano__multisig_path: str
    cardano__nested_scripts_template: str
    cardano__network: str
    cardano__no_output_tx: str
    cardano__nonce: str
    cardano__other: str
    cardano__path: str
    cardano__pledge: str
    cardano__pointer: str
    cardano__policy_id: str
    cardano__pool_metadata_hash: str
    cardano__pool_metadata_url: str
    cardano__pool_owner: str
    cardano__pool_owner_path: str
    cardano__pool_reward_account: str
    cardano__reference_input_id: str
    cardano__reference_input_index: str
    cardano__reference_script: str
    cardano__required_signer: str
    cardano__reward: str
    cardano__reward_address: str
    cardano__reward_eligibility_warning: str
    cardano__rewards_go_to: str
    cardano__script: str
    cardano__script_all: str
    cardano__script_any: str
    cardano__script_data_hash: str
    cardano__script_hash: str
    cardano__script_invalid_before: str
    cardano__script_invalid_hereafter: str
    cardano__script_key: str
    cardano__script_n_of_k: str
    cardano__script_reward: str
    cardano__sending: str
    cardano__show_simple: str
    cardano__sign_tx_path_template: str
    cardano__stake_delegation: str
    cardano__stake_deregistration: str
    cardano__stake_pool_registration: str
    cardano__stake_pool_registration_pool_id: str
    cardano__stake_registration: str
    cardano__staking_key_for_account: str
    cardano__to_pool: str
    cardano__token_minting_path: str
    cardano__total_collateral: str
    cardano__transaction: str
    cardano__transaction_contains_minting_or_burning: str
    cardano__transaction_contains_script_address_no_datum: str
    cardano__transaction_fee: str
    cardano__transaction_id: str
    cardano__transaction_no_collateral_input: str
    cardano__transaction_no_script_data_hash: str
    cardano__transaction_output_contains_tokens: str
    cardano__ttl: str
    cardano__unknown: str
    cardano__unknown_collateral_amount: str
    cardano__unusual_path: str
    cardano__valid_since: str
    cardano__verify_script: str
    cardano__vote_key_registration: str
    cardano__vote_public_key: str
    cardano__voting_purpose: str
    cardano__warning: str
    cardano__weight: str
    cardano__withdrawal_for_address_template: str
    cardano__witness_path: str
    cardano__x_of_y_signatures_template: str
    coinjoin__access_account: str
    coinjoin__do_not_disconnect: str
    coinjoin__max_mining_fee: str
    coinjoin__max_rounds: str
    coinjoin__title: str
    coinjoin__title_do_not_disconnect: str
    coinjoin__title_progress: str
    coinjoin__waiting_for_others: str
    confirm_total__account: str
    confirm_total__fee_rate: str
    confirm_total__sending_from_account: str
    confirm_total__title_fee: str
    confirm_total__title_information: str
    confirm_total__title_sending_from: str
    debug__loading_seed: str
    debug__loading_seed_not_recommended: str
    device_name__change_template: str
    device_name__title: str
    entropy__send: str
    entropy__title: str
    entropy__title_confirm: str
    eos__about_to_sign_template: str
    eos__account: str
    eos__action_name: str
    eos__amount: str
    eos__arbitrary_data: str
    eos__buy_ram: str
    eos__bytes: str
    eos__cancel_vote: str
    eos__checksum: str
    eos__code: str
    eos__contract: str
    eos__cpu: str
    eos__creator: str
    eos__delegate: str
    eos__delete_auth: str
    eos__from: str
    eos__link_auth: str
    eos__memo: str
    eos__name: str
    eos__net: str
    eos__new_account: str
    eos__no: str
    eos__owner: str
    eos__parent: str
    eos__payer: str
    eos__permission: str
    eos__proxy: str
    eos__receiver: str
    eos__refund: str
    eos__requirement: str
    eos__sell_ram: str
    eos__sender: str
    eos__sign_transaction: str
    eos__threshold: str
    eos__to: str
    eos__transfer: str
    eos__type: str
    eos__undelegate: str
    eos__unlink_auth: str
    eos__update_auth: str
    eos__vote_for_producers: str
    eos__vote_for_proxy: str
    eos__voter: str
    eos__yes: str
    ethereum__amount_sent: str
    ethereum__confirm_fee: str
    ethereum__contract: str
    ethereum__data_size_template: str
    ethereum__gas_limit: str
    ethereum__gas_price: str
    ethereum__max_gas_price: str
    ethereum__name_and_version: str
    ethereum__new_contract: str
    ethereum__no_message_field: str
    ethereum__priority_fee: str
    ethereum__show_full_array: str
    ethereum__show_full_domain: str
    ethereum__show_full_message: str
    ethereum__show_full_struct: str
    ethereum__sign_eip712: str
    ethereum__title_confirm_data: str
    ethereum__title_confirm_domain: str
    ethereum__title_confirm_message: str
    ethereum__title_confirm_struct: str
    ethereum__title_confirm_typed_data: str
    ethereum__title_signing_address: str
    ethereum__units_template: str
    ethereum__unknown_token: str
    ethereum__valid_signature: str
    experimental_mode__enable: str
    experimental_mode__only_for_dev: str
    experimental_mode__title: str
    fido__already_registered: str
    fido__device_already_registered: str
    fido__device_already_registered_with_template: str
    fido__device_not_registered: str
    fido__does_not_belong: str
    fido__erase_credentials: str
    fido__export_credentials: str
    fido__not_registered: str
    fido__not_registered_with_template: str
    fido__please_enable_pin_protection: str
    fido__title_authenticate: str
    fido__title_import_credential: str
    fido__title_list_credentials: str
    fido__title_register: str
    fido__title_remove_credential: str
    fido__title_reset: str
    fido__title_u2f_auth: str
    fido__title_u2f_register: str
    fido__title_verify_user: str
    fido__unable_to_verify_user: str
    fido__wanna_erase_credentials: str
    homescreen__click_to_connect: str
    homescreen__click_to_unlock: str
    homescreen__title_backup_failed: str
    homescreen__title_backup_needed: str
    homescreen__title_coinjoin_authorized: str
    homescreen__title_experimental_mode: str
    homescreen__title_hold_to_lock: str
    homescreen__title_no_usb_connection: str
    homescreen__title_pin_not_set: str
    homescreen__title_seedless: str
    homescreen__title_set: str
    inputs__back: str
    inputs__cancel: str
    inputs__delete: str
    inputs__enter: str
    inputs__return: str
    inputs__show: str
    inputs__space: str
    joint__title: str
    joint__to_the_total_amount: str
    joint__you_are_contributing: str
    language__change_template: str
    language__set_default: str
    language__title_change: str
    lockscreen__tap_to_connect: str
    lockscreen__tap_to_unlock: str
    lockscreen__title_locked: str
    lockscreen__title_not_connected: str
    misc__decrypt_value: str
    misc__encrypt_value: str
    misc__title_suite_labeling: str
    modify_amount__address: str
    modify_amount__decrease_amount: str
    modify_amount__increase_amount: str
    modify_amount__new_amount: str
    modify_amount__title: str
    modify_fee__decrease_fee: str
    modify_fee__fee_rate: str
    modify_fee__increase_fee: str
    modify_fee__new_transaction_fee: str
    modify_fee__no_change: str
    modify_fee__title: str
    modify_fee__transaction_fee: str
    monero__confirm_export: str
    monero__confirm_fee: str
    monero__confirm_ki_sync: str
    monero__confirm_refresh: str
    monero__confirm_unlock_time: str
    monero__hashing_inputs: str
    monero__payment_id: str
    monero__postprocessing: str
    monero__processing: str
    monero__processing_inputs: str
    monero__processing_outputs: str
    monero__signing: str
    monero__signing_inputs: str
    monero__unlock_time_set_template: str
    monero__wanna_export_tx_der: str
    monero__wanna_export_tx_key: str
    monero__wanna_export_watchkey: str
    monero__wanna_start_refresh: str
    monero__wanna_sync_key_images: str
    nem__absolute: str
    nem__activate: str
    nem__add: str
    nem__confirm_action: str
    nem__confirm_address: str
    nem__confirm_creation_fee: str
    nem__confirm_fee: str
    nem__confirm_mosaic: str
    nem__confirm_multisig_fee: str
    nem__confirm_namespace: str
    nem__confirm_payload: str
    nem__confirm_properties: str
    nem__confirm_rental_fee: str
    nem__confirm_transfer_of: str
    nem__convert_account_to_multisig: str
    nem__cosign_transaction_for: str
    nem__cosignatory: str
    nem__create_mosaic: str
    nem__create_namespace: str
    nem__deactivate: str
    nem__decrease: str
    nem__description: str
    nem__divisibility_and_levy_cannot_be_shown: str
    nem__encrypted: str
    nem__final_confirm: str
    nem__immutable: str
    nem__increase: str
    nem__initial_supply: str
    nem__initiate_transaction_for: str
    nem__levy_divisibility: str
    nem__levy_fee: str
    nem__levy_fee_of: str
    nem__levy_mosaic: str
    nem__levy_namespace: str
    nem__levy_recipient: str
    nem__levy_type: str
    nem__modify_supply_for: str
    nem__modify_the_number_of_cosignatories_by: str
    nem__mutable: str
    nem__no: str
    nem__of: str
    nem__percentile: str
    nem__raw_units_template: str
    nem__remote_harvesting: str
    nem__remove: str
    nem__set_minimum_cosignatories_to: str
    nem__sign_tx_fee_template: str
    nem__supply_change: str
    nem__supply_units_template: str
    nem__transferable: str
    nem__under_namespace: str
    nem__unencrypted: str
    nem__unknown_mosaic: str
    nem__yes: str
    passphrase__access_hidden_wallet: str
    passphrase__always_on_device: str
    passphrase__from_host_not_shown: str
    passphrase__hidden_wallet: str
    passphrase__hide: str
    passphrase__next_screen_will_show_passphrase: str
    passphrase__please_enter: str
    passphrase__revoke_on_device: str
    passphrase__title_confirm: str
    passphrase__title_enter: str
    passphrase__title_hide: str
    passphrase__title_settings: str
    passphrase__title_source: str
    passphrase__turn_off: str
    passphrase__turn_on: str
    pin__change: str
    pin__changed: str
    pin__cursor_will_change: str
    pin__diff_from_wipe_code: str
    pin__disabled: str
    pin__enabled: str
    pin__enter: str
    pin__enter_new: str
    pin__entered_not_valid: str
    pin__info: str
    pin__invalid_pin: str
    pin__last_attempt: str
    pin__mismatch: str
    pin__pin_mismatch: str
    pin__please_check_again: str
    pin__reenter_new: str
    pin__reenter_to_confirm: str
    pin__should_be_long: str
    pin__title_check_pin: str
    pin__title_settings: str
    pin__title_wrong_pin: str
    pin__tries_left: str
    pin__turn_off: str
    pin__turn_on: str
    pin__wrong_pin: str
    progress__authenticity_check: str
    progress__done: str
    progress__loading_transaction: str
    progress__one_second_left: str
    progress__please_wait: str
    progress__processing: str
    progress__refreshing: str
    progress__signing_transaction: str
    progress__syncing: str
    progress__x_seconds_left_template: str
    reboot_to_bootloader__restart: str
    reboot_to_bootloader__title: str
    recovery__cancel_dry_run: str
    recovery__check_dry_run: str
    recovery__cursor_will_change: str
    recovery__dry_run_bip39_valid_match: str
    recovery__dry_run_bip39_valid_mismatch: str
    recovery__dry_run_slip39_valid_match: str
    recovery__dry_run_slip39_valid_mismatch: str
    recovery__enter_any_share: str
    recovery__enter_backup: str
    recovery__enter_different_share: str
    recovery__enter_share_from_diff_group: str
    recovery__group_num_template: str
    recovery__group_threshold_reached: str
    recovery__invalid_seed_entered: str
    recovery__invalid_share_entered: str
    recovery__more_shares_needed: str
    recovery__num_of_words: str
    recovery__only_2_to_three_words: str
    recovery__only_first_letters: str
    recovery__progress_will_be_lost: str
    recovery__select_num_of_words: str
    recovery__share_already_entered: str
    recovery__share_from_another_shamir: str
    recovery__share_num_template: str
    recovery__title: str
    recovery__title_cancel_dry_run: str
    recovery__title_cancel_recovery: str
    recovery__title_dry_run: str
    recovery__title_recover: str
    recovery__title_remaining_shares: str
    recovery__type_word_x_of_y_template: str
    recovery__wallet_recovered: str
    recovery__wanna_cancel_dry_run: str
    recovery__wanna_cancel_recovery: str
    recovery__word_count_template: str
    recovery__word_x_of_y_template: str
    recovery__x_of_y_entered_template: str
    recovery__you_have_entered: str
    reset__advanced_group_threshold_info: str
    reset__all_x_of_y_template: str
    reset__any_x_of_y_template: str
    reset__button_create: str
    reset__button_recover: str
    reset__by_continuing: str
    reset__check_backup_title: str
    reset__check_group_share_title_template: str
    reset__check_seed_title: str
    reset__check_share_title_template: str
    reset__continue_with_next_share: str
    reset__continue_with_share_template: str
    reset__finished_verifying_group_template: str
    reset__finished_verifying_seed: str
    reset__finished_verifying_shares: str
    reset__group_description: str
    reset__group_info: str
    reset__group_share_checked_successfully_template: str
    reset__group_share_title_template: str
    reset__more_info_at: str
    reset__need_all_share_template: str
    reset__need_any_share_template: str
    reset__needed_to_form_a_group: str
    reset__needed_to_recover_your_wallet: str
    reset__never_make_digital_copy: str
    reset__num_of_share_holders_template: str
    reset__num_of_shares_advanced_info_template: str
    reset__num_of_shares_basic_info: str
    reset__num_shares_for_group_template: str
    reset__number_of_shares_info: str
    reset__one_share: str
    reset__only_one_share_will_be_created: str
    reset__recovery_seed_title: str
    reset__recovery_share_title_template: str
    reset__required_number_of_groups: str
    reset__select_correct_word: str
    reset__select_word_template: str
    reset__select_word_x_of_y_template: str
    reset__set_it_to_count_template: str
    reset__share_checked_successfully_template: str
    reset__share_words_title: str
    reset__slip39_checklist_num_groups: str
    reset__slip39_checklist_num_shares: str
    reset__slip39_checklist_set_num_groups: str
    reset__slip39_checklist_set_num_shares: str
    reset__slip39_checklist_set_sizes: str
    reset__slip39_checklist_set_sizes_longer: str
    reset__slip39_checklist_set_threshold: str
    reset__slip39_checklist_title: str
    reset__slip39_checklist_write_down: str
    reset__slip39_checklist_write_down_recovery: str
    reset__the_threshold_sets_the_number_of_shares: str
    reset__threshold_info: str
    reset__title_backup_is_done: str
    reset__title_create_wallet: str
    reset__title_create_wallet_shamir: str
    reset__title_group_threshold: str
    reset__title_number_of_groups: str
    reset__title_number_of_shares: str
    reset__title_set_group_threshold: str
    reset__title_set_number_of_groups: str
    reset__title_set_number_of_shares: str
    reset__title_set_threshold: str
    reset__to_form_group_template: str
    reset__tos_link: str
    reset__total_number_of_shares_in_group_template: str
    reset__use_your_backup: str
    reset__write_down_words_template: str
    reset__wrong_word_selected: str
    reset__you_need_one_share: str
    reset__your_backup_is_done: str
    ripple__confirm_tag: str
    ripple__destination_tag_template: str
    rotation__change_template: str
    rotation__east: str
    rotation__north: str
    rotation__south: str
    rotation__title_change: str
    rotation__west: str
    safety_checks__approve_unsafe_always: str
    safety_checks__approve_unsafe_temporary: str
    safety_checks__enforce_strict: str
    safety_checks__title: str
    safety_checks__title_safety_override: str
    sd_card__all_data_will_be_lost: str
    sd_card__card_required: str
    sd_card__disable: str
    sd_card__disabled: str
    sd_card__enable: str
    sd_card__enabled: str
    sd_card__error: str
    sd_card__format_card: str
    sd_card__insert_correct_card: str
    sd_card__please_insert: str
    sd_card__please_unplug_and_insert: str
    sd_card__problem_accessing: str
    sd_card__refresh: str
    sd_card__refreshed: str
    sd_card__restart: str
    sd_card__title: str
    sd_card__title_problem: str
    sd_card__unknown_filesystem: str
    sd_card__unplug_and_insert_correct: str
    sd_card__use_different_card: str
    sd_card__wanna_format: str
    sd_card__wrong_sd_card: str
    send__address_path: str
    send__amount: str
    send__confirm_sending: str
    send__from_multiple_accounts: str
    send__including_fee: str
    send__maximum_fee: str
    send__receiving_to_multisig: str
    send__title_amount: str
    send__title_confirm_sending: str
    send__title_joint_transaction: str
    send__title_receiving_to: str
    send__title_recipient: str
    send__title_sending: str
    send__title_sending_amount: str
    send__title_sending_to: str
    send__to_the_total_amount: str
    send__total_amount: str
    send__transaction_id: str
    send__you_are_contributing: str
    share_words__words_in_order: str
    share_words__wrote_down_all: str
    sign_message__confirm_address: str
    sign_message__confirm_message: str
    stellar__account: str
    stellar__account_merge: str
    stellar__account_thresholds: str
    stellar__add_signer: str
    stellar__add_trust: str
    stellar__all_will_be_sent_to: str
    stellar__allow_trust: str
    stellar__asset: str
    stellar__bump_sequence: str
    stellar__buying: str
    stellar__clear_data: str
    stellar__clear_flags: str
    stellar__confirm_issuer: str
    stellar__confirm_memo: str
    stellar__confirm_network: str
    stellar__confirm_operation: str
    stellar__confirm_stellar: str
    stellar__confirm_timebounds: str
    stellar__create_account: str
    stellar__debited_amount: str
    stellar__delete: str
    stellar__delete_passive_offer: str
    stellar__delete_trust: str
    stellar__destination: str
    stellar__exchanges_require_memo: str
    stellar__final_confirm: str
    stellar__hash: str
    stellar__high: str
    stellar__home_domain: str
    stellar__inflation: str
    stellar__initial_balance: str
    stellar__initialize_signing_with: str
    stellar__issuer_template: str
    stellar__key: str
    stellar__limit: str
    stellar__low: str
    stellar__master_weight: str
    stellar__medium: str
    stellar__new_offer: str
    stellar__new_passive_offer: str
    stellar__no_memo_set: str
    stellar__no_restriction: str
    stellar__on_network_template: str
    stellar__path_pay: str
    stellar__path_pay_at_least: str
    stellar__pay: str
    stellar__pay_at_most: str
    stellar__preauth_transaction: str
    stellar__price_per_template: str
    stellar__private_network: str
    stellar__remove_signer: str
    stellar__revoke_trust: str
    stellar__selling: str
    stellar__set_data: str
    stellar__set_flags: str
    stellar__set_sequence_to_template: str
    stellar__sign_tx_count_template: str
    stellar__sign_tx_fee_template: str
    stellar__source_account: str
    stellar__testnet_network: str
    stellar__trusted_account: str
    stellar__update: str
    stellar__valid_from: str
    stellar__valid_to: str
    stellar__value_sha256: str
    stellar__wanna_clean_value_key_template: str
    stellar__your_account: str
    tezos__address: str
    tezos__amount: str
    tezos__baker_address: str
    tezos__balance: str
    tezos__ballot: str
    tezos__confirm_delegation: str
    tezos__confirm_origination: str
    tezos__delegator: str
    tezos__fee: str
    tezos__proposal: str
    tezos__register_delegate: str
    tezos__remove_delegation: str
    tezos__submit_ballot: str
    tezos__submit_proposal: str
    tezos__submit_proposals: str
    tutorial__middle_click: str
    tutorial__press_and_hold: str
    tutorial__ready_to_use: str
    tutorial__scroll_down: str
    tutorial__sure_you_want_skip: str
    tutorial__title_hello: str
    tutorial__title_screen_scroll: str
    tutorial__title_skip: str
    tutorial__title_tutorial_complete: str
    tutorial__use_trezor: str
    tutorial__welcome_press_right: str
    u2f__get: str
    u2f__set_template: str
    u2f__title_get: str
    u2f__title_set: str
    wipe__info: str
    wipe__title: str
    wipe__want_to_wipe: str
    wipe_code__change: str
    wipe_code__changed: str
    wipe_code__diff_from_pin: str
    wipe_code__disabled: str
    wipe_code__enabled: str
    wipe_code__enter_new: str
    wipe_code__info: str
    wipe_code__invalid: str
    wipe_code__mismatch: str
    wipe_code__reenter: str
    wipe_code__reenter_to_confirm: str
    wipe_code__title_check: str
    wipe_code__title_invalid: str
    wipe_code__title_settings: str
    wipe_code__turn_off: str
    wipe_code__turn_on: str
    wipe_code__wipe_code_mismatch: str
    word_count__title: str
    words__are_you_sure: str
    words__buying: str
    words__continue_anyway: str
    words__continue_with: str
    words__error: str
    words__from: str
    words__keep_it_safe: str
    words__know_what_your_doing: str
    words__my_trezor: str
    words__outputs: str
    words__please_check_again: str
    words__please_try_again: str
    words__really_wanna: str
    words__sign: str
    words__title_check: str
    words__title_group: str
    words__title_remember: str
    words__title_share: str
    words__title_shares: str
    words__title_success: str
    words__title_summary: str
    words__title_threshold: str
    words__unknown: str
    words__warning: str
