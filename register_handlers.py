from handlers import *
from aiogram import types


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(main_menu, commands=['menu'])

    # Рассылка
    dp.register_message_handler(command_mailing, commands=['mailing'])
    dp.register_message_handler(set_mailing_photo, state=Mailing.text)
    dp.register_message_handler(send_message_to_all_users_in_db, state=Mailing.photo, content_types=types.ContentType.PHOTO)

    # Подарок
    dp.register_callback_query_handler(get_one_time_gift, text='/Подарок')

    # Блок регистрации основных хэндлеров
    dp.register_callback_query_handler(cancel_handler, text='отмена')
    dp.register_message_handler(get_contact, content_types=types.ContentType.CONTACT)
    dp.register_callback_query_handler(approved_name, text='Nameapproved')
    dp.register_callback_query_handler(disapproved_name, text='Namedisapproved')
    dp.register_callback_query_handler(no_contact, text='no_contact')
    dp.register_message_handler(get_file_id, content_types=types.ContentType.DOCUMENT)
    dp.register_message_handler(get_photo_id, content_types=types.ContentType.PHOTO)

    # Блок регистрации корпоративных хэндлеров
    dp.register_callback_query_handler(company_order, text='/Компанию')
    dp.register_message_handler(load_name, state=CommercialContact.name)

    # Блок регистрации взрослых хэндлеров
    dp.register_callback_query_handler(adult_order, text='/Взрослых')
    dp.register_callback_query_handler(adult_order_take_contacts, text='AdultChose1')

   # Блок регистрации детских хэндлеров
    dp.register_callback_query_handler(children_order, text='/Детей')
    # dp.register_callback_query_handler(children_order_print_menu_element, text=['menu_back', 'menu_next'])
    dp.register_callback_query_handler(children_order_print_menu, text=['product1', 'product2', 'product3',
                                                                    'product4', 'product5', 'product6'])
    dp.register_callback_query_handler(children_order_menu, text=['menu_back'])
    dp.register_callback_query_handler(children_order_choise, text=['1caption', '2caption', '3caption',
                                                                    '4caption', '5caption'])
    dp.register_callback_query_handler(children_count, text=['1_3childcount', '4_7childcount', '35childcount',
                                                             '58childcount', '8morechildcount'])
    dp.register_callback_query_handler(children_30_minutes, text=['30minsyes', '30minsno', 'morning_celebration'])
    dp.register_message_handler(children_age, state=ChildrenContact.age)
