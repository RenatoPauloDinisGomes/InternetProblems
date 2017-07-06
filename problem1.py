
import random
size = 10
list = [random.randint(0,50) for i in range(10)]
total = 0

prompt = "Three functions that compute the sum of the numbers in a given list using a " \
         "\n1 - for-loop\n2 - a while-loop\n3 - recursion.\noption: "


def recursive(i):
    if i == len(list):
        return 0
    else:
        return recursive(i + 1) + list[i]

def main():
    global total
    global list
    print(list)
    index = 0
    opt = input(prompt)
    if opt == "1":
        for i in range(len(list)):
            total += list[i]
        print(total)
    elif opt == "2":
        while (len(list) != index):
            total += list[index]
            index += 1
        print(total)
    elif opt == "3":
        print(recursive(0))
    else:
        print("Invalid option")


if __name__ == '__main__':
    main()
