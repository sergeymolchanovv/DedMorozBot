# import time
# import pygsheets
# import datetime


# global value_adult1
# value_adult1 = 'ы пидор'
# global value_adult2
# value_adult2 = 'ы пидор'
# global value_children1
# value_children1 = 'ы пидор'
# global value_children2
# value_children2 = 'ы пидор'


# def is_it_now():
#     now  = datetime.datetime.now().strftime("%Y-%m-%d")
#     needed_date = "2022-07-28"
#     pydate = datetime.datetime.strptime(needed_date, '%Y-%m-%d')
#     print(pydate)
#     if now == needed_date:
#         print("True")
#     else:
#         print("False")
#
#
# while True:
#     is_it_now()
#     time.sleep(10800)
#
# def get_values_from_google_sheets():
#     gc = pygsheets.authorize(service_file='./client_secret.json')
#     sh = gc.open('Сергей Молчанов')
#     wks = sh.worksheet('index', 4)
#     global value_adult1
#     value_adult1 = wks.get_value('A1')
#     global value_adult2
#     value_adult2 = wks.get_value('B1')
#     global value_children1
#     value_children1 = wks.get_value('A2')
#     global value_children2
#     value_children2 = wks.get_value('B2')
#
#
# get_values_from_google_sheets()

caption_adult = 'На корпоратив' + '\n'\
 + '\n' + '(в ресторан, кафе, в офис, в любое место, где проходит ваш праздник)' + '\n' \
 + '\n' + 'Время: 30 минут' \
 + '\n' + 'Сказочные герои, которых взрослые ждут с детства! '\
          'Громкие песни, зажигательные танцы, интересные интерактивы, яркий реквизит!'\
 + '\n' \
 + '\n' + '- Насыщенная интерактивная программа' \
 + '\n' + '- Музыкальное сопровождение' \
 + '\n' + '- Песни, танцы, загадки' \
 + '\n' + '- Красивые костюмы героев, как на фото!' \
 + '\n' + '- Стихи от взрослых ребят' \
 + '\n' + '- Вручение ваших подарков' + '\n' \
 + '\n' + f'До завтра стоимость от <b><u> 0 </u></b> <s> 0 </s> руб.'

caption_child1 = 'Экспресс-поздравление.' + '\n'\
 + '\n' + \
 '15-минутная игровая программа с Дедом Морозом и Снегурочкой' + '\n' \
 + '\n' + '- 2 игры с интересным реквизитом и без него' \
 + '\n' + '- Музыкальное сопровождение' \
 + '\n' + '- Костюмы как на фото!' \
 + '\n' + '- Ёлочка, гори! Хоровод! Детские стихи!' \
 + '\n' + '- Загадывание желаний' \
 + '\n' + '- Вручение вашего подарка'\
 + '\n' + '- Общее фото на память' + '\n' \
 + '\n' + '(подходит для 1-2 детей, а также детям до 2 лет) ' + '\n' \
 + '\n' + f'До завтра стоимость от <b><u> 0 </u></b> <s> 0 </s> руб.' + '\n'\
 + '\n' + '*В поездках за город дополнительно рассчитывается дорога' + '\n'

caption_child2 = """Описание 2"""
caption_child3 = "Описание 3"
caption_child4 = "Описание 4"
caption_child5 = "Описание 5"
caption_child6 = "Утренник"
