import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--upper', action='store_true',
                        help='Convert text to uppercase')
    parser.add_argument('--lines', type=int, default=None,
                        help='Number of lines to copy')
    parser.add_argument('source', help='Source file name')
    parser.add_argument('destination', help='Destination file name')

    args = parser.parse_args()

    try:
        with open(args.source, 'r', encoding='utf-8') as src_file:
            with open(args.destination, 'w', encoding='utf-8') as dest_file:
                lines_copied = 0
                for line in src_file:
                    if args.lines is not None and lines_copied >= args.lines:
                        break
                    if args.upper:
                        line = line.upper()
                    dest_file.write(line)
                    lines_copied += 1

    except FileNotFoundError: # не нада
        pass


if __name__ == '__main__':
    main()
