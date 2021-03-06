## 1. Главная страница. Должна содержать форму, в которую пользователь может ввести слово из русского лексикона, а после отправки на сервер это слово транслитерируется в написание в старой (дореволюционной) орфографии (подробности ниже).
## Кроме того, на главной странице должна показываться информация об актуальной погоде в Скопье (столица Македонии), поскольку славянская письменность была разработана на основе македонских диалектов. Погода должна "забираться" с какого-либо показывающего погоду ресурса с помощью urllib.request.
## Страница должна быть оформлена в фреймворке Bootstrap.
##
## 2. Страница, при заходе пользователя на которую с определённого вами новостного ресурса (lenta.ru, kommersant.ru, sports.ru и т.д.) с помощью urllib.request скачивается главная страница, все кириллические слова на ней транслитерируются в старую орфографию и показываются пользователю.
## Кроме того, на экран должна выводиться информация о том, какие 10 самых частотных слов присутствуют на странице в данный момент.
##
## 3. Страница-тест для проверки знания пользователя, какие слова в старой орфографии содержат в своём составе букву "ѣ". Тест должен предлагать не менее 10 вопросов, в каждом из которых пользователю нужно выбрать между двумя вариантами, например, "хлебъ" или "хлѣбъ". Словарь слов, содержащих ѣ, можно найти здесь: http://www.dorev.ru/ru-faq-yatroots.html

from flask import Flask
from flask import url_for, render_template, request, redirect

import json

from uuid import uuid4

app = Flask(__name__)



@app.route('/')
def index():
    ...
    return ...

@app.route('/', methods=['POST'])
def process_request():
    ...
    return ...

@app.route('/translit')
def translit_news():
    ...
    return ...

@app.route('/check')
def check():
    ...
    return ...
