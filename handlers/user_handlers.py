from aiogram.types import Message,ReplyKeyboardRemove
from aiogram.filters import Command,CommandStart
from aiogram import Router,F
from lexicon.lexicon import LEXICON_RU,LEXICON_WORD
from services.words_game import wordGame
from sqlite3 import Connection
from keyboards.keyboards import what_game_kb, get_word_kb, stop_kb

router = Router()
game = wordGame()

# Этот хэндлер будет срабатывать на команду "/start"
@router.message(Command(commands=["start"]))
async def process_start_command(message: Message, dbConnect: Connection):
    await message.answer(LEXICON_RU['start'], reply_markup=what_game_kb)

# Этот хэндлер будет срабатывать на команду "/creator"
@router.message(Command(commands=['creator']))
async def process_help_command(message: Message):
    await message.answer(LEXICON_RU['creator'])

# Этот хэндлер будет срабатывать на кнопку играть в виселицу
@router.message(F.text == LEXICON_RU['hanged_button'])
async def process_word_need(message: Message):
    await message.answer(LEXICON_RU['hang_need'],reply_markup= ReplyKeyboardRemove())
    await message.answer(LEXICON_WORD['ready_to_play'], reply_markup= get_word_kb)

# Этот хэндлер будет срабатывать на кнопу отмены
@router.message(F.text == LEXICON_RU['cancel'])
async def process_cancel(message: Message):
    await message.answer(LEXICON_RU['cancel_start'],reply_markup=what_game_kb)

# Этот хэндлер срабатывает для получения слова
@router.message(F.text == LEXICON_WORD['get_word'])
async def process_game_command(message: Message):
    await message.answer(text=LEXICON_WORD['you_word'], reply_markup=ReplyKeyboardRemove())
    if game.status:
        await message.answer(text='Игра уже запущена! Отгадывайте слово')
        return
    try:
        msg = await game.getWord()
    except:
        msg = 'У меня нет слов (('
    await message.answer(text=msg,reply_markup=stop_kb)

# Этот хэндлер срабатывает при угадывании слова по буквам
@router.message(lambda message: len(message.text) == 1 and game.status)
async def process_check_symb(message: Message):
    answer = game.checkSymb(message.text)
    if answer == 'win':
        game.stop()
        await message.answer(text=f'Победил {message.from_user.full_name}!🎉🎉')
        await message.answer(text=LEXICON_RU['again_answ'],reply_markup= get_word_kb)
    elif answer:
        await message.answer(text=answer)
        await message.answer(text=f'Использованные символы: {game.getUsedSymbols()}')
    else:
        game.stop()
        await message.answer(text='Словом было:')
        await message.answer(text=game.stop())
        await message.answer(text='Не расстраивайтесь, сыграем еще раз?', reply_markup=get_word_kb)

# Этот хэндлер срабатывает при угадывании слова целиком
@router.message(lambda message: message.text == game.word)
async def process_win(message: Message):
    if game.status:
        game.stop()
        await message.answer(text=f'Победил {message.from_user.full_name}!🎉🎉')
        await message.answer(text=LEXICON_RU['again_answ'], reply_markup=get_word_kb)

# Этот хэндлер срабатывает при остановке игры
@router.message(F.text == LEXICON_RU['stop_game'])
async def process_stop_game(message: Message):
    game.stop()
    await message.answer(text='Игра остановлена⛔')
    await message.answer(text='Но всегда можно начать новую!', reply_markup=get_word_kb)
