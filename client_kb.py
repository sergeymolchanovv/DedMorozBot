# -*- coding: utf-8 -*-
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# Блок общих кнопок
button_children = InlineKeyboardButton('Детей', callback_data="/Детей")
button_adults = InlineKeyboardButton('Взрослых', callback_data="/Взрослых")
button_company = InlineKeyboardButton('Юр. лицо (Взрослых и Детей)', callback_data="/Компанию")
button_get_gift = InlineKeyboardButton('Получить подарок ❄', callback_data="/Подарок")
kb_menu = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_menu.add(button_children).add(button_adults).add(button_company)
kb_menu_with_gift = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_menu_with_gift.add(button_children).add(button_adults).add(button_company).add(button_get_gift)

start_menu = KeyboardButton('/Start')
kb_start_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_start_menu.add(start_menu)

main_menu = KeyboardButton('/Menu')
kb_main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
kb_main_menu.add(main_menu)


name_button_yes = InlineKeyboardButton('Да', callback_data="Nameapproved")
name_button_no = InlineKeyboardButton('Нет', callback_data="Namedisapproved")
yes_no_kb = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
yes_no_kb.add(name_button_yes, name_button_no)

contact_button = KeyboardButton('Поделиться контактом', request_contact = True)
contact_button1 = KeyboardButton('Не делиться контактом')
contact_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
contact_kb.add(contact_button).add(contact_button1)

no_contact_button = InlineKeyboardButton('Не хочу делиться', callback_data='no_contact')
no_contact_kb = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
no_contact_kb.add(no_contact_button)

instagram_button = InlineKeyboardButton(text='Инстаграм',
                                        url='https://instagram.com/ded_moroz.tomsk',
                                        callback_data='inst')
telegram_button = InlineKeyboardButton(text='Телеграм',
                                       url='https://t.me/ded_moroz_tomsk',
                                       callback_data='telegram')
site_button = InlineKeyboardButton(text='Сайт',
                                   url='https://дедмороз-томск.рф',
                                   callback_data='site')
wa_button = InlineKeyboardButton(text="WhatsApp",
                                   url='https://wa.me/+79618881162',
                                   callback_data='whatsapp')
social_networks_kb = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
social_networks_kb.add(instagram_button, site_button).add(wa_button, telegram_button)



# Блок кнопок детских заказов
button_child_back = InlineKeyboardButton('Назад', callback_data="menu_back")
button_child_next = InlineKeyboardButton('Далее', callback_data="menu_next")
button_child1 = InlineKeyboardButton('Выбрать', callback_data="children_15_mins")
kb_child_captions1 = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_child_captions1.add(button_child1)
button_child2 = InlineKeyboardButton('Выбрать', callback_data="children_30_mins")
kb_child_captions2 = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_child_captions2.add(button_child2)
button_child3 = InlineKeyboardButton('Выбрать', callback_data="ded_moroz_mail")
kb_child_captions3 = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_child_captions3.add(button_child3)
button_child4 = InlineKeyboardButton('Выбрать', callback_data="forest_meeting")
kb_child_captions4 = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_child_captions4.add(button_child4)
button_child5 = InlineKeyboardButton('Выбрать', callback_data="online_gift")
kb_child_captions5 = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_child_captions5.add(button_child5)
button_child6 = InlineKeyboardButton('Выбрать', callback_data="utrennik")
kb_child_captions6 = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_child_captions6.add(button_child6)
kb_child_caption1_menu = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_child_caption1_menu.add(button_child1, button_child_next)
kb_child_caption2_menu = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_child_caption2_menu.add(button_child_back, button_child2, button_child_next)
kb_child_caption3_menu = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_child_caption3_menu.add(button_child_back, button_child3, button_child_next)
kb_child_caption4_menu = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_child_caption4_menu.add(button_child_back, button_child4, button_child_next)
kb_child_caption5_menu = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_child_caption5_menu.add(button_child_back, button_child5, button_child_next)
kb_child_caption6_menu = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_child_caption6_menu.add(button_child_back, button_child6)

kb_child_caption1_menu = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_child_caption1_menu.add(button_child_back, button_child1)
kb_child_caption2_menu = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_child_caption2_menu.add(button_child_back, button_child2)
kb_child_caption3_menu = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_child_caption3_menu.add(button_child_back, button_child3)
kb_child_caption4_menu = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_child_caption4_menu.add(button_child_back, button_child4)
kb_child_caption5_menu = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_child_caption5_menu.add(button_child_back, button_child5)
kb_child_caption6_menu = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_child_caption6_menu.add(button_child_back, button_child6)

button_children_count = InlineKeyboardButton('1-3', callback_data="1_3childcount")
button_children_count2 = InlineKeyboardButton('4-7', callback_data="4_7childcount")
button_children_count5 = InlineKeyboardButton('8 и более', callback_data="8morechildcount")
children_count_kb = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
children_count_kb.add(button_children_count, button_children_count2, button_children_count5)

button_children_30mins_yes = InlineKeyboardButton('Выбрать 30', callback_data="30minsyes")
button_children_30mins_no = InlineKeyboardButton('Нет, оставить 15', callback_data="30minsno")
button_children_30mins = InlineKeyboardButton('Выбрать 30 минут', callback_data="30minsyes")
button_children_morning = InlineKeyboardButton('Выбрать Утренник', callback_data="morning_celebration")
children_30min_kb = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
children_30min_kb.add(button_children_30mins_yes, button_children_30mins_no)
children_30min_kb_with_morning = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
# children_30min_kb_with_morning.add(button_children_30mins_no).add(button_children_morning).add(button_children_30mins)
children_30min_kb_with_morning.add(button_children_morning, button_children_30mins).add(button_children_30mins_no)

button_children_morning_yes = InlineKeyboardButton('Хочу', callback_data="morningyes")
button_children_morning_no = InlineKeyboardButton('Не хочу', callback_data="morningno")
children_morning_kb = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
children_morning_kb.add(button_children_30mins_yes, button_children_30mins_no).add(button_children_morning)

button_children_product1 = InlineKeyboardButton('15-минутное', callback_data="product1")
button_children_product2 = InlineKeyboardButton('30-минутное', callback_data="product2")
button_children_product3 = InlineKeyboardButton('Дед Мороз - почтальон', callback_data="product3")
button_children_product4 = InlineKeyboardButton('Лесная встреча', callback_data="product4")
button_children_product5 = InlineKeyboardButton('Онлайн-поздравление', callback_data="product5")
button_children_product6 = InlineKeyboardButton('Утренник', callback_data="product6")
button_back = InlineKeyboardButton('⬅ Назад', callback_data="menu")
children_product_kb = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
children_product_kb.add(button_children_product1).add(button_children_product2).add(button_children_product3)\
    .add(button_children_product4).add(button_children_product5).add(button_children_product6).add(button_back)


# Блок кнопок взрослых заказов
chose_button_adult = InlineKeyboardButton('Выбрать "На корпоратив"', callback_data="AdultChose1")
adult_chose_kb = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
adult_chose_kb.add(chose_button_adult).add(button_back)
