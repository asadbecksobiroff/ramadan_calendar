import logging

from aiogram import Bot, Dispatcher, executor, types
from functions import get_times, get_day_info
from config import API_TOKEN

# Configure logging

logging.basicConfig(level=logging.INFO)


# Initialize bot and dispatcher

bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])

async def start(msg: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    name = msg.from_user.first_name
    text = f"Assalomu alaykum {name}.\n\n"
    text += "Saharlik va iftorlik vaqtlarini bilib oling.\n"
    text += "Mintaqani tanlang👇"
    
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [["Andijon", "Buxoro"]]
    buttons.append(["Farg'ona", "Guliston"])
    buttons.append(["Jizzah", "Namangan"])
    buttons.append(["Navoiy", "Nukus"])
    buttons.append(["Qarshi", "Rishton"])
    buttons.append(["Samarqand", "Termiz"])
    buttons.append(["Toshkent", "Urganch"])
    
    keyboard.add(*buttons[0])
    keyboard.add(*buttons[1])
    keyboard.add(*buttons[2])
    keyboard.add(*buttons[3])
    keyboard.add(*buttons[4])
    keyboard.add(*buttons[5])
    keyboard.add(*buttons[6])
        
    await bot.send_message(msg.from_user.id, text=text, reply_markup=keyboard)
    
    

@dp.message_handler()

async def send_time(msg: types.Message):
    cities = ["Andijon", "Buxoro", "Farg'ona", "Guliston", "Jizzah", "Namangan", "Navoiy", "Nukus", "Qarshi", "Rishton", "Samarqand", "Termiz", "Toshkent", "Urganch"]
    city = msg.text

    if city not in cities:
        await bot.send_message(msg.from_user.id, text="Ushbu shahar/tuman uchun ma'lumot topilmadi")
    
    else:
        times = get_times(city.lower())
        
        if times:        
            text = get_day_info()
            text += f"\n{city} vaqti bo'yicha \n\n"
            text += f"Saharlik vaqti: {times[0]} \n"
            text += f"Iftorlik vaqti: {times[1]} \n\n"
            text += "©️Ma'lumotlar islom.uz saytidan olindi."
            await bot.send_message(msg.from_user.id, text=text)
            
        else:
            await bot.send_message(msg.from_user.id, text="Qandaydir xatolik bo'ldi, qaytadan urinib ko'ring")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
