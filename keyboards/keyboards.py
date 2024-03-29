from aiogram import Bot
from aiogram import types
from lexicon.lexicon import LEXICON_RU, LEXICON_CMD, LEXICON_WORD

card_but = types.KeyboardButton(text=LEXICON_RU['card_button'])
hang_but = types.KeyboardButton(text=LEXICON_RU['hanged_button'])
what_game_kb = types.ReplyKeyboardMarkup(keyboard=[[card_but,hang_but]])

get_word_but = types.KeyboardButton(text=LEXICON_WORD['get_word'])
get_word_kb = types.ReplyKeyboardMarkup(keyboard= [[get_word_but]])


async def set_main_menu(bot: Bot):
    main_menu_commands = [
        types.BotCommand(
            command=command,
            description=description
        ) for command, description in LEXICON_CMD.items()
    ]
    await bot.set_my_commands(main_menu_commands)