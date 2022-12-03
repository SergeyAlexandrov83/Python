# Задача №2 "Список покупок":
def get_shop_list_by_dishes(dishes, person_count):
    shopping_list = {}

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

    for dish in dishes:
        for shopping_pos in cook_book[dish]:
            name, amount, string = shopping_pos.values()
            if name in shopping_list.keys():
                shopping_list[name]['quantity'] += int(amount) * person_count
            else:
                shopping_list[name] = {'measure': string, 'quantity': int(amount) * person_count}
    return shopping_list


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
