import asyncio
import json

from aiogram import types, Dispatcher
from Classes import CommercialContact, ChildrenContact, AdultContact, Contact, Mailing
# from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.types import ChatActions, ReplyKeyboardRemove, InputMedia, InputFile
from client_kb import *
from create_bot import dp, bot
from register_handlers import *
from publications import *
from database import *


serg_id = 357864166
kp_telegram_id = "BQACAgIAAxkBAAMiY1WZ14cYBZ_g17DOLUHh7ZuEdZUAAtUkAALw17FKJw34-lEGYZIqBA"
photo_telegram_id1 = "AgACAgIAAxkBAAMyY1Wf61ZbQmsCpOXsYbXT9B2cmbEAAtq_MRvw17FKLxGFzroLy6wBAAMCAAN5AAMqBA"
photo_telegram_id2 = "AgACAgIAAxkBAAM3Y1WgGrQ31yOq-Hsg2KWDM0Xxgv0AAtu_MRvw17FKgAPCZPaLXWcBAAMCAAN5AAMqBA"
photo_telegram_id3 = "AgACAgIAAxkBAAM4Y1WgLC6LzZe0AAG8CQvvO7kV-svZAALcvzEb8NexSoo-ck9CNj5gAQADAgADeQADKgQ"
photo_telegram_id4 = "AgACAgIAAxkBAAM5Y1WgV8BHKKlpfBnC6MY6sQ1xzdAAAt2_MRvw17FKgQWq068AAc9DAQADAgADeQADKgQ"
photo_telegram_id5 = "AgACAgIAAxkBAAM6Y1Wgdvm5toF0C-MhnRTy5VsuBv8AAt6_MRvw17FKw4jZRK8bTOIBAAMCAAN5AAMqBA"
photo_telegram_id6 = "AgACAgIAAxkBAAIJ9GLU9oiVfPWq63f3wceDKLOPTToWAAJCuzEbkoeoSkLX5kkpqtobAQADAgADeQADKQQ"
photo_telegram_corporate = "AgACAgIAAxkBAANRY1WhtIwxlDcV4VlQFDeGMvNZ5YcAAuW_MRvw17FK76YIdocWvREBAAMCAAN5AAMqBA"
photo_telegram_adult = "AgACAgIAAxkBAANSY1WhzXmsLnVUUfghNqKskni5kL8AAua_MRvw17FKimbZtQIeWJMBAAMCAAN5AAMqBA"

publications_index_dict = {0: (caption_child1, kb_child_caption1_menu, photo_telegram_id1),
                           1: (caption_child2, kb_child_caption2_menu, photo_telegram_id2),
                           2: (caption_child3, kb_child_caption3_menu, photo_telegram_id3),
                           3: (caption_child4, kb_child_caption4_menu, photo_telegram_id4),
                           4: (caption_child5, kb_child_caption5_menu, photo_telegram_id5),
                           5: (caption_child6, kb_child_caption6_menu, photo_telegram_id1)}
index = 0

contact = Contact(False)


# Блок общих хэндлеров
async def command_start(message: types.Message):
    await message.answer('''Добро пожаловать к главному волшебнику Нового года - Дедушке Морозу 😊

Я знаю, как сложно бывает выбрать нужное поздравление для ребенка, компании друзей или на работу, поэтому вместе со своими эльфами создали этот бот-помощник!✨

Уверен, что вы найдете то, что подходит именно вам!

А моя внучка Снегурочка будет рада забронировать удобное для вас время🎉

А чтобы добавить вам праздничного настроения, я подготовил для вас подарок! Жми на Снежинку❄️

Кстати, это не единственный подарок. Оставьте заявку на праздник, чтобы получить второй 🎁

С наступающим Новым годом!🎄''')

    menu = await get_keyboard_menu()
    await message.answer('Выберите в меню, кого требуется поздравить', reply_markup=menu)
    print(message.chat.id)


