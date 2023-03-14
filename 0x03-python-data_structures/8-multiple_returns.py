#!/usr/bin/python3
# returns a tuple with the length of a string and its first character
def multiple_returns(sentence):
    len_sent = len(sentence)
    if sentence == "":
        return (0, None)
    return (len_sent, sentence[0])
