import random
import sys


def main():
    l = random.choices(range(10), k=10)
    print(l)
    print(6 not in l)





if __name__ == "__main__":
    sys.exit(main())