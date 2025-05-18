import zipfile
import json
import sys


def main():
    count = 0
    with zipfile.ZipFile('input.zip', 'r') as zfile:
        for file_info in zfile.infolist():
            if file_info.filename.endswith('.json'):
                try:
                    with zfile.open(file_info) as f:
                        data = json.load(f)
                        if data.get("city") == "Москва":
                            count += 1
                except Exception as e:
                    print(f"{file_info.filename}: {e}", file=sys.stderr)
    print(count)


if __name__ == "__main__":
    main()