async def main_menu(message: types.Message):
    menu = await get_keyboard_menu()
    await message.answer('Выберите в меню, кого требуется поздравить', reply_markup=menu)
    print(message.chat.id)
    print(message.from_user.username)


async def get_one_time_gift(callback: types.CallbackQuery):
    contact.gifted = True
    await callback.message.edit_text('На тебе подарок, епта в лицо прям. Выбирай, кого поздравить')
    await callback.message.edit_reply_markup(kb_menu)


async def get_keyboard_menu():
    if contact.gifted is False:
        return kb_menu_with_gift
    else:
        return kb_menu


async def cancel_handler(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await callback.message.answer('Хорошо')


async def get_contact(msg: types.Message):
    global contact
    contact.phone = msg.contact.phone_number
    contact.username = msg.from_user.username
    print(msg.from_user.username)
    await data_collection_and_final_sending(msg)


async def get_file_id(msg: types.Message):
    print(msg.document.file_id)


async def get_photo_id(msg: types.Message):
    print(msg.photo[-1].file_id)


async def data_collection_and_final_sending(msg):
    if isinstance(contact, CommercialContact):
        if msg.from_user.full_name != contact.name:
            await bot.send_message(serg_id, 'Корпоративный заказ 👇' + '\n' + f'Имя: {contact.name}' + '\n' +
                                            f'Username: @{contact.username}')
        else:
            await bot.send_message(serg_id, 'Корпоративный заказ 👇' + '\n' +
                                            f'Username: @{contact.username}')
        await return_to_menu(msg)

    elif isinstance(contact, AdultContact):
        if msg.from_user.full_name != contact.name:
            await bot.send_message(serg_id, 'Заказ на корпоратив 👇' + '\n' +
                                            f'Имя: {contact.name}' + '\n' +
                                            f'Username: @{contact.username}')
        else:
            await bot.send_message(serg_id, 'Заказ на корпоратив 👇' + '\n' +
                                            f'Username: @{contact.username}')
        await return_to_menu(msg)

    elif isinstance(contact, ChildrenContact):
        if msg.from_user.full_name != contact.name:
            await bot.send_message(serg_id,
                                   'Заказ для ребёнка 👇' + '\n' + f'Имя заказчика: {contact.name}' + '\n' +
                                   f'Username: @{contact.username}' + '\n' +
                                   f'Тип заказа: {contact.order}' + '\n' +
                                   f'Количество детей: {contact.children_count}' + '\n' +
                                   f'Возраст детей: {contact.age}')
        else:
            await bot.send_message(serg_id,
                                   'Заказ для ребёнка 👇' + '\n' +
                                   f'Username: @{contact.username}' + '\n' +
                                   f'Тип заказа: {contact.order}' + '\n' +
                                   f'Количество детей: {contact.children_count}' + '\n' +
                                   f'Возраст детей: {contact.age}')
        await return_to_menu(msg)


async def return_to_menu(msg):
    await bot.send_message(msg.chat.id,
                           'Снегурочка свяжется с вами в ближайшее время и расскажет все подробности 😉' + '\n' + '\n' +
                           'Если хотите связаться самостоятельно, контакты снегурочки:' + '\n' +
                           '+79999999999', reply_markup=social_networks_kb)
    await msg.forward(serg_id)
    await msg.answer('Также обещанный подарок для вас. Сказка на ночь!', reply_markup=kb_main_menu)
    await bot.send_document(msg.chat.id, document=kp_telegram_id)
    push_data(msg.chat.id, msg.contact.phone_number, msg.from_user.username)


async def approved_name(callback: types.CallbackQuery):
    await callback.message.delete_reply_markup()
    await callback.message.delete()
    global contact
    contact.name = callback.from_user.full_name
    contact.username = callback.from_user.username
    await callback.message.answer('Нажмите кнопку "Поделиться контактом"', reply_markup=contact_kb)
    await callback.message.answer('Либо нажмите "не хочу делиться"', reply_markup=no_contact_kb)


async def no_contact(callback: types.CallbackQuery):
    await callback.message.delete_reply_markup()
    await bot.send_message(callback.message.chat.id,
                           'Если хотите связаться самостоятельно, контакты снегурочки:' + '\n' +
                           '+79999999999', reply_markup=social_networks_kb)
    await callback.message.answer('Чтобы вернуться в меню, нажмите на кнопку /Menu', reply_markup=kb_main_menu)
    push_data(callback.from_user.id, username=callback.from_user.username)


async def disapproved_name(callback: types.CallbackQuery):
    await callback.message.edit_text('Напишите ваше имя')
    await CommercialContact.name.set()


async def load_name(message: types.Message, state: FSMContext):
    global contact
    contact.name = message.text
    await state.finish()
    await message.answer('Нажмите кнопку "Поделиться контактом"', reply_markup=contact_kb)
    await message.answer('Либо нажмите "не хочу делиться"', reply_markup=no_contact_kb)


async def command_mailing(message: types.Message):
    if (message.from_user.id == 357864166) or (message.from_user.id == 461358524) or (message.from_user.id == 344743951):
        await message.answer('Вставьте текст для рассылки')
        await Mailing.text.set()
    else:
        await message.answer('Вам недоступна эта функция')


async def set_mailing_photo(message: types.Message, state: FSMContext):
    global mailing
    mailing = Mailing()
    mailing.text = message.text
    await Mailing.next()
    await message.answer('Вставьте фото для рассылки')


async def send_message_to_all_users_in_db(message: types.Message, state: FSMContext):
    mailing.photo = message.photo[-1].file_id
    list_of_ids = get_all_tg_ids_from_db()

    for id in list_of_ids:
        await bot.send_photo(id, caption=mailing.text, photo=mailing.photo)
    await state.finish()


# Блок корпоративных хэндлеров
async def company_order(callback: types.CallbackQuery):
    await assign_contact_class_obj(contact, "CommercialContact")
    await callback.message.delete_reply_markup()
    await callback.message.delete()
    await bot.send_photo(callback.message.chat.id, photo=photo_telegram_corporate,
                         caption=caption_corporate, parse_mode=types.ParseMode.HTML)
    # await callback.message.edit_text()
    await bot.send_document(callback.message.chat.id, document=kp_telegram_id)
    await callback.message.answer('Если вам всё понравилось, оставьте ваши контакты, чтобы снегурочка ' +
                                  'могла с вами связаться', reply_markup=contact_kb)
    await callback.message.answer(f'Ваше настоящее имя: {callback.from_user.full_name}?', reply_markup=yes_no_kb)


# Блок взрослых хэндлеров
async def adult_order(callback: types.CallbackQuery):
    await callback.message.delete_reply_markup()
    await callback.message.delete()
    await assign_contact_class_obj(contact, "AdultContact")

    await bot.send_photo(callback.message.chat.id, photo=photo_telegram_adult,
                         caption=caption_adult, parse_mode=types.ParseMode.HTML,
                         reply_markup=adult_chose_kb)


async def adult_order_take_contacts(callback: types.CallbackQuery):
    await callback.message.delete_reply_markup()
    await callback.message.delete()
    await callback.message.answer('Если вы хотите, чтобы Снегурочка с вами связалась, оставьте, пожалуйста, '
                                  'свои контактные данные и мы вам перезвоним!' + '\n' +
                                  f'Ваше настоящее имя: {callback.from_user.full_name}?', reply_markup=yes_no_kb)


# Блок детских хэндлеров
async def children_order(callback: types.CallbackQuery):
    await callback.message.delete_reply_markup()
    await callback.message.delete()
    await assign_contact_class_obj(contact, "ChildrenContact")
    await callback.message.answer('Нажмите на поздравление, чтобы узнать подробнее', reply_markup=children_product_kb)

    # await bot.send_photo(callback.message.chat.id, photo=publications_index_dict[index][2],
    #                      caption=publications_index_dict[index][0],
    #                      reply_markup=publications_index_dict[index][1])
# async def children_order_print_menu_element(callback: types.CallbackQuery):
#     await callback.answer('')
#     global index
#     if callback.data == 'menu_back':
#         index -= 1
#     elif callback.data == 'menu_next':
#         index += 1
#
#     file = InputMedia(media=publications_index_dict[index][2], caption=publications_index_dict[index][0])
#     await callback.message.edit_media(file, reply_markup=publications_index_dict[index][1])


async def children_order_print_menu(callback: types.CallbackQuery):
    # await callback.message.edit_text()
    await callback.answer('')
    if callback.data == 'product1':
        await callback.message.delete()
        await bot.send_photo(callback.message.chat.id, photo=publications_index_dict[0][2],
                             caption=publications_index_dict[0][0],
                             reply_markup=publications_index_dict[0][1])
    elif callback.data == 'product2':
        await callback.message.delete()
        await bot.send_photo(callback.message.chat.id, photo=publications_index_dict[1][2],
                             caption=publications_index_dict[1][0],
                             reply_markup=publications_index_dict[1][1])
    elif callback.data == 'product3':
        await callback.message.delete()
        await bot.send_photo(callback.message.chat.id, photo=publications_index_dict[2][2],
                             caption=publications_index_dict[2][0],
                             reply_markup=publications_index_dict[2][1])
    elif callback.data == 'product4':
        await callback.message.delete()
        await bot.send_photo(callback.message.chat.id, photo=publications_index_dict[3][2],
                             caption=publications_index_dict[3][0],
                             reply_markup=publications_index_dict[3][1])
    elif callback.data == 'product5':
        await callback.message.delete()
        await bot.send_photo(callback.message.chat.id, photo=publications_index_dict[4][2],
                             caption=publications_index_dict[4][0],
                             reply_markup=publications_index_dict[4][1])
    elif callback.data == 'product6':
        await callback.message.delete()
        await bot.send_photo(callback.message.chat.id, photo=publications_index_dict[5][2],
                             caption=publications_index_dict[5][0],
                             reply_markup=publications_index_dict[5][1])


async def children_order_menu(callback: types.CallbackQuery):
    await callback.answer('')
    await callback.message.delete()
    await callback.message.answer('Выберите поздравление', reply_markup=children_product_kb)
# async def children_order_print_menu_element(callback: types.CallbackQuery):
#     await callback.answer('')
#     global index
#     if callback.data == 'menu_back':
#         index -= 1
#     elif callback.data == 'menu_next':
#         index += 1
#
#     file = InputMedia(media=publications_index_dict[index][2], caption=publications_index_dict[index][0])
#     await callback.message.edit_media(file, reply_markup=publications_index_dict[index][1])


async def children_order_choise(callback: types.CallbackQuery):
    await callback.answer('')
    await callback.message.delete()
    if callback.data == "1caption":
        contact.order = '1caption'
    elif callback.data == "2caption":
        contact.order = '2caption'
    elif callback.data == "3caption":
        contact.order = '3caption'
    elif callback.data == "4caption":
        contact.order = '4caption'
    elif callback.data == "5caption":
        contact.order = '5caption'
    await callback.message.answer('Выберите количество детей', reply_markup=children_count_kb)


async def children_count(callback: types.CallbackQuery):
    await callback.answer('')
    await interpretate_children_count(callback)
    print(callback.data)
    if (callback.data == '4_7childcount') and (contact.order == '1caption'):
        await callback.message.edit_text('Боюсь, Дедушке не хватит времени на всех ребят '
                                      'при экспресс-поздравлении (15 мин.)'
                                      + '\n' + '\n' +
                                      'Не хотите выбрать 30 минут?', reply_markup=children_30min_kb)
    elif (callback.data == '8morechildcount') and (contact.order == '1caption'):
        await callback.message.edit_text('Боюсь, Дедушке не хватит времени на всех ребят '
                                         'при экспресс-поздравлении (15 мин.)' + '\n' +
                                         'Оповещаем вас, что 8 и каждый последующий ребёнок оплачивается дополнительно!'
                                         'Стоимость доплаты составит 300 рублей за каждого ребёнка 😊' + '\n'
                                          + '❗️Если в поздравлении участвует больше 10 детей, '
                                            'предлагаем вам рассмотреть формат утренника (от 10-20 детей)'
                                          + '\n' +
                                         'Изменим тип поздравления?', reply_markup=children_30min_kb_with_morning)
    elif (callback.data == '8morechildcount') and (contact.order == '2caption'):
        await callback.message.edit_text('8й и каждый последующий ребёнок оплачивается дополнительно '
                                      '300 рублей за ребёнка' + '\n'
                                      + 'Если у вас больше 10 детей, предлагаем взять утренник'
                                      + '\n' + '\n' +
                                      'Не хотите выбрать утренник?', reply_markup=children_morning_kb)
    else:
        await callback.message.answer('Напишите возраст детей')
        await ChildrenContact.age.set()


async def children_30_minutes(callback: types.CallbackQuery):
    await callback.answer('')
    if callback.data == '30minsyes':
        await callback.message.edit_text('Хорошо, поменял ваш заказ на 30-минутное поздравление')
        contact.order = '2caption, но сначала хотел 1caption'
        await callback.message.answer('Напишите возраст детей')
        await ChildrenContact.age.set()
    elif callback.data == 'morning_celebration':
        await callback.message.edit_text('Хорошо, поменял ваш заказ на утренник')
        contact.order = '6caption, но хотел 1caption'
        await callback.message.answer('Напишите возраст детей')
        await ChildrenContact.age.set()
    else:
        await callback.message.edit_text('Хорошо. Тогда напишите возраст детей')
        await ChildrenContact.age.set()


async def children_age(msg: types.Message,  state: FSMContext):
    async with state.proxy() as data:
        data['age'] = msg.text
    async with state.proxy() as data:
        contact.age = data['age']
    await state.finish()
    await msg.answer('Если вы хотите, чтобы Снегурочка с вами связалась, оставьте, пожалуйста, '
                     'свои контактные данные и мы вам перезвоним!' + '\n' +
                     f'Ваше настоящее имя: {msg.from_user.full_name}?', reply_markup=yes_no_kb)


async def interpretate_children_count(callback):
    await callback.answer('')
    if callback.data == '1_3childcount':
        contact.children_count = '1-3 ребенка'
    elif callback.data == '4_7childcount':
        contact.children_count = '4-7 детей'
    elif callback.data == '35childcount':
        contact.children_count = '3-5 детей'
    elif callback.data == '58childcount':
        contact.children_count = '5-8 детей'
    elif callback.data == '8morechildcount':
        contact.children_count = '8 и более детей'


async def assign_contact_class_obj(user_contact: Contact, classname: str):
    global contact
    if classname == "AdultContact":
        if user_contact.gifted is False:
            contact = AdultContact(False)
        else:
            contact = AdultContact(True)
    elif classname == "ChildrenContact":
        if user_contact.gifted is False:
            contact = ChildrenContact(False)
        else:
            contact = ChildrenContact(True)
    elif classname == "CommercialContact":
        if user_contact.gifted is False:
            contact = CommercialContact(False)
        else:
            contact = CommercialContact(True)


# # @dp.message_handler(state=Admin.age)  # ловим четвертый ответ
# async def load_age(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['age'] = message.text
#     print(message.from_user.id)
#     async with state.proxy() as data:
#         await bot.send_message(357864166, 'Новый заказ!'
#                                + '\n' + 'Имя: ' + data['name']
#                                + '\n' + 'Телефон: ' + data['phone']
#                                + '\n' + 'Удобная дата: ' + data['date']
#                                + '\n' + 'Возраст ребёнка: ' + data['age'])
#
#     await message.reply('Спасибо за заказ. С вами свяжутся в ближайшее время.')
#
#     await state.finish()  # завершаем машину состояний
