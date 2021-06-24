import random
import sys


def main():
    x = [random.randint(1, 5)
         for x in range(10)]
    print(x)
if __name__ =="__main__":
    sys.exit(main())