#!/usr/bin/python3
def text_indentation(text):
    """prints text with two new lines after each ".", "?", and ":"
    argument:
        text (string): text to print
    raises:
        TypeError: when the text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    st = 0
    while st < len(text) and text[st] == ' ':
        st += 1
    while st < len(text):
        print(text[st], end="")
        if text[st] == "\n" or text[st] in ".?:":
            if text[st] in ".?:":
                print("\n")
            st += 1
            while st < len(text) and text[st] == ' ':
                st += 1
            continue
        st += 1
