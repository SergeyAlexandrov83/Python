# Задача 1 "Чтение из файла":
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

print(cook_book)