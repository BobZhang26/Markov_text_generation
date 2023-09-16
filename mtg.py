"""
Main code
"""

import random

# nltk.download("gutenberg")
# nltk.download("punkt")


def store_freq(sentence, n, corpus):
    """
    this function stores n_gram combination of the given sentence as key and
    their frequency in the corpus as value

    return -> dictionary: dict_freq
    """
    dict_freq = {}
    for i in range(len(corpus) + 1 - n):
        ele = corpus[i : i + n]
        if sentence[-n + 1 :] == ele[: n - 1]:
            if ele[-1] not in dict_freq.keys():
                dict_freq[ele[-1]] = 1
            else:
                dict_freq[ele[-1]] += 1
    # print(dict_freq)
    return dict_freq


def random_res(dict_freq, randomnize):
    """
    this function predicts the next possible output word in either deterministic
    or stochastic situation

    return: str
    """
    if randomnize == False:
        # print("deterministic running")
        sort_dict = sorted(dict_freq.items(), key=lambda x: x[1], reverse=True)
        return sort_dict[0][0]
    else:
        # print("stochastic running")
        weight = [val for val in dict_freq.values()]
        ls = [e for e in dict_freq.keys()]
        return random.choices(ls, weight, k=1).pop()


def unigram(corpus):
    dict_token = {}
    for i in range(len(corpus)):
        if corpus[i] not in dict_token.keys():
            dict_token[corpus[i]] = 1
        else:
            dict_token[corpus[i]] += 1
    return dict_token


def select_next(sentence, n, corpus, randomize):
    """
    this function gathers all necessary sub-functions to select next possible word
    return: next -> str
        otherwise recursive select_next with 'n-1' until yield
    """
    # stop condition if n_gram less than 1 (inclusive)
    if n < 1:
        return  # "index out of range, model failed!"
    elif n == 1:
        dict_token = unigram(corpus)
        next_token = random_res(dict_token, randomize)
        return next_token

    # store possible next and their frequency
    dict_freq = store_freq(sentence, n, corpus)

    # next word in deterministic and stochastic situations
    if dict_freq:
        next_token = random_res(dict_freq, randomize)
        return next_token

    else:  # not dict_freq
        # print("backoff on, try n = ", n - 1)
        # execute back off until yield frequency, break at stop condition
        return select_next(sentence, n - 1, corpus, randomize)


def finish_sentence(sentence, n, corpus, randomize):
    """
    this function will give a complete sentence output given a part of sentence
    return: curr_sentence -> list
    """
    curr_sentence = sentence
    punk = [".", "?", "!"]
    while len(curr_sentence) < 10 and curr_sentence[-1] not in punk:
        new_token = select_next(curr_sentence, n, corpus, randomize)
        curr_sentence.append(new_token)
    return curr_sentence


# if __name__ == "__main__":
# pylint: disable=no-value-for-parameter
#     add_cli()
# sentence = ["she", "was", "not"]
# n = 3
# corpus = nltk.word_tokenize(nltk.corpus.gutenberg.raw("austen-sense.txt").lower())

# fs = finish_sentence(sentence, n, corpus, randomize=True)
# print(fs)
