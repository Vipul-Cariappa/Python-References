import sys


if len(sys.argv) > 1:
    args = sys.argv[1:]

    if args[0] == "add":
        print("\n", "Instruction Given to Add: ", args[1:])
        print(sum(int(i) for i in args[1:]))
    else:
        raise TypeError("This Script Only Sums Numbers.")
