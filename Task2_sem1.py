# Напишите программу для. проверки истинности
#  утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
#  для всех значений предикат.

def inputNumbers(x):
    xyz = ["X", "Y", "Z"]
    list1 = []
    for i in range(x):
        list1.append(input(f"Введите значение {xyz[i]}: "))
    return list1


def Predicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result


affirmation = inputNumbers(3)

if Predicate(affirmation) == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")