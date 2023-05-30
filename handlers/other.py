from aiogram.types import Message, CallbackQuery
from aiogram import Dispatcher
from init_jarvis import dp, bot
from data_base.mainDB import *
from keyboards.other_kb import mainKeyboardInline
from settings.Math.checkUsersReg import checkUsersOfRegInDb
from settings.answerText.compliteAnswer import CompliteAnswer

async def writeNewUsersInDb(message: Message):
    user_id = message.from_user.id
    name = message.from_user.first_name
    var = await addNewUsersInDb(user_id, name)
    await message.answer(f"<b>{var}</b>")


async def mainCommandListFunc(message: Message):
    user_id = message.from_user.id
    name = message.from_user.first_name
    var = await checkUsersOfRegInDb(user_id)
    if var == True:
        await message.answer("<b>Вот, что умею...</b>", reply_markup=mainKeyboardInline)
    elif var == False:
        await bot.send_message(chat_id=user_id, text="<b>Для начала пройди регистрацию!</b>")

@dp.callback_query_handler(text="callAllPride")
async def callAllPride(call:CallbackQuery):
    await call.message.answer(f"{CompliteAnswer.callAllMans}")
    await call.answer()


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(mainCommandListFunc, commands=['main'])
    dp.register_message_handler(writeNewUsersInDb, commands=['start'])