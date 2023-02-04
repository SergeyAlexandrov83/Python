import random
import time

start = time.time()
count = 100
result = False
while count > 0:
    predicates = []
    for i in range(random.randint(5, 25)):
        predicates.append(bool(random.randint(0, 1)))
    print(predicates)
    for i in range(len(predicates) - 2):
        left = not (predicates[i] or predicates[i+1])
        right = not predicates[i] and not predicates[i+1]
        result = left == right
    print(result)
    count -= 1
end = time.time()
time_result = end - start
print(time_result)
