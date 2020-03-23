import sys, getopt

morse = {
        # Letters
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        # Numbers
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        }

for i in range(1, len(sys.argv)):
    for word in sys.argv[i].split():
        if word.isalnum() == False:
            print("ERROR")
            sys.exit()
first = True
for i in range(1, len(sys.argv)):
    for word in sys.argv[i].split():
        if first == True:
            first = False
        else:
            print("/ ", end = "")
        first_letter = True
        for letter in word:
            print(f'{morse[letter.lower()]}', end = " ")