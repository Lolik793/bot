import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, html, F
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, FSInputFile

TOKEN = "8335473611:AAEiyemFmSG3RzJ0V9Au9zyTLkaAr45qbjI"

bot = Bot(token=TOKEN)
dp = Dispatcher()

logging.basicConfig(level=logging.DEBUG)

BANNER_MAIN = "banner.png"
BANNER_MODEL = "banner_model.png"
BANNER_USERNAME = "banner_username.png"
BANNER_INFO = "banner_info.png"

def get_main_menu():
    buttons = [
        [InlineKeyboardButton(text="⚔️ Каталог 3D Моделей", callback_data="open_models")],
        [InlineKeyboardButton(text="🆔 Премиум Юзернеймы", callback_data="open_usernames")],
        [InlineKeyboardButton(text="🎨 Дизайн / Сайты / Карточки", callback_data="open_design")],
        [InlineKeyboardButton(text="👤 Мой Профиль / Баланс", callback_data="open_profile")],
        [InlineKeyboardButton(text="🏪 Посетить магазин Astrix на FunPay", url="https://funpay.com/users/14410614/")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def get_models_menu():
    buttons = [
        [InlineKeyboardButton(text="🛒 Купить 3D Модели на FunPay", url="https://funpay.com/lots/offer?id=64793664")],
        [InlineKeyboardButton(text="⬅️ Назад в меню", callback_data="back_to_main")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def get_usernames_menu():
    buttons = [
        [InlineKeyboardButton(text="🛒 Купить Юзернеймы на FunPay", url="https://funpay.com/lots/offer?id=69365909")],
        [InlineKeyboardButton(text="⬅️ Назад в меню", callback_data="back_to_main")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def get_design_menu():
    buttons = [
        [InlineKeyboardButton(text="🛒 Заказать Дизайн/Баннеры на FunPay", url="https://funpay.com/lots/offer?id=69625512")],
        [InlineKeyboardButton(text="⬅️ Назад в меню", callback_data="back_to_main")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def get_profile_menu():
    buttons = [
        [InlineKeyboardButton(text="🔗 Перейти в профиль автора", url="https://funpay.com/users/14410614/")],
        [InlineKeyboardButton(text="⬅️ Назад в меню", callback_data="back_to_main")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

async def send_photo_safely(chat_id: int, photo_path: str, caption: str, reply_markup: InlineKeyboardMarkup):
    if os.path.exists(photo_path):
        photo = FSInputFile(photo_path)
        return await bot.send_photo(chat_id=chat_id, photo=photo, caption=caption, reply_markup=reply_markup, parse_mode="HTML")
    else:
        error_text = caption + f"\n\n⚠️ {html.italic(f'(Файл {photo_path} не найден)')}"
        return await bot.send_message(chat_id=chat_id, text=error_text, reply_markup=reply_markup, parse_mode="HTML")

@dp.message(CommandStart())
async def cmd_start(message: Message):
    text = (
        f"👋 Добро пожаловать в {html.bold('Astrix Store')}!\n\n"
        f"⚡️ Здесь ты найдешь топовые цифровые услуги, скрипты и уникальную графику.\n"
        f"👇 Выбирай интересующую категорию в меню ниже:"
    )
    await send_photo_safely(message.chat.id, BANNER_MAIN, text, get_main_menu())

@dp.callback_query(F.data == "back_to_main")
async def process_back(callback: CallbackQuery):
    text = (
        f"👋 Добро пожаловать в {html.bold('Astrix Store')}!\n\n"
        f"⚡️ Здесь ты найдешь топовые цифровые услуги, скрипты и уникальную графику.\n"
        f"👇 Выбирай интересующую категорию в меню ниже:"
    )
    await callback.message.delete()
    await send_photo_safely(callback.message.chat.id, BANNER_MAIN, text, get_main_menu())
    await callback.answer()

@dp.callback_query(F.data == "open_models")
async def process_models(callback: CallbackQuery):
    text = (
        f"⚔️ {html.bold('Каталог уникальных 3D Моделей (BlockBench)')}\n\n"
        f"🔥 Изготавливаю качественные кастомные модели оружия, брони, предметов и мобов для вашего сервера Minecraft!\n\n"
        f"⚡️ Гарантия качества, чистый UV-маппинг и сочный визуал.\n"
        f"👇 Нажми на кнопку ниже, чтобы перейти к оформлению заказа:"
    )
    await callback.message.delete()
    await send_photo_safely(callback.message.chat.id, BANNER_MODEL, text, get_models_menu())
    await callback.answer()

@dp.callback_query(F.data == "open_usernames")
async def process_usernames(callback: CallbackQuery):
    text = (
        f"🆔 {html.bold('Каталог премиум Юзернеймов (Short & Clean)')}\n\n"
        f"⚡️ В наличии крутые 4-5 значные тег-имена для Telegram каналов и чатов.\n"
        f"💎 Полная чистота, трастовые ID и отличная отлёжка под любые ваши проекты.\n\n"
        f"👇 Выбирай и забирай свой статус прямо сейчас:"
    )
    await callback.message.delete()
    await send_photo_safely(callback.message.chat.id, BANNER_USERNAME, text, get_usernames_menu())
    await callback.answer()

@dp.callback_query(F.data == "open_design")
async def process_design(callback: CallbackQuery):
    text = (
        f"🎨 {html.bold('Услуги цифрового дизайна (Astrix Design Studio)')}\n\n"
        f"💻 Создание стильных веб-сайтов и лендингов под ключ.\n"
        f"📈 Продающая инфографика, аватарки, превью и оформление лотов.\n\n"
        f"⚡️ Сделай свой проект дорогим и узнаваемым!\n"
        f"👇 Переходи по кнопке ниже для связи и заказа:"
    )
    await callback.message.delete()
    await send_photo_safely(callback.message.chat.id, BANNER_INFO, text, get_design_menu())
    await callback.answer()

@dp.callback_query(F.data == "open_profile")
async def process_profile(callback: CallbackQuery):
    profile_text = (
        f"👤 {html.bold('ВАШ КОММЕРЧЕСКИЙ ПРОФИЛЬ')}\n\n"
        f"🆔 Ваш ID: {html.code(callback.from_user.id)}\n"
        f"👤 Ник: @{callback.from_user.username if callback.from_user.username else 'Не установлен'}\n"
        f"💰 Игровой баланс: {html.bold('0₽ (в разработке)')}\n\n"
        f"🚀 {html.italic('Спасибо, что выбираете качество от Astrix Store!')}\n\n"
        f"🤫 {html.italic('Создам тебе любой бот в телеге пиши @rouap')}"
    )
    await callback.message.delete()
    await bot.send_message(chat_id=callback.message.chat.id, text=profile_text, reply_markup=get_profile_menu(), parse_mode="HTML")
    await callback.answer()

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    print("=== Bot Started ===")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())