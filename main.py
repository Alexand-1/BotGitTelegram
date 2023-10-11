import telebot
from telebot import types

bot = telebot.TeleBot('YOUR TOKEN')


questions = {
    "Что делает наша компания?": (["a) Разработка продуктов", "b) Продажа продуктов", "c) Обучение сотрудников", "d) Сфера технологий"], "d"),
    "Что является основой успеха проекта?": (["a) Инновации", "b) Команда", "c) Финансы", "d) Маркетинг"], "b"),
    "Как начинается адаптация новых сотрудников?": (["a) Обучение процессам", "b) Знакомство с культурой компании", "c) Проведение тестов", "d) Митинги"], "b"),
    "Что является важной частью программы адаптации?": (["a) Менторская поддержка", "b) Обучение продуктам", "c) Работа в команде", "d) Участие в проектах"], "a"),
    "Какая атмосфера царит в нашей компании?": (["a) Открытая и дружелюбная", "b) Строгая и формальная", "c) Профессиональная", "d) Спокойная и расслабленная"], "a"),
    "Что делает успешную адаптацию новых сотрудников?": (["a) Участие в проектах", "b) Индивидуальный подход", "c) Активное участие в оценках", "d) Профессиональный опыт"], "c"),
    "Какие результаты достигаются в результате адаптации?": (["a) Лучшее понимание бизнеса", "b) Индивидуальный рост", "c) Интеграция в команду", "d) Достижение общих целей"], "d")
}
user_answers = {}
current_question = 0


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    item_info = types.KeyboardButton('Информация')
    item_test = types.KeyboardButton('Тест по тексту')
    item_video = types.KeyboardButton('Видеофрагмент')
    item_adress = types.KeyboardButton('Местонахождение')
    markup.add(item_adress, item_video, item_test, item_info)

    Usname = f'<b>Привет {message.from_user.first_name}! Я помогаю новым сотрудникам в обучении и знакомлю их с компанией. Выбери интересующий тебя раздел</b>'
    bot.send_message(message.chat.id, Usname, parse_mode='html', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Видеофрагмент')
def video(message):
    markup = types.InlineKeyboardMarkup()
    video_button = types.InlineKeyboardButton('Переход',url='https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    markup.add(video_button)
    bot.send_message(message.chat.id, 'Привет, вот небольшой видеофрагмент, который поможет погрузиться в атмосферу нашей команды',reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Местонахождение')
def location(message):
    loc_text =  """
    Мы крупная компания с многочисленными отделениями по всему миру.
    У нас более 100 отделений по всему миру. 
    Наши офисы расположены в различных крупных городах, таких как:
    - Москва
    - Санкт-Петербург
    - Новосибирск
    - Екатеринбург
    - Киев
    - Минск
    """
    bot.send_message(message.chat.id,loc_text)


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
    global current_question
    current_question = 0
    user_answers[message.chat.id] = {}
    ask_question(message.chat.id)


def ask_question(chat_id):
    global current_question
    question = list(questions.keys())[current_question]
    options = questions[question][0]


    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    for i, option in enumerate(options):
        markup.add(f"{chr(97 + i)}) {option}")

    bot.send_message(chat_id, f"Вопрос {current_question + 1}: {question}", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text.startswith(('a)', 'b)', 'c)', 'd)')))
def handle_answer(message):
    global current_question
    chat_id = message.chat.id
    user_answer = message.text[0].lower()

    question = list(questions.keys())[current_question]
    correct_answer = questions[question][1]

    user_answers[chat_id][current_question] = {
        'user_answer': user_answer,
        'correct_answer': correct_answer
    }

    current_question += 1

    if current_question < len(questions):
        ask_question(chat_id)
    else:
        calculate_score(chat_id)


def calculate_score(chat_id):
    correct_answers = sum(1 for q, a in user_answers[chat_id].items() if a['user_answer'] == a['correct_answer'])
    total_questions = len(questions)

    result_message = f"Вы ответили правильно на {correct_answers} из {total_questions} вопросов."
    bot.send_message(chat_id, result_message)


    for question_number, answers in user_answers[chat_id].items():
        question = list(questions.keys())[question_number]
        user_answer = answers['user_answer']
        correct_answer = answers['correct_answer']
        result = "Правильно" if user_answer == correct_answer else f"Неправильно, правильный ответ: {correct_answer}"

        bot.send_message(chat_id, f"Вопрос {question_number + 1}: {question}\nВаш ответ: {user_answer}\nРезультат: {result}")


    send_menu(chat_id)

def send_menu(chat_id):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    item_info = types.KeyboardButton('Информация')
    item_test = types.KeyboardButton('Тест по тексту')
    item_video = types.KeyboardButton('Видеофрагмент')
    item_adress = types.KeyboardButton('Местонахождение')
    markup.add(item_adress, item_video, item_test, item_info)


    Usname = f'<b>Привет! Вы вернулись в меню</b>'
    bot.send_message(chat_id, Usname, parse_mode='html', reply_markup=markup)

bot.polling(none_stop=True)
