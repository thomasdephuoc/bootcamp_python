import getopt, sys

try:
    argument = int(sys.argv[1])
except ValueError:
    print("Error")
    sys.exit()
except IndexError:
    print("Error")
    sys.exit()

if len(sys.argv) > 2:
    print("Error")
    sys.exit()

if argument == 0:
    print("I'm Zero.")
elif argument % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
