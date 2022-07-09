from keyboards.inline.DotaClientInline import DotaClientInline
from keyboards.inline.CsgoClientInline import CsgoClientInline
from keyboards.inline.GtaClientInline import GtaClientInline
from states.SelectAccount import SelectAccount

dota_inline = DotaClientInline()
csgo_inline = CsgoClientInline()
gta_inline = GtaClientInline()


def get_keyboard_by_game(current_game, buttons_to_change):
    if (current_game == "dota"):
        return dota_inline.get_dota_keyboard(buttons_to_change)
    if (current_game == "gta"):
        return gta_inline.get_gta_keyboard(buttons_to_change)
    if (current_game == "csgo"):
        return csgo_inline.get_csgo_keyboard(buttons_to_change)


async def get_filter_keyboard_and_set_filter_state(current_filter, current_game):
    if (current_filter == "ratings"):
        await SelectAccount.set_dota_rating.set()
        return dota_inline.get_dota_rating_sheet()

    if (current_filter == "lvl"):
        await SelectAccount.set_dota_account_lvl.set()
        return dota_inline.get_dota_account_lvls_sheet()

    if (current_filter == "dota_hours"):
        await SelectAccount.set_dota_hours.set()
        return dota_inline.get_dota_hours_sheet()

    if (current_filter == "decency"):
        await SelectAccount.set_dota_decency.set()
        return dota_inline.get_dota_decency_sheet()

    if (current_filter == "ranks"):
        await SelectAccount.set_csgo_rank.set()
        return csgo_inline.get_csgo_ranks_keyboard()

    if (current_filter == "faceit"):
        await SelectAccount.set_csgo_faceit.set()
        return csgo_inline.get_csgo_faceit_keyboard()

    if (current_filter == "prime"):
        await SelectAccount.set_csgo_prime.set()
        return csgo_inline.get_csgo_prime_keyboard()

    if (current_filter == "csgo_hours"):
        await SelectAccount.set_csgo_hours.set()
        return dota_inline.get_dota_hours_sheet()

    if (current_filter == "char_lvl"):
        await SelectAccount.set_gta_char_lvl.set()
        return gta_inline.get_gta_char_lvl_keyboard()

    if (current_filter == "balance"):
        await SelectAccount.set_gta_balance.set()
        return gta_inline.get_gta_balance_keyboard()

    if (current_filter == "edition"):
        await SelectAccount.set_gta_edition.set()
        return gta_inline.get_gta_edition_keyboard()

async def set_select_state(state):
    async with state.proxy() as data:
        required_state = data["current_game"]

    if (required_state == "dota"):
        await state.set_state(SelectAccount.dota)
    elif (required_state == "csgo"):
        await state.set_state(SelectAccount.csgo)
    elif (required_state == "gta"):
        await state.set_state(SelectAccount.gta)

