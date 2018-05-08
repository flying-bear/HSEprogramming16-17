##    Написать программу-бота, с которой можно разговаривать: пользователь пишет ей реплику, а она отвечает предложением,
##    в котором все слова заменены на какие-то случайные другие слова той же части речи и с теми же грамматическими характеристиками.
##    Предложение-ответ должно быть согласованным. Например, на фразу "Мама мыла раму" программа может ответить "Девочка пела песню".
##    Для такой программы вам понадобится большой список русских слов: можно взять список словоформ с сайта НКРЯ - http://ruscorpora.ru/corpora-freq.html
##    Из этого списка вам нужен только список разных лемм разных частей речи, и затем нужно будет использовать функции parse и inflect.

import json
from pymorphy2 import MorphAnalyzer
morph = MorphAnalyzer()
dictionary = {}

def get_file_lines(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return lines


def write_text_in_file(filename, text):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)

    
def analyze(form):
    an = morph.parse(form)[0] ## Parse(word='любимая', tag=OpencorporaTag('ADJF,Subx,Qual femn,sing,nomn'), normal_form='любимый', 
                              ## score=0.666666, methods_stack=((<DictionaryAnalyzer>, 'любимая', 367, 7),))
    return an


def get_dictionary(lines):
    for line in lines:
        form = line.split()[-1].strip()
        analyzis = analyze(form)
        tag = str(analyzis.tag)
        normal = str(analyzis.normal_form)
        dictionary[form] = {'tag':tag, normal:'normal'}
    write_text_in_file('jsdict.json', json.dumps(dictionary, ensure_ascii = False))
               

def main():
    lines = get_file_lines('dict_example.txt')
    get_dictionary(lines)


if __name__ == '__main__':
    main()