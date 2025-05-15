# Все оказалось проще, а жаль
# PASS
n1, n2, n3 = map(int, input().split())

def main():

    sorted_nums = sorted([n1, n2, n3])
    median = sorted_nums[1]
    print(median)


if __name__ == '__main__':
    main()