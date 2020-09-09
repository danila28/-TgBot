import asyncio
import config
import logging
from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton, ChatActions, ParseMode
import aiogram.utils.markdown as md
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor

logging.basicConfig(format=u'%(filename)s [ LINE:%(lineno)+3s ]#%(levelname)+8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)

bot = Bot(token=config.TOKEN)
base_url = config.BASE_URL
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

SOHO = 'AgACAgIAAxkBAAEFxk1fPXHvhAt9D14IrAS1HLCcYR4hmQACErAxG1aA6EllJDonIGgcqdteC5cuAAMBAAMCAAN5AAM_OgACGwQ'
DRINK = 'AgACAgIAAxkBAAEFxk1fPXHvhAt9D14IrAS1HLCcYR4hmQACErAxG1aA6EllJDonIGgcqdteC5cuAAMBAAMCAAN5AAM_OgACGwQ'
TEA = 'AgACAgIAAxkBAAEFxk1fPXHvhAt9D14IrAS1HLCcYR4hmQACErAxG1aA6EllJDonIGgcqdteC5cuAAMBAAMCAAN5AAM_OgACGwQ'
FOOD = 'AgACAgIAAxkBAAEFxk1fPXHvhAt9D14IrAS1HLCcYR4hmQACErAxG1aA6EllJDonIGgcqdteC5cuAAMBAAMCAAN5AAM_OgACGwQ'
VIDEO_STOCKS = 'BAACAgIAAxkBAAEFxjJfPWcAAXNMPn35cwlm4oNGL4bluoYAAn4MAAJn_vBJG9n8U7HsiocbBA'


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_hi = KeyboardButton('Привет! 👋')
    greet_kb.add(button_hi)
    await bot.send_message(message.chat.id,
                           text=md.bold(
                               f"Привет {message.from_user.first_name}, я демонстративный бот, который покажет, на что он способен😉\n"
                               "Пример оформлен под кальянную"), reply_markup=greet_kb, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(commands=['about'])
async def send_about(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    itembtn4 = KeyboardButton('🌐Главное меню🌐')
    markup.add(itembtn4)
    await bot.send_message(
        message.chat.id,
        text=md.bold("Что может этот бот:\n1⃣Этот бот может рассказывать о вашем заведении, сайте или странице\n"
                     "2⃣Помогать клиенту определиться с выбором без какого любо участия владельца\n"
                     "3⃣Дать возможность клиенту оставить заявку на ту или иную услгу✏."),
        reply_markup=markup, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(commands=['menu'])
async def process_menu_command(message: types.Message):
    greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button_soho = KeyboardButton('/Кальяны💨')
    button_drink = KeyboardButton('/Напитки🍹')
    button_tea = KeyboardButton('/Чаи☕')
    button_food = KeyboardButton('/Закуски🍤')
    button_menu = KeyboardButton('🌐Главное меню🌐')
    greet_kb.add(button_soho, button_drink, button_tea, button_food, button_menu)
    await bot.send_message(message.chat.id, text=md.bold("Выбери что хочешь посмотреть"), reply_markup=greet_kb,
                           parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(commands=['Кальяны💨'])
async def process_soho(message: types.Message):
    user_id = message.from_user.id
    await bot.send_chat_action(user_id, ChatActions.UPLOAD_PHOTO)
    await asyncio.sleep(1)
    await bot.send_photo(message.from_user.id, SOHO,
                         reply_to_message_id=message.message_id)


@dp.message_handler(commands=['Напитки🍹'])
async def process_drink(message: types.Message):
    user_id = message.from_user.id
    await bot.send_chat_action(user_id, ChatActions.UPLOAD_PHOTO)
    await asyncio.sleep(1)
    await bot.send_photo(message.from_user.id, DRINK,
                         reply_to_message_id=message.message_id)


@dp.message_handler(commands=['Чаи☕'])
async def process_tea(message: types.Message):
    user_id = message.from_user.id
    await bot.send_chat_action(user_id, ChatActions.UPLOAD_PHOTO)
    await asyncio.sleep(1)
    await bot.send_photo(message.from_user.id, TEA,
                         reply_to_message_id=message.message_id)


@dp.message_handler(commands=['Закуски🍤'])
async def process_food(message: types.Message):
    user_id = message.from_user.id
    await bot.send_chat_action(user_id, ChatActions.UPLOAD_PHOTO)
    await asyncio.sleep(1)
    await bot.send_photo(message.from_user.id, FOOD,
                         reply_to_message_id=message.message_id)


@dp.message_handler(commands=['stocks'])
async def process_stocks(message: types.Message):
    user_id = message.from_user.id
    greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_menu = KeyboardButton('🌐Главное меню🌐')
    greet_kb.add(button_menu)
    await bot.send_message(message.chat.id, text=md.bold("Видео или фото вашей акции акции📹"), reply_markup=greet_kb,
                           parse_mode=ParseMode.MARKDOWN)
    await bot.send_chat_action(user_id, ChatActions.RECORD_VIDEO)
    await asyncio.sleep(0)  # конвертируем видео и отправляем его пользователю
    await bot.send_video(message.from_user.id, VIDEO_STOCKS)


@dp.message_handler(commands=['contact'])
async def process_contact(message: types.Message):
    keyboards = InlineKeyboardMarkup(row_width=2, one_time_keyboard=True)
    btn1 = InlineKeyboardButton(text='Вконтакте', url='https://vk.com/')
    btn2 = InlineKeyboardButton(text='Инстаграм', url='https://www.instagram.com/')
    keyboards.add(btn1, btn2)
    await bot.send_message(message.chat.id, md.italic('Как с нами связаться📲\n'
                                                      'Наш телефон: +7911888888📞\n'
                                                      'Наш адресс: ул.Достоевског, д.15, оф.48🏢'),
                           reply_markup=keyboards, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(commands=['comment'])
async def process_comment(message: types.Message):
    user_id = message.from_user.id
    greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_menu = KeyboardButton('🌐Главное меню🌐')
    greet_kb.add(button_menu)
    await bot.send_message(message.chat.id, text=md.bold("Видео или фото ваших отзывов📹"), reply_markup=greet_kb,
                           parse_mode=ParseMode.MARKDOWN)
    await bot.send_chat_action(user_id, ChatActions.RECORD_VIDEO)
    await asyncio.sleep(0)  # конвертируем видео и отправляем его пользователю
    await bot.send_video(message.from_user.id, VIDEO_STOCKS)


@dp.message_handler(commands=['help'])
async def process_help(message: types.Message):
    greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
    button_about = KeyboardButton('/about')
    button_menu = KeyboardButton('/menu')
    button_stocks = KeyboardButton('/stocks')
    button_reg = KeyboardButton('/reg')
    button_contact = KeyboardButton('/contact')
    button_comment = KeyboardButton('/comment')
    greet_kb.add(button_about, button_stocks, button_reg, button_menu, button_contact, button_comment)
    await bot.send_message(message.chat.id,
                           text=md.italic("Все довольно просто, нажимайте на команды, которые указаы ниже\n"
                                          "Для того чтобы посмотреть информацию о нас выбери команду /about\n"
                                          "Для того чтобы посмотреть наше меню выбери команду /menu\n"
                                          "Для того чтобы сделать заказ выбери команду /reg\n"
                                          "Для того чтобы посмотреть наши контакты  выбери команду /contact\n"
                                          "Для того чтобы посмотреть отзывы о нас ведери команду /comment\n"),
                           reply_markup=greet_kb, parse_mode=ParseMode.MARKDOWN)


#
# @dp.callback_query_handler(func=lambda call: True)
# async def keyboard_regulate3(call):
#    if call.data == 'CALLBACK_BAD':
#        keyboard1 = InlineKeyboardMarkup()
#        btn2 = InlineKeyboardButton(
#            text='lox',
#            callback_data='CALLBACK_BAD')
#        keyboard1.add(btn2)
#        await bot.edit_message_text(
#            chat_id=call.message.chat.id,
#            message_id=call.message.message_id,
#            text='palace',
#            reply_markup=keyboard1)
#    elif call.data == 'CALLBACK_AMAZING':
#        keyboard1 = InlineKeyboardMarkup()
#        btn2 = InlineKeyboardButton(text='Моя страница', url='https://vk.com/filimonov280101')
#        keyboard1.add(btn2)
#        await bot.edit_message_text(
#            chat_id=call.message.chat.id,
#            message_id=call.message.message_id,
#            text='lumia',
#            reply_markup=keyboard1)
#
#    elif call.data == 'CALLBACK_FORWARD':
#        keyboards = InlineKeyboardMarkup(row_width=2)
#        btn1 = InlineKeyboardButton(text='Моя страница', callback_data='CALLBACK_AMAZING')
#        btn2 = InlineKeyboardButton(text='Написать автору', callback_data='CALLBACK_BAD')
#        btn3 = InlineKeyboardButton(text='Меню', url='https://vk.com/filimonov280101')
#        keyboards.add(btn1, btn2, btn3)
#
#        await bot.edit_message_text(
#            chat_id=call.message.chat.id,
#            message_id=call.message.message_id,
#            text='menu',
#            reply_markup=keyboards)
#


class Form(StatesGroup):
    name = State()
    age = State()
    city = State()
    phone = State()
    service = State()
    strength = State()
    date = State()


@dp.message_handler(commands='reg')
async def cmd_start(message: types.Message):
    await Form.name.set()
    greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_cancel = ('/Отменить❌')
    greet_kb.add(button_cancel)
    await bot.send_message(message.chat.id, md.italic(
        "Если вы ознакомились с нашим меню, то для заполнения заявки нужно указать свои данные📝\n"
        "Чтобы мы могли с вами связаться, вводите пожалуйста точную информаци, спасибо😊\n"
        "Если вы ввели не те данные, нажмите Отменить❌\n"
        "1⃣Введите свои инициалы(ФИО)"), reply_markup=greet_kb,
                           parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(state='*', commands='Отменить❌')
@dp.message_handler(Text(equals='Отменить❌', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info('Cancelling state %r', current_state)
    await state.finish()
    greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_menu = KeyboardButton('🌐Главное меню🌐')
    greet_kb.add(button_menu)
    await bot.send_message(message.chat.id, text="Ваш заказ отменен, вернитесь в главное меню", reply_markup=greet_kb)


@dp.message_handler(state=Form.name)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

    await Form.next()
    greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_cancel = ('/Отменить❌')
    greet_kb.add(button_cancel)
    await bot.send_message(message.chat.id, md.italic(f"2⃣Отлично, {message.from_user.first_name}\n"
                                                      "Сколько тебе лет?🔞"), reply_markup=greet_kb,
                           parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(lambda message: not message.text.isdigit(), state=Form.age)
async def process_age_invalid(message: types.Message):
    return await bot.send_message(message.chat.id, "Возраст должен быть числом.\nСколько тебе лет?🔞 (только числа)")


@dp.message_handler(lambda message: message.text.isdigit(), state=Form.age)
async def process_age(message: types.Message, state: FSMContext):
    await Form.next()
    await state.update_data(age=int(message.text))

    await bot.send_message(message.chat.id, md.italic("3⃣Из какого вы города?🏭"), parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(state=Form.city)
async def process_city(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['city'] = message.text

    await Form.next()
    await bot.send_message(message.chat.id, md.italic("4⃣Введите свой номер телефона📱"), parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(lambda message: not message.text.isdigit(), state=Form.phone)
async def process_phone_invalid(message: types.Message):
    return await bot.send_message(message.chat.id, "Номер должен быть числом.\nВведите свой телефон📱(только числа)")


@dp.message_handler(lambda message: message.text.isdigit(), state=Form.phone)
async def process_phone(message: types.Message, state: FSMContext):
    await Form.next()
    await state.update_data(phone=int(message.text))

    await bot.send_message(message.chat.id, md.italic("5⃣Напишите, чтобы вы хотели заказть из меню📘"),
                           parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(state=Form.service)
async def process_service(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['service'] = message.text

    await Form.next()
    greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3, one_time_keyboard=True)
    button_soft = KeyboardButton('Мягкий')
    button_medium = KeyboardButton('Средний')
    button_hard = KeyboardButton('Жеский')
    button_cancel = KeyboardButton('/Отменить❌')
    greet_kb.add(button_soft, button_medium, button_hard, button_cancel)
    await bot.send_message(message.chat.id, text="6⃣Какой крепости кальян вы бы хотели?💨", reply_markup=greet_kb,
                           parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(state=Form.strength)
async def process_strength(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['strength'] = message.text

    await Form.next()
    greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
    button_cancel = ('/Отменить❌')
    button_not = ('Нет')
    greet_kb.add(button_cancel, button_not)
    await bot.send_message(message.chat.id, md.text(md.italic("7⃣Вы хотели бы забронировать стол?⌚\n"),
                                                    "Если да то напишите дату, например 14.06.20 в 14:00"),
                           reply_markup=greet_kb,
                           parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(state=Form.date)
async def process_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        chat_id = message.chat.id
        data['date'] = message.text
        markup = ReplyKeyboardRemove()
    await bot.send_message(chat_id, md.text(
        md.text('Ваша заявка:', md.bold(message.from_user.first_name)),
        md.text('Ваши инициалы:', md.bold(data['name'])),
        md.text('Возраст:', md.bold(data['age'])),
        md.text('Город:', md.bold(data['city'])),
        md.text('Ваш телефон', md.bold(data['phone'])),
        md.text('Ваш заказ:', md.bold(data['service'])),
        md.text('Крепость кальяна:', md.bold(data['strength'])),
        md.text('Дата:', md.bold(data['date'])),
        sep='\n',
    ),
                           reply_markup=markup,
                           parse_mode=ParseMode.MARKDOWN,

                           )
    await bot.send_message(config.chat_id, md.text(
        md.text('Заявка от:', md.bold(message.from_user.first_name)),
        md.text('Инициалы:', md.bold(data['name'])),
        md.text('Возраст:', md.bold(data['age'])),
        md.text('Город:', md.bold(data['city'])),
        md.text('Телефон:', md.bold(data['phone'])),
        md.text('Заказ клиента:', md.bold(data['service'])),
        md.text('Крепость кальяна:', md.bold(data['strength'])),
        md.text('Дата:', md.bold(data['date'])),
        sep='\n',
    ),
                           reply_markup=markup,
                           parse_mode=ParseMode.MARKDOWN,
                           )
    greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_menu = KeyboardButton('🌐Главное меню🌐')
    greet_kb.add(button_menu)
    await bot.send_message(message.chat.id,
                           text="Ваша заявка📝 уже пришла к нам, в ближайшее время мы с вами свяжемся😊",
                           reply_markup=greet_kb)
    await state.finish()


@dp.message_handler(content_types=["🌐Главное меню🌐"])
async def send_help(message: types.Message):
    await bot.send_message(message.chat.id, md.bold(
        'Нажимай на кнопки справа👇\nСтарт🚀 - /start\nО нас📖 - /about\nМеню📘 - /menu\nАкции‼ - /stocks\n'
        'Сделать заказ✏ - /reg\nНаши контакты📱 - /contact\nОтзывы👍 - /comment\nПомощь🚑 - /help'),
                           parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(content_types=["text"])
async def send_help(message: types.Message):
    await bot.send_message(message.chat.id, md.bold(
        'Нажимай на кнопки справа👇\nСтарт🚀 - /start\nО нас📖 - /about\nМеню📘 - /menu\nАкции‼ - /stocks\n'
        'Сделать заказ✏ - /reg\nНаши контакты📱 - /contact\nОтзывы👍 - /comment\nПомощь🚑 - /help'),
                           parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(content_types=["photo"])
def send_photo_text(message):
    bot.send_message(message.chat.id, 'Напишите текст, я не понимаю чего вы хотите по фото!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
