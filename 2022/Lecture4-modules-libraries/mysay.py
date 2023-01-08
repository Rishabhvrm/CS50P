import sys

from sayings import goodbye

if len(sys.argv) == 2:
    print(goodbye(sys.argv[1]))