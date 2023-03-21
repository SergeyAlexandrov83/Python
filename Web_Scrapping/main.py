from bs4 import BeautifulSoup
from selenium import webdriver
import json
import requests
import time
from tqdm import tqdm


def vac_search(source_page):
    bs = BeautifulSoup(source_page, 'xml')
    vac = bs.findAll('a', class_='serp-item__title')
    return vac


def key_words(words, bs):
    vacancy_description = bs.find('div', class_='vacancy-description')
    if words[0].lower() in vacancy_description.text.lower() and words[1].lower() in vacancy_description.text.lower():
        return True


def vacancy_parser(vac):
    fake_ua = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_2_1) '
                      'AppleWebKit/537.36 (HTML, like Gecko) '
                      'Chrome/107.0.0.0 Safari/537.36'
    }

    result = []
    for vacancy in tqdm(vac, desc='processing'):
        vacancy_url = vacancy['href']
        response = requests.get(url=vacancy_url, headers=fake_ua)
        time.sleep(0.2)

        bs = BeautifulSoup(response.text, 'xml')

        if key_words(['Django', 'Flask'], bs):
            vacancy_title = bs.find('div', class_='vacancy-title')
            if vacancy_title:
                position = vacancy_title.find('h1').text
                salary = vacancy_title.find('span', class_='bloko-header-section-2 bloko-header-section-2_lite').text
                company = bs.find('a', class_='bloko-link bloko-link_kind-tertiary').find('span').text

                city = bs.find('div', class_='vacancy-company-redesigned').find('p')
                if city:
                    city = city.text
                else:
                    city = bs.find('a', class_='bloko-link bloko-link_kind-tertiary bloko-link_disable-visited').find(
                        'span').text.split(',')[0]

                result.append({
                    'Должность': position,
                    'Зарплата': salary,
                    'Компания': company,
                    'Город': city,
                    'Ссылка на вакансию': vacancy_url
                })
    return result


if __name__ == '__main__':
    url = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'
    driver = webdriver.Chrome()

    try:
        driver.get(url)
        page_source = driver.page_source
        vacancies = vac_search(page_source)
        py_vacancies = vacancy_parser(vacancies)

        with open('python_vacancies.json', 'w', encoding='utf-8') as file:
            json.dump(py_vacancies, file, ensure_ascii=False)

    except Exception as ex:
        print(f'Error. {ex}')
    finally:
        driver.quit()
