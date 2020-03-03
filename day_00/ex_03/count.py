def text_analyzer(text): 
    if text is None:
        text = input("What is the text to analyse?")

    nb_char = sum(1 for c in text if c.isalpha())
    nb_upper = sum(1 for c in text if c.isupper())
    nb_lower = sum(1 for c in text if c.islower())
    nb_punc = sum(1 for c in text if c == "!")
    nb_spaces = sum(1 for c in text if c == " ")
    print("The text contains", nb_char, "characters:\n-", nb_upper, "upper letters\n-", nb_lower, 
    "lower letters\n-", nb_punc, "punctuation marks\n-", nb_spaces, "spaces")