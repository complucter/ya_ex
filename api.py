# coding: utf-8
# Импортирует поддержку UTF-8.
from __future__ import unicode_literals

# Импортируем модули для работы с JSON и логами.
import json
import logging

# Импортируем подмодули Flask для запуска веб-сервиса.
from flask import Flask, request

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

# Хранилище данных о сессиях.
sessionStorage = {}


# Задаем параметры приложения Flask.
@app.route("/", methods=['POST'])
def main():
    # Функция получает тело запроса и возвращает ответ.
    logging.info('Request: %r', request.json)

    response = {
        "version": request.json['version'],
        "session": request.json['session'],
        "response": {
            "end_session": False
        }
    }

    handle_dialog(request.json, response)

    logging.info('Response: %r', response)

    return json.dumps(
        response,
        ensure_ascii=False,
        indent=2
    )

def handle_dialog(req, res):
    user_id = req['session']['user_id']

        res['response'][
            'text'] = 'Привет! Я подскажу тебе, какие оценки ты должен получить для' \
                      ' достижения желаемого среднего балла. Сначала скажи средний' \


        res['response']['buttons'] = get_suggests(user_id)
        return

    if req['request']['original_utterance'].lower() in [
        'помощь',
        'что ты умеешь',
        'что ты умеешь?',
        'помоги',
    ]:
        res['response']['text'] = 'Я подскажу какие оценки тебе нужно получить, чтобы достичь ' \
                                  'желаемого балла. Просто введи сначала ' \
                                  'балл, который хочешь получить, а потом свои текущие оценки. ' \

        return


    if 'зарадка' in req['request']['original_utterance'].lower() :
        res['response']['text'] = 'Сделайте пять отшиманий и 5 приседаний'
        return

    if req['request']['original_utterance'].lower() == 'сайт':
        res['response']['text'] = 'Можете перейти по ссылке: mionitsa.pythonanywhere.com/marks_calculator'
        return

    if req['request']['original_utterance'].lower() == 'привет':
        res['response']['text'] = 'Привет, друг!'
        return

    if req['request']['original_utterance'].lower() == 'пока':
        res['response']['text'] = 'Миша пока('
        return
