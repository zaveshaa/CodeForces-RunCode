import argparse


def main():
    p = argparse.ArgumentParser()
    p.add_argument('nums', nargs='*')
    a = p.parse_args().nums

    if not a:
        print("NO PARAMS")
        return

    try:
        n = [int(x) for x in a]
    except ValueError as e:
        print("ValueError")
        return
    except Exception as e:
        print(type(e).__name__)
        return

    if len(n) < 2:
        print("TOO FEW PARAMS")
    elif len(n) > 2:
        print("TOO MANY PARAMS")
    else:
        print(sum(n))


if __name__ == '__main__':
    main()
