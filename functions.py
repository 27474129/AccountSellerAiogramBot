from keyboards.inline.ClientInline import ClientInline
from states.SelectAccount import SelectAccount

cl_inline = ClientInline()


def get_keyboard_by_game(current_game, buttons_to_change):
    if (current_game == "dota"):
        return cl_inline.get_dota_keyboard(buttons_to_change)
    elif (current_game == "gta5"):
        return
    elif (current_game == "csgo"):
        return

async def get_filter_keyboard_and_set_filter_state(current_filter):
    if (current_filter == "ratings"):
        await SelectAccount.set_dota_rating.set()
        return cl_inline.get_dota_rating_sheet()

    if (current_filter == "lvl"):
        await SelectAccount.set_dota_account_lvl.set()
        return cl_inline.get_dota_account_lvls_sheet()

    if (current_filter == "hours"):
        await SelectAccount.set_dota_hours.set()
        return cl_inline.get_dota_hours_sheet()

    if (current_filter == "decency"):
        await SelectAccount.set_dota_decency.set()
        return cl_inline.get_dota_decency_sheet()

async def set_select_state(state):
    async with state.proxy() as data:
        required_state = data["current_game"]

    if (required_state == "dota"):
        await state.set_state(SelectAccount.dota)
    elif (required_state == "csgo"):
        await state.set_state(SelectAccount.csgo)
    elif (required_state == "gta5"):
        await state.set_state(SelectAccount.gta5)