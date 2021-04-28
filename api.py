# coding: utf-8
# Импортирует поддержку UTF-8.
from __future__ import unicode_literals

# Импортируем модули для работы с JSON и логами.
import json
import logging
import random
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
    hello = ['Здравствуйте, я могу посоветовать вам много различных упражнений. Спросите у меня что-нибудь про отжимания, приседания или пресс, например, как правильно делать отжимания.',
        'Здравствуйте, я могу рассказать вам много об упражнениях, которые вы можете делать, не выходя из дома. Например спросите меня как правильно делать приседания.',
        'Здравствуйте, я могу посоветовать вам тренировки, напрвленныен на различные цели. Например могу рассказать об упражнениях на выносливость.']
    error = ['Извините, не знаю как ответить на ваш вопрос .', 'Извините, не понимаю вас', 'Попробуйте переформулировать ваш вопрос, не понимаю вас.']

    help = ['Я могу посоветовать вам много различных упражнений. Спросите у меня что-нибудь про отжимания, приседания или пресс, например, как правильно делать отжимания.',
        'Я могу рассказать вам много об упражнениях, которые вы можете делать, не выходя из дома. Например спросите меня как правильно делать приседания.',
        'Я могу посоветовать вам тренировки, напрвленныен на различные цели. Например могу рассказать об упражнениях на выносливость.']

    user_id = req['session']['user_id']

    if req['session']['new']:
        res['response'][
            'text'] = random.choice(hello)
        return

    if 'зарядк' in req['request']['original_utterance'].lower():
        res['response']['text'] = 'Утренняя зарядка очень важна, выполняйте ее каждый день и будьте в тонусе. Для начала разомните шею и руки легкими вращениями. Далее переходите к корпусу.'\
        'После этого выполните упражнения на нижнюю часть тела. Вы можете подробно расспросить об упражнениях у меня.'
        return


    if 'прес' in req['request']['original_utterance'].lower():
        res['response']['text'] = 'Лягте на пол, вытянув прямые ноги. Расположите руки на полу по бокам для поддержки. Сокращая мышцы нижнего пресса, поднимайте ноги под прямым углом к полу. Выполняйте упражнение до легкого жжения в области пресса.'
        return

    if 'отжим' in req['request']['original_utterance'].lower():
        res['response']['text'] = 'Для начала постарайтесь сделать максимальное колличесвто отжиманий, которое вы можете, затем отбавьте от него 2 повторения. При ежедневном выполнении упражнений, можете прибавлять по одному отжиманию каждую неделю.'
        return

    if 'планк' in req['request']['original_utterance'].lower():
        res['response']['text'] = 'Примите упор лежа, затем согните руки в локтях и обопритесь на предплечья. Увеличивайте время выполнение этого упражнения с каждым днем, и вы сможете добиться результата.'
        return

    if 'берпи' in req['request']['original_utterance'].lower():
        res['response']['text'] = 'Поставьте стопы параллельно друг другу, не шире плеч. Выполните приседание.'\
        ' Поставьте ладони на пол, сделайте вдох. Выполните прыжок в планку на выдохе. Прижимая локти к корпусу, на вдох опускайтесь максимально к полу. На выдох отжимайтесь от пола. Затем подпрыгните к ладоням и выпрыгните с пола в исходное положение.'
        return

    if 'бёрпи' in req['request']['original_utterance'].lower():
        res['response']['text'] = 'Поставьте стопы параллельно друг другу, не шире плеч. Выполните приседание.'\
        ' Поставьте ладони на пол, сделайте вдох. Выполните прыжок в планку на выдохе. Прижимая локти к корпусу, на вдох опускайтесь максимально к полу. На выдох отжимайтесь от пола. Затем подпрыгните к ладоням и выпрыгните с пола в исходное положение.'
        return

    if 'выносл' in req['request']['original_utterance'].lower():
        res['response']['text'] = 'Для тренировки на вносливость отлично подойдут бёрпи. Поставьте стопы параллельно друг другу, не шире плеч. Выполните приседание.'\
        ' Поставьте ладони на пол, сделайте вдох. Выполните прыжок в планку на выдохе. Прижимая локти к корпусу, на вдох опускайтесь максимально к полу. На выдох отжимайтесь от пола. Затем подпрыгните к ладоням и выпрыгните с пола в исходное положение.'
        return

    if 'похуд' in req['request']['original_utterance'].lower():
        res['response']['text'] = 'Чтобы избавиться от лишнего веса, отлично подойдет планка. '\
        'Примите упор лежа, затем согните руки в локтях и обопритесь на предплечья. Увеличивайте время выполнение этого упражнения с каждым днем, и вы сможете добиться результата.'
        return

    if 'снижен' in req['request']['original_utterance'].lower():
        res['response']['text'] = 'Чтобы избавиться от лишнего веса, отлично подойдет планка. '\
        'Примите упор лежа, затем согните руки в локтях и обопритесь на предплечья. Увеличивайте время выполнение этого упражнения с каждым днем, и вы сможете добиться результата.'
        return


    if 'присед' in req['request']['original_utterance'].lower():
        res['response']['text'] = 'Рекомендуется начинать с двадцати приседаний'\
        'в день, затем увеличивать колличесвто повторений. Существует несколько'\
        'правил для более эффективного выполнения данного упражнения. Расставьте'\
        'ноги чуть шире ширины плеч. Носки немного врозь. Во время приседаний'\
        'расправьте плечи и отведите их назад.'
        return

    if req['request']['original_utterance'].lower() in [
        'помощь',
        'что ты умеешь',
        'что ты умеешь?',
        'помоги',
    ]:
        res['response']['text'] = random.choice(help)
    else:
        res['response']['text'] = random.choice(error)
