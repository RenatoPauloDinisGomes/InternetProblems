listA = [i for i in range(10)]
listB = ["A", "B", "C", "D", "E", "F"]
listC = []


def main():
    problem = "Function that combines two lists by alternatingly taking elements.\nFor example: given the two lists [a, b, c] and [1, 2, 3], the function return [a, 1, b, 2, c, 3]."
    print(problem)
    print("list A:", end=" ")
    print(listA)
    print("list B:", end=" ")
    print(listB)
    lenA = len(listA)
    lenB = len(listB)
    maxlen = max(lenA, lenB)
    for i in range(maxlen):
        if i < lenA:
            listC.append(listA[i])
        if i < lenB:
            listC.append(listB[i])
    print("list C:", end=" ")
    print(listC)


if __name__ == '__main__':
    main()
