# Более User-friendly решение:
def get_cookbook():
    with open('recipes.txt') as file:
        cook_book = {}
        for line in file:
            recipe_name = line.strip()
            ingredients_count = int(file.readline())
            ingredients = []
            for i in range(ingredients_count):
                ingredient = file.readline().strip()
                ingredient_name, quantity, measure = ingredient.split(' | ')
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': quantity,
                    'measure': measure
                })
            file.readline()
            cook_book[recipe_name] = ingredients
    return cook_book


def get_dishes(recipes_book):
    dishes = []
    dishes_all = []
    for dish_name in recipes_book.keys():
        dishes_all.append(dish_name)
    while True:
        print("Список доступных для добавления блюд:")
        n = 1
        for recipe in dishes_all:
            print(f'    {n}. {recipe}')
            n += 1
        print("Список блюд для приготовления:")
        n = 1
        for added in dishes:
            print(f'    {n}. {added}')
            n += 1
        num = int(input("Введите номер рецепта для добавления в список покупок (введите '0' чтоб закончить): "))
        if num == 0:
            break
        elif num > len(dishes_all):
            print("Такого рецепта не существует!")
        else:
            dishes.append(dishes_all[num - 1])
            dishes_all.remove(dishes_all[num - 1])
    return dishes


def get_shop_list_by_dishes(recipes_book):
    shopping_list = {}
    menu = get_dishes(recipes_book)
    person_count = int(input("Введите количество персон: "))
    for dish in menu:
        for shopping_pos in recipes_book[dish]:
            name, amount, string = shopping_pos.values()
            if name in shopping_list.keys():
                shopping_list[name]['quantity'] += int(amount) * person_count
            else:
                shopping_list[name] = {'measure': string, 'quantity': int(amount) * person_count}
    return shopping_list


def create_shoppinglist(recipes_book):
    shop_list = get_shop_list_by_dishes(recipes_book)
    print("Ваш список покупок: ")
    for pos in shop_list:
        print(f'{pos}: {shop_list[pos]}')


cook_book = get_cookbook()
create_shoppinglist(cook_book)
