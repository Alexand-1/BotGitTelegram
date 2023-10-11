import telebot
from telebot import types


bot = telebot.TeleBot('YOUR TOKEN')
user_state = {}

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    item_info = types.KeyboardButton('Информация')
    item_test = types.KeyboardButton('Тест по тексту')
    item_video = types.KeyboardButton('Видеофрагмент')
    item_adress = types.KeyboardButton('Местонахождение')
    markup.add(item_adress,item_video,item_test,item_info)

    Usname = f'<b>Привет {message.from_user.first_name}! Я помогаю новым сотрудникам в обучении и знакомлю их с компанией.Выбери интересующий тебя раздел</b>'
    bot.send_message(message.chat.id,Usname,parse_mode='html',reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Видеофрагмент')
def video(message):
    markup = types.InlineKeyboardMarkup()
    video_button = types.InlineKeyboardButton('Переход',url='https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    markup.add(video_button)
    bot.send_message(message.chat.id, 'Привет, вот небольшой видеофрагмент, который поможет погрузиться в атмосферу нашей команды',reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Информация')
def info(message):
    mes = "Наша компания специализируется на разработке инновационных продуктов и решений в сфере технологий." \
          " Мы придаем большое значение адаптации новых сотрудников, с уверенностью в том, что команда — это основа успеха любого проекта." \
          " В нашей организации созданы специальные программы для эффективной адаптации новых сотрудников, которые помогают быстро войти в рабочий ритм и стать частью команды." \
          " Адаптация новых коллег у нас начинается с тщательного знакомства с корпоративной культурой и ценностями компании. Мы обеспечиваем индивидуальный подход к каждому сотруднику, помогая ему освоить основные процессы и задачи, а также предоставляем возможности для профессионального роста." \
          " Важной частью нашей программы адаптации является менторская поддержка, где опытные сотрудники готовы делиться своими знаниями и опытом. Мы создали дружественную и открытую атмосферу, где новички могут задавать вопросы, обсуждать идеи и с уверенностью взаимодействовать с коллегами. Компания осуществляет регулярные оценки адаптации сотрудников, что позволяет нам постоянно улучшать наши программы и методики." \
          " В результате успешной адаптации новые сотрудники быстро интегрируются в команду и принимают активное участие в достижении общих целей. Мы убеждены, что хорошо сплоченная и адаптированная к команде команда способна преодолевать любые профессиональные вызовы и достигать высоких результатов."
    bot.send_message(message.chat.id,mes)


@bot.message_handler(func=lambda message: message.text == 'Тест по тексту')
def test(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    item_start_test = types.KeyboardButton('Начать тест')
    item_go_back = types.KeyboardButton('Вернуться назад')
    markup.add(item_go_back,item_start_test)

    greeting_message = "Привет для прохождения теста! Тебе сначала нужно ознакомиться с информацией о компании. Что хочешь сделать?"
    bot.send_message(message.chat.id, greeting_message, reply_markup=markup)

    user_state[message.chat.id] = 'test'

@bot.message_handler(func=lambda message: message.text == 'Вернуться назад')
def go_back(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    item_info = types.KeyboardButton('Информация')
    item_test = types.KeyboardButton('Тест по тексту')
    item_video = types.KeyboardButton('Видеофрагмент')
    item_adress = types.KeyboardButton('Местонахождение')
    markup.add(item_adress, item_video, item_test, item_info)

    back_mes = 'Вы вернулись в меню'

    bot.send_message(message.chat.id,back_mes, reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Начать тест')
def start_test(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    item_start_test = types.KeyboardButton('Пройти')
    item_go_back = types.KeyboardButton('Отменить')
    markup.add(item_go_back, item_start_test)

    greeting_message = "Тест будет состоять из 7 легких вопросов по тексту.Готов?"
    bot.send_message(message.chat.id, greeting_message, reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Отменить')
def cansel(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    item_start_test = types.KeyboardButton('Начать тест')
    item_go_back = types.KeyboardButton('Вернуться назад')
    markup.add(item_go_back, item_start_test)

    greeting_message = "Привет для прохождения теста! Тебе сначала нужно ознакомиться с информацией о компании. Что хочешь сделать?"
    bot.send_message(message.chat.id, greeting_message, reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Пройти')
def go(message):
    pass



bot.polling(none_stop=True)
