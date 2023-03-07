import json

import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker

from models import Publisher, Book, Shop, Sale, Stock, create_tables

with open('password.txt') as f:
    password = f.readline()

DNS = f'postgresql://postgres:{password}@localhost:5432/bookstore'
engine = sq.create_engine(DNS)

Session = sessionmaker(bind=engine)
session = Session()


def find_publisher_by_id(ses):
    result = input('Enter publisher id ')
    query = ses.query(Publisher).filter(Publisher.id == result)
    for i in query.all():
        return print(f'Publisher id {result} -> {i.name}')


def find_publisher_by_name(ses):
    result = input('Enter publisher name  ')
    query = ses.query(Publisher).filter(Publisher.name == result)
    for i in query.all():
        return print(f'Publisher {result} -> id {i.id}')


def find_shop_by_publisher_name(ses):
    result = input('Enter publisher name ')
    query = ses.query(Shop.name).join(Stock).join(Book).join(Publisher).filter(Publisher.name == result)
    for i in query.all():
        return print(i)


if __name__ == '__main__':

    create_tables(engine=engine)

    with open('tests_data.json') as test_file:
        test_data = json.load(test_file)

    for item in test_data:
        model = {
            'publisher': Publisher,
            'shop': Shop,
            'book': Book,
            'stock': Stock,
            'sale': Sale,
        }[item.get('model')]
        session.add(model(id=item.get('pk'), **item.get('fields')))
    session.commit()

    find_publisher_by_id(session)
    find_publisher_by_name(session)
    find_shop_by_publisher_name(session)
