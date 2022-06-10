import telebot
from telebot import types
import sqlite3
import time
import keyboard

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
bot = telebot.TeleBot("5148308795:AAG-GZqSFqs7H3947e5PvkADS7PIWM8chKE")

conn = sqlite3.connect('C:/Users/Liza/PycharmProjects/1/sql/baza.db',check_same_thread=False )
cursor = conn.cursor()

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text="Ученик")
    btn2 = types.KeyboardButton(text="Учитель")
    markup.add(btn1, btn2)
    people_id = message.chat.id
    cursor.execute(f'SELECT user_id FROM users WHERE user_id = {people_id}')
    data = cursor.fetchone()
    if data is None:
        user_id  = [message.chat.id, message.from_user.first_name,message.from_user.last_name]
        cursor.execute('INSERT INTO users VALUES (?,?,?,0);',user_id)
        conn.commit()
        bot.send_message(message.chat.id, 'Спасибо за регистрацию',reply_markup=markup)
        bot.send_message(message.chat.id, 'Вы ученик или учитель?', reply_markup=markup)
    else:
        bot.send_message(message.chat.id,"Вы уже зарегистировались",reply_markup=markup)



@bot.message_handler(func= lambda m: m.text =="Учитель")
def teacher(message):
    markup2 = types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
    people_id = message.chat.id
    cursor.execute(f'SELECT user_id FROM users WHERE user_id = {people_id}')
    user_id = cursor.fetchone()
    if user_id is None:
        bot.send_message(message.chat.id, 'Вы незарегестррованный пользователь',reply_markup=markup2)
        bot.send_message(message.chat.id, 'Для регистрации отравьте команду /start',reply_markup=markup2)
    else:
        msg = bot.send_message(message.chat.id, 'Введите логин', reply_markup=markup2)
        bot.register_next_step_handler(msg, teacher2)

def teacher2(message):
    message_to_save = message.text
    if message_to_save == "123456789" :
        markup2 = types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
        people_id = message.chat.id
        cursor.execute((f'UPDATE users SET status = 1 WHERE user_id = {people_id}'))
        conn.commit()
        bot.send_message(message.chat.id, 'Добро пожаловать, учитель!', reply_markup=markup2)
        bot.send_message(message.chat.id, 'Для продолжения напиши "Начать"', reply_markup=markup)
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    else:
        bot.send_message(message.chat.id, 'Логин неверный. Повторите запрос снова', reply_markup=markup)

