import sqlite3


def check_user_in_db(telegram_id):
    conn = sqlite3.connect('data/snowman_database.db')
    cursor = conn.cursor()
    cursor.execute(f'Select TelegramID FROM MainDB WHERE TelegramID = {telegram_id}')
    conn.commit()
    records = cursor.fetchall()
    if records != []:
        return True
    else:
        return False


def get_user_data_from_db(telegram_id):
    conn = sqlite3.connect('data/snowman_database.db')
    cursor = conn.cursor()
    cursor.execute(f'Select TelegramID, Phone, Username, Gifted, NameInTelegram FROM MainDB WHERE TelegramID = {telegram_id}')
    conn.commit()
    data = cursor.fetchall()
    list_of_params = []
    for parameter in data:
        list_of_params.append(parameter[0])
    cursor.close()
    return data



def push_data(telegram_id, phone=None, username=None, gifted=None, tg_name=None):
    conn = sqlite3.connect('data/snowman_database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO MainDB (TelegramID, Phone, Username, Gifted, NameInTelegram) VALUES (?, ?, ?, ?, ?)',
                   (telegram_id, phone, username, gifted, tg_name))
    conn.commit()


def check_gifted(tg_id):
    conn = sqlite3.connect('data/snowman_database.db')
    cursor = conn.cursor()
    cursor.execute(f'Select Gifted FROM MainDB where TelegramID = {tg_id}')
    records = cursor.fetchall()
    conn.commit()
    if records[0][0] == 0:
        return False
    else:
        return True

def update_gifted_in_db(tg_id):
    conn = sqlite3.connect('data/snowman_database.db')
    cursor = conn.cursor()
    cursor.execute(f'Update MainDB SET Gifted = 1 WHERE TelegramID = {tg_id}')
    conn.commit()


def update_phone_in_db(tg_id, phone):
    conn = sqlite3.connect('data/snowman_database.db')
    cursor = conn.cursor()
    cursor.execute(f'Update MainDB SET Phone = {phone} WHERE TelegramID = {tg_id}')
    conn.commit()


def get_all_tg_ids_from_db():
    conn = sqlite3.connect('data/snowman_database.db')
    cursor = conn.cursor()
    cursor.execute('select distinct TelegramID from MainDB')
    records = cursor.fetchall()
    list_of_ids = []
    for id in records:
        list_of_ids.append(id[0])
    cursor.close()
    print(list_of_ids)
    return list_of_ids
