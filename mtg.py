"""
Main code
"""
import nltk

nltk.download("gutenberg")
nltk.download("punkt")


def select_next(sentence, n, corpus, random=False):
    for i in range(len(text) + 1 - n):
        ele = corpus[i : i + n]
        if sen[-1] == ele[: n - 1]:
            if ele[-1] not in dict_freq:
                dict_freq[ele[-1]] = 1
            else:
                dict_freq[ele[-1]] += 1
    dict_freq = sorted(dict_freq.items(), key=lambda x: x[1])
    return dict_freq


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


corpus = nltk.word_tokenize(nltk.corpus.gutenberg.raw("austen-sense.txt").lower())
sentence = ["I"]
n = 2
select_next(sentence, n, corpus, random=False)

# if __name__ == "__main__":
# pylint: disable=no-value-for-parameter
#     add_cli()
