from keyboards.inline.client_inline import SteamClientInline
from states.select_account import SelectAccount

cl_inline = SteamClientInline()


def get_keyboard(current_game, buttons_to_change):
    if (current_game == "dota"):
        return cl_inline.get_dota_keyboard(buttons_to_change)
    elif (current_game == "gta5"):
        return
    elif (current_game == "csgo"):
        return

async def back_from_select_state(state):
    async with state.proxy() as data:
        required_state = data["current_game"]

    if (required_state == "dota"):
        await state.set_state(SelectAccount.dota)
    elif (required_state == "csgo"):
        await state.set_state(SelectAccount.csgo)
    elif (required_state == "gta5"):
        await state.set_state(SelectAccount.gta5)
    else:
        return