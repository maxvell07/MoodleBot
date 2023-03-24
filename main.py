from test import test
import telebot
from telebot import types

bot = telebot.TeleBot('6122227939:AAFN3ZQb4wON7fFGgj8AaCMUokXw6s7Gqmw')


test()
markup_inline = types.InlineKeyboardMarkup()
markup2 = types.InlineKeyboardMarkup()
item_yes = types.InlineKeyboardButton(text='Креативное мышление и генерация идей', callback_data='yes',
                                      resize_keyboard=True)
# item_no = types.InlineKeyboardButton(text='❌', callback_data='no')
item_inf = types.InlineKeyboardButton(text='Сроки курса', callback_data='ye1', resize_keyboard=True)
item_teach = types.InlineKeyboardButton(text='Контакты преподавателей', callback_data='ye2', resize_keyboard=True)
item_grade = types.InlineKeyboardButton(text='Зачет или экзамен?', callback_data='ye3', resize_keyboard=True)
item_crit = types.InlineKeyboardButton(text='Критерии оценки', callback_data='ye4', resize_keyboard=True)
item_raz = types.InlineKeyboardButton(text='Расписание', callback_data='ye5', resize_keyboard=True)
item_place = types.InlineKeyboardButton(text='Место проведения занятий', callback_data='ye6', resize_keyboard=True)
markup1 = types.InlineKeyboardMarkup()
markup_inline.add(item_yes)
markup2.add(item_inf, item_teach, item_grade, item_crit, item_raz, item_place, row_width=1)


@bot.message_handler(commands=['help'])
def get_info(message):
    bot.send_message(message.chat.id, "Список команд:\n"
                                      "/start - Выбрать курс\n"
                                      "/help - Информация о боте и всех командах")
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEINN1kGFcHEkgLUMLkO4JnqlLpqMgrcgACtCAAAtDDCUpblvSlWU6vCS8E")

@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == 'ye1':
        bot.send_message(call.message.chat.id, "Условная группа 10/1 - 15.02 - 24.05 \n"
                                               "Условная группа 10/2 - 08.02 - 17.05", reply_markup=markup2)
    elif call.data == 'yes':
        bot.send_message(call.message.chat.id, "Информация по курсу", reply_markup=markup2)
    elif call.data == 'ye2':
        bot.send_message(call.message.chat.id, "Преподаватель Носкова Ольга Павловна (ГИ) - noskova_op@spbstu.ru\n"
                                               "Куратор Андреева Антонина Андреевна (ГИ) - andreeva_aa@spbstu.ru",
                         reply_markup=markup2)
    elif call.data == 'ye3':
        bot.send_message(call.message.chat.id, "Будет зачет на летней сессии в июне", reply_markup=markup2)
    elif call.data == 'ye4':
        bot.send_message(call.message.chat.id,
                         "Зачет по курсу можно получить при условии:\n- прохождение тестов по темам\n"
                         "- разработка портфолио", reply_markup=markup2)
    elif call.data == 'ye5':
        bot.send_message(call.message.chat.id,
                         "Условная группа 10/1 - занятия по средам в 16.00 в ГЗ - 211:\n- 5.02.2023\n"
                         "- 15.03.2023\n- 29.03.2023\n- 12.04.2023\n- 26.04.2023\n- 10.05.2023\n- 24.05.2023\n"
                         "Условная группа 10/2 - занятия по средам в 16.00 в 9к - 333:\n- 08.02.2023\n"
                         "- 01.03.2023\n- 22.03.2023\n- 05.04.2023\n- 19.04.2023\n- 03.05.2023\n- 17.05.2023",
                         reply_markup=markup2)
    elif call.data == 'ye6':
        bot.send_message(call.message.chat.id, "Условная группа 10/1 - занятия по средам в 16.00 в ГЗ - 211\n"
                                               "Условная группа 10/2 - занятия по средам в 16.00 в 9к - 333",
                         reply_markup=markup2)
    elif call.data == 'm':
        bot.send_message(call.message.chat.id, '')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1= types.KeyboardButton('что-то')
    item2= types.KeyboardButton('где-то')
    item3= types.KeyboardButton('тут-та')
   # item4= types.KeyboardButton('кнопка')
    markup.add(item1,item2,item3)
    bot.send_message(message.chat.id, "Привет, {0.first_name}! Я бот.\nВы хотите узнать информацию по курсу?".format(message.from_user),
                     reply_markup=markup)


@bot.message_handler(content_types=["text", "photo", "sticker", "audio", "video", "document", "voice"])
def any(message):
    bot.send_message(message.chat.id, "Список команд:\n"
                                      "/start - Выбрать курс\n"
                                      "/help - Информация о боте и всех командах")


bot.polling(none_stop=True)
