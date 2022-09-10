import sqlite3




def push_data(telegram_id, phone=None, username=None):
    conn = sqlite3.connect('snowman_database.db')
    cursor = conn.cursor()
    print('попали в пуш дата')
    cursor.execute('INSERT INTO MainDB (TelegramID, Phone, Username) VALUES (?, ?, ?)', (telegram_id, phone, username))
    print('сработал метод без телефона')
    conn.commit()


def get_all_tg_ids_from_db():
    conn = sqlite3.connect('snowman_database.db')
    cursor = conn.cursor()
    cursor.execute('select distinct TelegramID from MainDB')
    records = cursor.fetchall()
    list_of_ids = []
    for id in records:
        list_of_ids.append(id[0])
    cursor.close()
    print(list_of_ids)
    return list_of_ids
