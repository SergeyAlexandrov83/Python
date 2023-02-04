N = int(input("Введите количество измерений: "))
coord_first = []
coord_second = []
delta = 0
for i in range(N):
    coord_first.append(float(input(f"{i+1} координата первой точки в {N}-мерном пространстве: ")))
    coord_second.append(float(input(f"{i+1} координата второй точки в {N}-мерном пространстве: ")))
    delta += (coord_second[i] - coord_first[i]) ** 2
print(f"Расстояние между точками = {delta ** 0.5}")
