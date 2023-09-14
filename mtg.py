"""
Main code
"""
import nltk
import random

nltk.download("gutenberg")
nltk.download("punkt")


def select_next(sentence, n, corpus, randomize):
    dict_freq = {}
    for i in range(len(corpus) + 1 - n):
        ele = corpus[i : i + n]
        if sentence[-n + 1 :] == ele[: n - 1]:
            if ele[-1] not in dict_freq:
                dict_freq[ele[-1]] = 1
            else:
                dict_freq[ele[-1]] += 1

    # frequency exist and deterministic
    if dict_freq and randomize == False:
        sort_dict = sorted(dict_freq.items(), key=lambda x: x[1], reverse=True)
        return sort_dict[0][0]
    # frequency exist and stochastic
    elif dict_freq and randomize == True:
        print(dict_freq)
        weight = [val[1] for val in dict_freq]
        return random.choices(dict_freq, weight, k=1)

    elif not dict_freq:
        # execute back off until yield frequency
        return select_next(sentence, n - 1, corpus, randomize)


def finish_sentence(sentence, n, corpus, randomize):
    curr_sentence = sentence
    punk = [".", "?", "!"]
    while len(curr_sentence) < 10 and curr_sentence[-1] not in punk:
        new_token = select_next(curr_sentence, n, corpus, randomize)
        curr_sentence.append(new_token)

    return curr_sentence


# if __name__ == "__main__":
# pylint: disable=no-value-for-parameter
#     add_cli()
