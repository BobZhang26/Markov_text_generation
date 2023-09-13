"""
Main code
"""
import numpy as np


class ngramModel:
    def __init__(self) -> None:
        # initialize
        return self.p

    def train(self, encodings):
        pass

    def apply(self, encodings):
        pass

    def encodings(self):
        pass


# at each step choose the sngle most probable next word/token until it yields
def finish_sentence(sentence, n, corpus, randomize=False):
    """
    inputs:
        sentence  -> a sentence [list of tokens] that we're trying to build on
        n         -> [int], the length of n-grams to use for prediction
        corpus    -> a source corpus [list of tokens]
        randomize -> a flag indicating whether the process should be randomize [bool]

    return:
        finished_sentence -> a finished sentence [list of tokens]
    """

    pass


# if __name__ == "__main__":
# pylint: disable=no-value-for-parameter
#     add_cli()
