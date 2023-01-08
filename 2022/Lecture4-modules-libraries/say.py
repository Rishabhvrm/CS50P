import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])
    cowsay.cow("I'mma cow YO!!")
    cowsay.trex("I'mma T-REX YOOO!!")