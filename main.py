"""
Created on Thu Mar 14 21:55:10 2024

@author: Asadbek
"""

import logging


from aiogram import Bot, Dispatcher, executor, types
from functions import get_times


PROXY_URL = "http://proxy.server:3128" #zarur emas, pythonanywhere serveri ishlashi uchun

API_TOKEN = 'YOUR API TOKEN'


# Configure logging

logging.basicConfig(level=logging.INFO)


# Initialize bot and dispatcher

bot = Bot(token=TOKEN)

dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])

async def send_welcome(msg: types.Message):

    """

    This handler will be called when user sends `/start` command

    """
    name = msg.from_user.first_name
    text = f"Assalomu aleykum {name}.\n\n"
    text += "Saharlik va iftorlik vaqtlarini bilib oling.\n"
    text += "Mintaqani tanlang:\n"
    text += "/Andijon \n/Fargona \n/Buxoro \n/Jizzah \n/Urganch \n/Namangan \n/Navoiy \n/Qarshi \n/Nukus \n/Samarqand \n/Guliston \n/Termiz \n/Toshkent \n/Rishton \n"
    await bot.send_message(msg.from_user.id, text=text)



# Mintaqalar

@dp.message_handler(commands=['andijon'])

async def send_welcome(msg: types.Message):
    times = get_times('andijon')
    text = "Andijon shahri uchun \n\n"
    text += f"Saharlik vaqti: {times[0]} \n"
    text += f"Iftorlik vaqti: {times[1]} \n\n"
    text += "Ma'lumotlar islom.uz saytidan olindi."
    await bot.send_message(msg.from_user.id, text=text)


@dp.message_handler(commands=['fargona'])

async def send_welcome(msg: types.Message):
    times = get_times("fergana")
    text = "Farg'ona shahri uchun \n\n"
    text += f"Saharlik vaqti: {times[0]} \n"
    text += f"Iftorlik vaqti: {times[1]} \n\n"
    text += "Ma'lumotlar islom.uz saytidan olindi."
    await bot.send_message(msg.from_user.id, text=text)
    
@dp.message_handler(commands=['buxoro'])

async def send_welcome(msg: types.Message):
    times = get_times('buxoro')
    text = "Buxoro shahri uchun \n\n"
    text += f"Saharlik vaqti: {times[0]} \n"
    text += f"Iftorlik vaqti: {times[1]} \n\n"
    text += "Ma'lumotlar islom.uz saytidan olindi."
    await bot.send_message(msg.from_user.id, text=text)
    
@dp.message_handler(commands=['jizzah'])

async def send_welcome(msg: types.Message):
    times = get_times('jizzah')
    text = "Jizzah shahri uchun \n\n"
    text += f"Saharlik vaqti: {times[0]} \n"
    text += f"Iftorlik vaqti: {times[1]} \n\n"
    text += "Ma'lumotlar islom.uz saytidan olindi."
    await bot.send_message(msg.from_user.id, text=text)


@dp.message_handler(commands=['urganch'])

async def send_welcome(msg: types.Message):
    times = get_times('urganch')
    text = "Urganch shahri uchun \n\n"
    text += f"Saharlik vaqti: {times[0]} \n"
    text += f"Iftorlik vaqti: {times[1]} \n\n"
    text += "Ma'lumotlar islom.uz saytidan olindi."
    await bot.send_message(msg.from_user.id, text=text)
    

@dp.message_handler(commands=['namangan'])

async def send_welcome(msg: types.Message):
    times = get_times('namangan')
    text = "Namangan shahri uchun \n\n"
    text += f"Saharlik vaqti: {times[0]} \n"
    text += f"Iftorlik vaqti: {times[1]} \n\n"
    text += "Ma'lumotlar islom.uz saytidan olindi."
    await bot.send_message(msg.from_user.id, text=text)
    
    
@dp.message_handler(commands=['navoiy'])

async def send_welcome(msg: types.Message):
    times = get_times('navoiy')
    text = "Navoiy shahri uchun \n\n"
    text += f"Saharlik vaqti: {times[0]} \n"
    text += f"Iftorlik vaqti: {times[1]} \n\n"
    text += "Ma'lumotlar islom.uz saytidan olindi."
    await bot.send_message(msg.from_user.id, text=text)
    
    
@dp.message_handler(commands=['qarshi'])

async def send_welcome(msg: types.Message):
    times = get_times('qarshi')
    text = "Qarshi shahri uchun \n\n"
    text += f"Saharlik vaqti: {times[0]} \n"
    text += f"Iftorlik vaqti: {times[1]} \n\n"
    text += "Ma'lumotlar islom.uz saytidan olindi."
    await bot.send_message(msg.from_user.id, text=text)
    
    
@dp.message_handler(commands=['nukus'])

async def send_welcome(msg: types.Message):
    times = get_times('nukus')
    text = "Nukus shahri uchun \n\n"
    text += f"Saharlik vaqti: {times[0]} \n"
    text += f"Iftorlik vaqti: {times[1]} \n\n"
    text += "Ma'lumotlar islom.uz saytidan olindi."
    await bot.send_message(msg.from_user.id, text=text)
    
    
@dp.message_handler(commands=['samarqand'])

async def send_welcome(msg: types.Message):
    times = get_times('samarqand')
    text = "Samarqand shahri uchun \n\n"
    text += f"Saharlik vaqti: {times[0]} \n"
    text += f"Iftorlik vaqti: {times[1]} \n\n"
    text += "Ma'lumotlar islom.uz saytidan olindi."
    await bot.send_message(msg.from_user.id, text=text)
    
    
@dp.message_handler(commands=['guliston'])

async def send_welcome(msg: types.Message):
    times = get_times('guliston')
    text = "Guliston shahri uchun \n\n"
    text += f"Saharlik vaqti: {times[0]} \n"
    text += f"Iftorlik vaqti: {times[1]} \n\n"
    text += "Ma'lumotlar islom.uz saytidan olindi."
    await bot.send_message(msg.from_user.id, text=text)



@dp.message_handler(commands=['termiz'])

async def send_welcome(msg: types.Message):
    times = get_times('termiz')
    text = "Termiz shahri uchun \n\n"
    text += f"Saharlik vaqti: {times[0]} \n"
    text += f"Iftorlik vaqti: {times[1]} \n\n"
    text += "Ma'lumotlar islom.uz saytidan olindi."
    await bot.send_message(msg.from_user.id, text=text)
    
    
@dp.message_handler(commands=['toshkent'])

async def send_welcome(msg: types.Message):
    times = get_times('toshkent')
    text = "Toshkent shahri uchun \n\n"
    text += f"Saharlik vaqti: {times[0]} \n"
    text += f"Iftorlik vaqti: {times[1]} \n\n"
    text += "Ma'lumotlar islom.uz saytidan olindi."
    await bot.send_message(msg.from_user.id, text=text)


@dp.message_handler(commands=['rishton'])

async def send_welcome(msg: types.Message):
    times = get_times('rishton')
    text = "Rishton tumani uchun \n\n"
    text += f"Saharlik vaqti: {times[0]} \n"
    text += f"Iftorlik vaqti: {times[1]} \n\n"
    text += "Ma'lumotlar islom.uz saytidan olindi."
    await bot.send_message(msg.from_user.id, text=text)
    
  
if __name__ == '__main__':

    executor.start_polling(dp, skip_updates=True)
