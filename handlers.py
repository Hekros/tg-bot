from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards import start_kb
from db import add_application, get_all_applications
from config import ADMIN_ID

router = Router()

class Form(StatesGroup):
    name = State()
    phone = State()
    email = State()
    comment = State()

def register_handlers(dp):
    dp.include_router(router)

@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    await message.answer("Приветствую! Давайте начнём анкету. Назовите ваше имя.", reply_markup=start_kb())
    await state.set_state(Form.name)

@router.message(StateFilter(Form.name))
async def form_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите ваш номер телефона:")
    await state.set_state(Form.phone)

@router.message(StateFilter(Form.phone))
async def form_phone(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await message.answer("Введите вашу почту:")
    await state.set_state(Form.email)

@router.message(StateFilter(Form.email))
async def form_email(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    await message.answer("Добавьте комментарий:")
    await state.set_state(Form.comment)

@router.message(StateFilter(Form.comment))
async def form_comment(message: Message, state: FSMContext):
    data = await state.get_data()
    name = data["name"]
    phone = data["phone"]
    email = data["email"]
    comment = message.text

    await add_application(name, phone, email, comment)

    text = (
        f"<b>Новая заявка!</b>\n\n"
        f"<b>Имя:</b> {name}\n"
        f"<b>Телефон:</b> {phone}\n"
        f"<b>Email:</b> {email}\n"
        f"<b>Комментарий:</b> {comment}"
    )

    await message.answer("Спасибо! Ваша заявка отправлена.")
    await message.bot.send_message(ADMIN_ID, text)

    await state.clear()

@router.message(Command("showall"))
async def show_all_applications(message: Message):
    if message.from_user.id != ADMIN_ID:
        await message.answer("У вас нет доступа.")
        return

    rows = await get_all_applications()
    if not rows:
        await message.answer("Заявок пока нет.")
        return

    text = "\n\n".join([
        f"🧾 <b>ID:</b> {r[0]}\n<b>Имя:</b> {r[1]}\n<b>Телефон:</b> {r[2]}\n<b>Email:</b> {r[3]}\n<b>Комментарий:</b> {r[4]}"
        for r in rows
    ])

    await message.answer(text)
