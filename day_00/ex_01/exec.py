import getopt, sys

fullCmdArguments = sys.argv

argumentList = fullCmdArguments[1:]

for currentArgument in reversed(argumentList):
    currentArgument = currentArgument [::-1]
    currentArgument = currentArgument.swapcase()
    print(currentArgument, end= ' ')
