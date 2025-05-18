import os
import sys
from collections import defaultdict


def get_size(path):
    total = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            try:
                total += os.path.getsize(fp)
            except Exception as e:
                print(f"{fp}: {e}")
    return total


def format_size(size_bytes):
    units = ['Байт', 'КБ', 'МБ', 'ГБ']
    index = 0
    while size_bytes >= 1024 and index < len(units) - 1:
        size_bytes /= 1024
        index += 1
    return f"{round(size_bytes)}{units[index]}"


def main(start_path):
    folder_sizes = []

    for entry in os.scandir(start_path):
        if entry.is_dir():
            size = get_size(entry.path)
            folder_sizes.append((entry.path, size))

    folder_sizes.sort(key=lambda x: x[1], reverse=True)

    for path, size in folder_sizes[:10]:
        print(f"{os.path.basename(path):<35} - {format_size(size)}")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(1)

    start_path = sys.argv[1]
    main(start_path)
