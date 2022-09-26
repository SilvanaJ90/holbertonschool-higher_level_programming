#!/usr/bin/python3
def multiple_returns(sentence):
    res = int(len(sentence))
    if sentence == "":
        return 0, None
    return res, sentence[:1]
