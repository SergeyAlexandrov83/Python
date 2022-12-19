import datetime as dt
import tqdm
import requests


def get_quest():
    t_date = int(dt.datetime.timestamp(dt.datetime.today()))
    f_date = t_date - 172800
    pbar = tqdm.tqdm(desc='Progress', total=None, ncols=100, unit=' вопросов найдено')
    key = 1
    page = 0
    questions = {}
    while True:
        page += 1
        url = "https://api.stackexchange.com/2.3/questions"
        params = {
            'page': page,
            'pagesize': 100,
            'order': 'desc',
            'sort': 'creation',
            'tagged': 'python',
            'site': 'stackoverflow',
            'fromdate': f_date,
            'todate': t_date
        }
        response = requests.get(url=url, params=params)
        if response.status_code != 200:
            print(f'Что то пошло не так! Сервер вернул: {response.status_code}')
        data = response.json()
        for question in data['items']:
            questions[key] = {'link': question['link'], 'title': question['title']}
            pbar.update(n=1)
            key += 1
        if not data['has_more']:
            return questions


def main():
    omg = get_quest()  # Эту переменную нельзя называть иначе!! XD
    for k, line in omg.items():
        print(f'\n{k}: {line["title"]} \n{line["link"]}\n')


if __name__ == '__main__':
    main()
