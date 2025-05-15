# PASS
import argparse


def print_error(message):
    print(f"ERROR: {message}!!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("message", nargs="?", default="")
    args = parser.parse_args()

    print("Welcome to my program")
    if args.message:
        print_error(args.message)
