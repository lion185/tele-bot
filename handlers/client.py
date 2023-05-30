from aiogram import types, Dispatcher
from aiogram.types import CallbackQuery, Message
from init_jarvis import dp, bot
from data_base.mainDB import *
from keyboards import calendarMainKb, pornFirstFlowKb, pornStarsUrlKb, genresUrlKb
from settings.Math.checkUsersReg import checkUsersOfRegInDb
import datetime

async def start_calendar_command(message: Message):
    user_id = message.from_user.id
    var = await checkUsersOfRegInDb(user_id)
    if var == True:
        await message.answer("<b>Календарь...</b>", reply_markup=calendarMainKb)
    elif var == False:
        await bot.send_message(chat_id=user_id, text="<b>Для начала пройди регистрацию!</b>")

@dp.callback_query_handler(text="showTotalTimesSex")
async def showTimesSexFunc(call: CallbackQuery):
    user_id = call.from_user.id
    var_total = await showTotalTimesSexDb(user_id)
    var_mounth = await showMounthTimesSexDb(user_id)
    var_day = await showDayTimesSexDb(user_id)
    await bot.send_message(chat_id=user_id, text=f"<b>Статистика мастурбаций:\nНа данный момент: {var_total[0]} - в общей сложности\nНа данный момент: {var_mounth[0]} - за этот месяц</b>\nНа данный момент: {var_day[0]} - за этот день")
    await call.answer()

@dp.callback_query_handler(text="addTimeSex")
async def addTimeSexFunc(call: CallbackQuery):
    user_id = call.from_user.id
    var = await addOneTimeSexDb(user_id)
    await call.message.answer(var)

@dp.callback_query_handler(text="wantFuksNaw")
async def wantFuksNawFunc(call: CallbackQuery):
    user_id = call.from_user.id
    day_now = datetime.datetime.today().weekday()
    if day_now >= 5:
        await bot.send_message(chat_id=user_id, text="Заканчивал бы ты мутузить соску в форме члена. Нужно херачить с 5 утра, пока все лохи спят. Ебашить до талого: спорт, наука, хобби. Постарайся сокращать количество подходов на змеиный удушающий", reply_markup=pornFirstFlowKb)
    else:
        await bot.send_message(chat_id=user_id, text="Сегодня запрещаю прикосаться к тёплому Дон Жуану. Сейчас встал и 50 отжиманий!")
    await call.answer()

@dp.callback_query_handler(text="statisticTimesSex")
async def statisticTimesSexFunc(call: CallbackQuery, old = None):
    await call.answer("Советую не удалять историю чата, чтобы я мог высчитывать прогрессию статистики)")
    user_id = call.from_user.id
    var_total = await showTotalTimesSexDb(user_id)
    var_mounth = await showMaxStatisticOfMounthDb(user_id)
    var_day = await showMaxStatisticOfDayDb(user_id)
    await bot.send_message(chat_id=user_id, text=f"<b>Статистика за всё время:\nМаксимальное количество за всё время: {var_total[0]}\nМаксимальное количество за месяц: {var_mounth[0]}\nМаксимально количество за день: {var_day[0]}</b>")
    await call.answer()

@dp.callback_query_handler(text="pornstars")
async def showPornStarsFunc(call: CallbackQuery):
    user_id = call.from_user.id
    day_now = datetime.datetime.today().weekday()
    if day_now >= 5:
        await bot.send_message(chat_id=user_id, text="<b>Выбирай</b>", reply_markup=pornStarsUrlKb)
    else:
        await bot.send_message(chat_id=user_id, text="Сегодня запрещаю прикосаться к тёплому Дон Жуану. Сейчас встал и 50 отжиманий!")
    await call.answer()

@dp.callback_query_handler(text="genresPorn")
async def showGenresPornFunc(call: CallbackQuery):
    user_id = call.from_user.id
    day_now = datetime.datetime.today().weekday()
    if day_now >= 5:
        await bot.send_message(chat_id=user_id, text="<b>Жанры</b>", reply_markup=genresUrlKb)
    else:
        await bot.send_message(chat_id=user_id, text="Сегодня запрещаю прикосаться к тёплому Дон Жуану. Сейчас встал и 50 отжиманий!")
    await call.answer()

@dp.callback_query_handler(text="reminderOfSex")
async def reminderOnOrOff(call: CallbackQuery):
    pass

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_calendar_command, commands=['calendar'])