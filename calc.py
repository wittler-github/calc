"""calc.py: A simple Python calculator."""

import sys

if __name__ == '__main__':
   print(sum(map(float, sys.argv[1:])))
