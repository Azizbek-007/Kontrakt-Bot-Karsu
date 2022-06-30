from config import bot, dp
from aiogram.types import Message

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from keyboards.ReplyKeyboard import main_btn
from sql.func import rege_student, student_info

class step(StatesGroup):
    step1 = State()
    access_token = State()


@dp.message_handler(commands=['start'], state=step.access_token)
async def auth_user(msg: Message, state: FSMContext):
    pas = await state.get_data()
    data = student_info(pas['password'])[0]
    await msg.answer(f"Assalamu alaykum *{data}* xosh keldin'iz!", parse_mode ='Markdown', reply_markup=main_btn())

@dp.message_handler(commands=['start'], state='*')
async def hello(msg: Message):
    await msg.answer(f"Assalamu Alaykum!\nDizimnen o'tiw ushin student kodin kiritin'!\n```002-*********``` formatta jiberin'", parse_mode='Markdown')
    await step.step1.set()

@dp.message_handler(state=step.step1)
async def step1(msg: Message, state: FSMContext):
    try:
        data = rege_student(int(msg.text), msg.from_user.id)
        if data[0] != False:  
            await msg.answer(f"*{data[0][1]}* dizimnen o'ttin'iz", parse_mode='Markdown', reply_markup=main_btn())
            await state.finish()
            await step.access_token.set()
            await state.update_data(password=msg.text)
        else: await msg.answer("Kodin'iz qa'te qayta kiritin'")    
    except: await msg.answer("Kodin'iz qa'te qayta kiritin'")


@dp.message_handler(text = "🔄 To`lemler", state=step.access_token)
async def tolem (msg: Message, state: FSMContext):
    pas = await state.get_data()
    data = student_info(pas['password'])[0]
    await msg.answer(
    f"<b>{data[1]}</b>\n\n<i>Kontrakt summasi:</i> <code>{data[3]}</code> so'm\n\n<i>To'lendi:</i> <code>{data[4]}</code> so'm\n\n <i>Qarizdarliq:</i> <code>{data[5]}</code> so'm \n\n <i>Qaldiq</i>: <code>{data[2]}</code>",
    parse_mode='html')

@dp.message_handler(text = "⛔️ Shig'iw", state=step.access_token)
async def shigiw (msg: Message, state: FSMContext):
    await msg.answer(f"Assalamu Alaykum!\nDizimnen o'tiw ushin student kodin kiritin'!\n```002-*********``` formatta jiberin'", parse_mode='Markdown')
    await state.finish()
    await step.step1.set()

