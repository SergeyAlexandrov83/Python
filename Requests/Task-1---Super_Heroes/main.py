import requests


def main():
    url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api'
    all_heroes = requests.get(url=url + '/all.json',
                              headers={'Content-Type': 'application/json; charset=utf-8'})
    heroes = ['Hulk', 'Captain America', 'Thanos']
    intelligence = {}
    for hero in all_heroes.json():
        if hero['name'] in heroes:
            intelligence[hero['name']] = hero['powerstats']['intelligence']
    final_dict = dict([max(intelligence.items(), key=lambda k_v: k_v[1])])
    print(final_dict)


if __name__ == '__main__':
    main()
