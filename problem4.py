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
    list = [random.randint(0, 100) for _ in range(5)]

    print(list)
    for i in range(len(list)):
        for j in range(len(list)):
            if comparator(list[i], list[j]) > 0:
                list[i], list[j] = list[j], list[i]
    print("Largest possible number: ", end="")
    for elm in list:
        print(elm, end="")


if __name__ == '__main__':
    main()
