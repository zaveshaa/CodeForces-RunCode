import argparse
import sys


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--count', action='store_true')
    p.add_argument('--num', action='store_true')
    p.add_argument('--sort', action='store_true')
    p.add_argument('file', nargs='?', default=None)
    a = p.parse_args()

    if not a.file:
        print("ERROR")
        return

    try:
        with open(a.file, 'r') as f:
            d = f.readlines()
    except FileNotFoundError:
        print("ERROR")
        return

    if a.sort:
        d.sort()

    c = 0
    for i, l in enumerate(d):
        o = ''
        if a.num:
            o += f'{i} '
        o += l.rstrip('\n')
        print(o)
        c += 1

    if a.count:
        print(f'rows count: {c}')


if __name__ == '__main__':
    main()
