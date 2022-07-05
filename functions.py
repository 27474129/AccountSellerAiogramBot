from keyboards.inline.client_inline import SteamClientInline
from states.select_account import SelectAccount

cl_inline = SteamClientInline()


def get_keyboard(current_game):
    if (current_game == "dota2"):
        return cl_inline.get_dota_keyboard()
    elif (current_game == "gta5"):
        return
    elif (current_game == "csgo"):
        return

async def back_from_select_price_state(state):
    async with state.proxy() as data:
        required_state = data["current_game"]

    if (required_state == "dota2"):
        await state.set_state(SelectAccount.dota2)
        keyboard = cl_inline.get_dota_keyboard()
    elif (required_state == "csgo"):
        await state.set_state(SelectAccount.csgo)
    elif (required_state == "gta5"):
        await state.set_state(SelectAccount.gta5)
    else:
        return
    return required_state