@bot.message_handler(func= lambda m: m.text =="Ученик")
def student(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    people_id = message.chat.id
    cursor.execute(f'SELECT user_id FROM users WHERE user_id = {people_id}')
    user_id = cursor.fetchone()
    if user_id is None:
        bot.send_message(message.chat.id, 'Вы незарегестррованный пользователь',reply_markup=markup)
        bot.send_message(message.chat.id, 'Для регистрации отравьте команду /start',reply_markup=markup)
    else:
        people_id = message.chat.id
        cursor.execute((f'UPDATE users SET status = 0 WHERE user_id = {people_id}'))
        conn.commit()
        bot.send_message(message.chat.id, 'Привет, ученик!', reply_markup=markup)
        bot.send_message(message.chat.id, 'Для продолжения напиши "Начать"', reply_markup=markup)

@bot.message_handler(func= lambda m: m.text =="Начать")
def raspisanie(message):
    startKBoard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn1 = types.KeyboardButton(text="Расписание уроков")
    btn2 = types.KeyboardButton(text="Расписание звонков")
    btn3 = types.KeyboardButton(text="Календарь")
    people_id = message.chat.id
    cursor.execute(f'SELECT status FROM users WHERE user_id = {people_id}')
    status = cursor.fetchone()
    if status[0] == 1:
        btn4 = types.KeyboardButton(text="Библиотека")
    else:
        btn4 = types.KeyboardButton(text="Котик")
    startKBoard.add(btn1, btn2, btn3,btn4)
    bot.send_message(message.chat.id, "Привет. Меня зовут Буки.", reply_markup=startKBoard)
    bot.send_message(message.chat.id, "Я школьный бот-ассистент", reply_markup=startKBoard)
    bot.send_message(message.chat.id, "Чем я могу помочь?", reply_markup=startKBoard)



@bot.message_handler(func= lambda m: m.text =="Расписание уроков")
def uroku(message):
    startKBoard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn1 = types.KeyboardButton(text="Понедельник",)
    btn2 = types.KeyboardButton(text="Вторник")
    btn3 = types.KeyboardButton(text="Среда")
    btn4 = types.KeyboardButton(text="Четверг")
    btn5 = types.KeyboardButton(text="Пятница")
    btn6 = types.KeyboardButton(text="Назад к меню")
    startKBoard.add(btn1,btn2,btn3,btn4,btn5,btn6)
    bot.send_message(message.chat.id, "На какой день?", reply_markup=startKBoard)

@bot.message_handler(func= lambda m: m.text =="Понедельник")
def raspisanie1(message):
    photo = open("C:/Users/Liza/PycharmProjects/1/расписание/понедельник.jpg", 'rb')
    bot.send_photo(message.chat.id, photo)

@bot.message_handler(func=lambda m: m.text == "Вторник")
def raspisanie2(message):
    photo = open("C:/Users/Liza/PycharmProjects/1/расписание/вторник.jpg", 'rb')
    bot.send_photo(message.chat.id, photo)

@bot.message_handler(func=lambda m: m.text == "Среда")
def raspisanie1(message):
    photo = open('C:/Users/user/PycharmProjects/baza/расписание/среда.jpg','rb')
    bot.send_photo(message.chat.id, photo)

@bot.message_handler(func=lambda m: m.text == "Четверг")
def raspisanie1(message):
    photo = open('C:/Users/Liza/PycharmProjects/1/расписание/четверг.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)

@bot.message_handler(func=lambda m: m.text == "Пятница")
def raspisanie1(message):
    photo = open("C:/Users/Liza/PycharmProjects/1/расписание/пятница.jpg", 'rb')
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(func= lambda m: m.text =="Расписание звонков")
def times(message):
    startKBoard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn1 = types.KeyboardButton(text="Назад к меню")
    startKBoard.add(btn1)
    bot.send_message(message.chat.id, "С радостью покажу. Вот:", reply_markup=startKBoard)
    photo = open("C:/Users/Liza/PycharmProjects/1/расписание/звонки.jpg", 'rb')
    bot.send_photo(message.chat.id, photo)

@bot.message_handler(func= lambda m: m.text =="Назад к меню")
def exit(message):
    startKBoard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn1 = types.KeyboardButton(text="Расписание уроков")
    btn2 = types.KeyboardButton(text="Расписание звонков")
    btn3 = types.KeyboardButton(text="Календарь")
    people_id = message.chat.id
    cursor.execute(f'SELECT status FROM users WHERE user_id = {people_id}')
    status = cursor.fetchone()
    if status[0] == 1:
        btn4 = types.KeyboardButton(text="Библиотека")
    else:
        btn4 = types.KeyboardButton(text="Котик")
    startKBoard.add(btn1, btn2, btn3,btn4)
    bot.send_message(message.chat.id, "Чем могу помочь?", reply_markup=startKBoard)

@bot.message_handler(func= lambda m: m.text =="Библиотека")
def lib(message):
    bot.send_message(message.chat.id, "Какой жанр предпочитаете?", reply_markup=markup)
    bot.send_message(message.chat.id, "Романтика, Ужасы, Детектив", reply_markup=markup)


@bot.message_handler(func= lambda m: m.text =="Романтика")
def romantic(message):
    startKBoard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    bot.send_message(message.chat.id, 'Николас Спаркс "Дневник памяти",  Джейн Остин (Остен) "Гордость и предубеждение",'
                                      'Гарсиа Маркес "Любовь во время чумы"  ,Джоджо Мойес "До встречи с тобой"  ,'
                                      'Эмили Бронте "Грозовой перевал"', reply_markup=startKBoard)

@bot.message_handler(func= lambda m: m.text =="Детектив")
def det(message):
    startKBoard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    bot.send_message(message.chat.id,'Стиг Ларссон «Девушка с татуировкой дракона» (трилогия «Миллениум), '
                                     ' Ю Несбе «Красношейка» (серия детективов про Харри Холе), '
                                     ' Александра Маринина «Отдаленные последствия» (серия детективов про Анастасию Каменскую),  '
                                     ' Роберт Гэлбрейт «Дурная кровь» (серия детективов про Корморана Страйка)',
                                     reply_markup=startKBoard)

@bot.message_handler(func= lambda m: m.text =="Ужасы")
def yyyy(message):
    startKBoard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    bot.send_message(message.chat.id,"Говард Филлипс Лавкрафт: «Хребты безумия»,  «Зов Ктулху»,  «Тень над Иннсмутом»,"
                                     " «Шепчущий во тьме»,' Стивен Кинг: «Кладбище домашних животных», «Оно»,"
                                     " «Безнадега», «Мизери»','Клайв Баркер: «Восставший из ада»,"
                                     "'Дин Кунц: «Звереныш»','Айра Левин: «Ребенок Розмари»','Кодзи Судзуки: «Звонок»",
                                    reply_markup=startKBoard)

@bot.message_handler(func= lambda m: m.text =="Котик")
def kot(message):
    photo = open("C:/Users/Liza/PycharmProjects/1/расписание/кот.jpg", 'rb')
    bot.send_photo(message.chat.id, photo)

@bot.message_handler(func= lambda m: m.text =="Календарь")
def kalendar(message):
    murkap3 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn01= types.KeyboardButton(text="Сегодня")
    btn02= types.KeyboardButton(text="Мои планы")
    btn03 = types.KeyboardButton(text="Праздники")
    btn04 = types.KeyboardButton(text="Назад к меню")
    murkap3.add(btn01,btn02,btn03,btn04)
    bot.send_message(message.chat.id, "О чём бы вы хотели узнать?", reply_markup=murkap3)
    murkap3 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

@bot.message_handler(func=lambda m: m.text=="Сегодня")
def today(message):
    murkap3 = types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
    bot.send_message(message.chat.id,"Сегодня:",reply_markup=murkap3)
    today = time.ctime()
    bot.send_message(message.chat.id, today, reply_markup=murkap3)

@bot.message_handler(func=lambda m: m.text=="Мои планы")
def myplans(message):
    murkap4=types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
    btn1 = types.KeyboardButton(text="Проверить")
    btn2 = types.KeyboardButton(text="Создать")
    btn3 = types.KeyboardButton(text ="Назад к календарю")
    murkap4.add(btn1, btn2,btn3)
    bot.send_message(message.chat.id, "Внимание. Это демо версия данного раздела...", reply_markup=murkap4)
    bot.send_message(message.chat.id,"Что именно вас интересует?",reply_markup=murkap4)

@bot.message_handler(func=lambda m: m.text=="Назад к календарю")
def back_to_kalendar(message):
    murkap3 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn01 = types.KeyboardButton(text="Сегодня")
    btn02 = types.KeyboardButton(text="Мои планы")
    btn03 = types.KeyboardButton(text="Праздники")
    btn04 = types.KeyboardButton(text="Назад к меню")
    murkap3.add(btn01, btn02, btn03, btn04)
    bot.send_message(message.chat.id, "О чём бы вы хотели узнать?", reply_markup=murkap3)
    murkap3 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)


@bot.message_handler(func=lambda m: m.text=="Проверить")
def checkplan(message):
    murkap4 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    mounth = time.localtime().tm_mon
    day = time.localtime().tm_mday
    msg = bot.send_message(message.chat.id,"Ваши планы нас ледующие 5 дней:",reply_markup=murkap4)
    bot.send_message(message.chat.id,(keyboard.planss[mounth])[day] , reply_markup=murkap4)
    bot.send_message(message.chat.id, (keyboard.planss[mounth])[day + 1], reply_markup=murkap4)
    bot.send_message(message.chat.id, (keyboard.planss[mounth])[day + 2], reply_markup=murkap4)
    bot.send_message(message.chat.id, (keyboard.planss[mounth])[day + 3], reply_markup=murkap4)
    bot.send_message(message.chat.id, (keyboard.planss[mounth])[day + 3], reply_markup=murkap4)


@bot.message_handler(func=lambda m: m.text=="Создать")
def createplan(message):
    murkap4 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    msg = bot.send_message(message.chat.id,"Напишите описание события:",reply_markup=murkap4)
    bot.register_next_step_handler(msg,create2)

def create2(message):
    keyboard.creatt["plan"] = message.text
    murkap4 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    msg = bot.send_message(message.chat.id,"На какое число?",reply_markup=murkap4)
    bot.register_next_step_handler(msg,create3)

def create3(message):
    keyboard.creatt["число"]=message.text
    murkap4 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    mounth = time.localtime().tm_mon
    if int(keyboard.creatt["число"]) > 32:
        murkap4 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        bot.send_message(message.chat.id, "Такого числа нет", reply_markup=murkap4)
    else:
        for i in range(0,32,1):
            if int(keyboard.creatt["число"])== i:
                    keyboard.planss[mounth][i]=  keyboard.creatt["plan"]
                    bot.send_message(message.chat.id, "План успешно создан", reply_markup=murkap4)

@bot.message_handler(func=lambda m: m.text=="Праздники")
def celebrate(message):
    murkap4 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    for i in range(1,6,1):
        bot.send_message(message.chat.id, str(i) + " Июня "+  " празднуют:", reply_markup=murkap4)
        bot.send_message(message.chat.id,keyboard.celebrate[i],reply_markup=murkap4)





bot.polling(none_stop=False)
