import re

nums = input()

def main():
    lnums = re.split(r'[,\s]+', nums.strip())
    if len(lnums) != 3:
        print("Error: need 3 nums!")
    try:
        num1, num2, num3 = map(float, lnums)
        summ = num1 + num2 + num3
        av = round(summ / 3)
        print(av)
    except ValueError:
        print("Error: nums. Not a text")
    pass


if __name__ == '__main__':
    main()