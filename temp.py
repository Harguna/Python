def isBeautiful(case):
    imps = 0
    ones = 0
    negs = 0
    for num in case:
        if num == 0:
            continue
        elif num == 1:
            ones += 1
        elif num == -1:
            negs += 1
        else:
            imps += 1
            if imps > 1:
                return 'no'
    if imps == 1 and negs > 0:
        return 'no'
    elif negs > 1 and ones == 0:
        return 'no'
    else:
        return 'yes'


def main():
    answers = []
    numCases = int(input())
    for i in range(numCases):
        input()
        case = [int(x) for x in input().split()]
        answers.append(isBeautiful(case))
    for answer in answers:
        print(answer)


main()