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

    if req['session']['new']:
        res['response'][
            'text'] = 'Привет!'
        return

    if 'зарядк' in req['request']['original_utterance'].lower():
        res['response']['text'] = 'Я могу посоветовать вам много различных упражнений. Скажите какую группу мышц вы хотите тренировать?'
        return

    if 'отжим' in req['request']['original_utterance'].lower():
        res['response']['text'] = 'Для начала постарайтесь сделать максимальное колличесвто отжиманий, которое вы можете, затем отбавьте от него 2 повторения. При ежедневном выполнении упражнений, можете прибавлять по одному отжиманию каждую неделю.'
        return
