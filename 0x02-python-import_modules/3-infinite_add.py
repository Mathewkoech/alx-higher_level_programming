#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    args = [int(arg) for arg in args]
    result = sum(args)
    print(result)
