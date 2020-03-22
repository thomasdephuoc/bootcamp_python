import getopt, sys, string

if sys.argv[1].isdigit:
    print("ERROR")
    sys.exit()

try: 
    max_size = int(sys.argv[2])
    output_list = []
    for word in sys.argv[1].split():
        if len(word) > max_size:
            output_list.append(word.translate(str.maketrans('', '', string.punctuation)))
except ValueError:
    print("ERROR")
    sys.exit()