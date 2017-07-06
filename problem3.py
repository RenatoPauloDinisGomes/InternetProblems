holder = [-1 for i in range(100)]

def main():
    problem = "Write a function that computes the list of the first 100 Fibonacci numbers. \nBy definition, the first two numbers in the Fibonacci sequence are 0 and 1, and each subsequent number is the sum of the previous two."
    holder[0] = 0
    holder[1] = 1
    dinamic(2)
    print(problem)
    for elm in holder:
        print(elm)


def dinamic(i):
    if i == 100:
        return
    if holder[i] != -1:
        return holder[i]
    else:
        holder[i] = holder[i - 1] + holder[i - 2]
        dinamic(i + 1)


if __name__ == '__main__':
    main()
