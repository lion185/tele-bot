from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

mainKeyboardInline = InlineKeyboardMarkup(row_width=1)
callAllPride = InlineKeyboardButton(text="Вызвать весь прайд!", callback_data="callAllPride")
mainKeyboardInline.add(callAllPride)