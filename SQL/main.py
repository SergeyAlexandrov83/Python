import psycopg2


def create_db(connect):
    with connect.cursor() as cur:
        cur.execute("""
        
        CREATE TABLE IF NOT EXISTS clients (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(60) NOT NULL,
            last_name VARCHAR(60) NOT NULL,
            email VARCHAR(40) UNIQUE NOT NULL 
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS phones (
            client_id INTEGER NOT NULL REFERENCES clients (id) ON DELETE CASCADE,
            phone VARCHAR(40) UNIQUE NOT NULL,
            is_active BOOLEAN DEFAULT TRUE,
            CONSTRAINT client_phone_pk PRIMARY KEY (client_id, phone)
        );
        """)
        print('Таблицы "clients" и "phones" созданы в базе данных')


def add_client(connect, first_name, last_name, email, phones=None):
    with connect.cursor() as cur:
        cur.execute('''
        INSERT INTO clients (first_name, last_name, email)
        VALUES (%s, %s, %s) RETURNING id;
        ''', (first_name, last_name, email))
        client_id = cur.fetchone()[0]
        print(f'Добавлен новый клиент c id - {client_id}')
        if phones:
            for phone in phones:
                add_phone(connect, client_id, phone)


def add_phone(connect, client_id, phone):
    with connect.cursor() as cur:
        cur.execute('''
        INSERT INTO phones (client_id, phone)
        VALUES (%s, %s);
        ''', (client_id, phone))
        print(f'Клиенту с id {client_id} добавлен телефон - {phone}')


def change_client(connect, client_id, first_name=None, last_name=None, email=None, phones=None):
    data_dict = {'first_name': first_name, 'last_name': last_name, 'email': email}
    sql_set = ", ".join([f"{key} = '{value}'" for key, value in data_dict.items() if value])
    sql_request = f'''
    UPDATE clients SET {sql_set}
    WHERE id = {client_id};
    '''
    with connect.cursor() as cur:
        if sql_set:
            cur.execute(sql_request)
        if phones:
            cur.execute('''
            SELECT phone FROM phones
            WHERE client_id=%s AND is_active=TRUE;
            ''', (client_id,))
            client_phones = cur.fetchall()
            if len(client_phones) == len(phones):
                for i, phone in enumerate(client_phones):
                    cur.execute('''
                                UPDATE phones SET phone=%s
                                WHERE client_id=%s AND phone=%s AND is_active=TRUE;
                                ''', (phones[i], client_id, phone[0]))
    print(f'Изменения в данные клиента с id {client_id} - внесены')


def delete_phone(connect, client_id, phone):
    with connect.cursor() as cur:
        cur.execute('''
        SELECT phone FROM phones
        WHERE client_id=%s AND phone=%s;
        ''', (client_id, phone))
        client_phones = cur.fetchall()
        if client_phones:
            cur.execute('''
            UPDATE phones SET is_active=FALSE
            WHERE client_id=%s AND phone=%s;
            ''', (client_id, phone))
            print(f'Телефон {phone} клиента с id {client_id} - удален')
        else:
            print(f'Телефон {phone} клиента с id {client_id} не записан')


def delete_client(connect, client_id):
    with connect.cursor() as cur:
        cur.execute('''
        DELETE FROM clients WHERE id=%s;
        ''', (client_id,))
        print(f'Клиент с id {client_id} удален')


def find_client(connect, first_name=None, last_name=None, email=None, phone=None):
    data_dict = {'first_name': first_name, 'last_name': last_name, 'email': email, 'phone': phone}
    sql_where = " AND ".join([f"{key} = '{value}'" for key, value in data_dict.items() if value])
    sql_request = f'''
    SELECT DISTINCT cl.id, cl.first_name, cl.last_name FROM phones AS ph
    JOIN clients AS cl ON ph.client_id = cl.id
    WHERE {sql_where};
    '''
    with connect.cursor() as cur:
        cur.execute(sql_request)
        print(f'Найдено: {cur.fetchall()}')


if __name__ == '__main__':
    with psycopg2.connect(database="clients_db", user="postgres", password="GoRUS1103", ) as conn:
        try:
            create_db(conn)
            add_client(conn,
                       first_name='Василий',
                       last_name='Пупкин',
                       email='pupkin@gmail.com',
                       phones=('+79107771234', '+79154504545')
                       )
            add_client(conn,
                       first_name='Дмитрий',
                       last_name='Онегин',
                       email='onegin_d@gmail.com',
                       phones=('+79126754321',)
                       )
            add_client(conn,
                       first_name='Наталья',
                       last_name='Ростова',
                       email='rostova_nat@gmail.com'
                       )
            add_client(conn,
                       first_name='Анна',
                       last_name='Каренина',
                       email='rjd_forever@gmail.com'
                       )
            add_phone(conn,
                      client_id=3,
                      phone='+79056005040')
            add_phone(conn,
                      client_id=4,
                      phone='+78002353535')
            delete_phone(conn,
                         client_id=1,
                         phone='+79154504545')
            change_client(conn,
                          client_id=4,
                          last_name='Фрагментовна',
                          email='i_did_it@gmail.com')
            delete_client(conn,
                          client_id=4)
            find_client(conn,
                        first_name='Дмитрий',
                        last_name='Онегин')
        except psycopg2.Error as er:
            print(f'ERROR: {er}')
    conn.close()
