
import random
size = 10
lista = [random.randint(0, 50) for i in range(10)]
total = 0

prompt = "Three functions that compute the sum of the numbers in a given list using a " \
         "\n1 - for-loop\n2 - a while-loop\n3 - recursion.\noption: "


def recursive(i):
    if i == len(lista):
        return 0
    else:
        return recursive(i + 1) + lista[i]

def main():
    global total
    global lista
    print(lista)
    index = 0
    opt = input(prompt)
    if opt == "1":
        for elm in lista:
            total += elm
        print(total)
    elif opt == "2":
        while (len(lista) != index):
            total += lista[index]
            index += 1
        print(total)
    elif opt == "3":
        print(recursive(0))
    else:
        print("Invalid option")


if __name__ == '__main__':
    main()
