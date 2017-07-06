import random


def comparator(x, y):
    a, b = str(x), str(y)
    ab, ba = a + "" + b, b + "" + a
    if int(ab) > int(ba):
        return 1
    else:
        return -1


def main():
    problem = "Write a function that given a list of non negative integers," \
              "arranges them such that they form the largest possible number."
    print(problem)
    lista = [random.randint(0, 100) for _ in range(5)]

    print(lista)
    for i, valuei in enumerate(lista):
        for j, valuej in enumerate(lista):
            if comparator(valuei, valuej) > 0:
                lista[i], lista[j] = valuej, valuei
    print("Largest possible number: ", end="")
    for elm in lista:
        print(elm, end="")


if __name__ == '__main__':
    main()
