import sys
import re


def main():
    for line in sys.stdin:
        print(line.replace("[SPACE]", " "))


if __name__ == "__main__":
    main()
