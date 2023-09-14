"""
Main code
"""
import nltk

nltk.download("gutenberg")
nltk.download("punkt")


def select_next(sentence, n, corpus, random=False):
    dict_freq = {}
    for i in range(len(corpus) + 1 - n):
        ele = corpus[i : i + n]
        if sentence[-n + 1 :] == ele[: n - 1]:
            if ele[-1] not in dict_freq:
                dict_freq[ele[-1]] = 1
            else:
                dict_freq[ele[-1]] += 1
    if dict_freq:
        sort_dict = sorted(dict_freq.items(), key=lambda x: x[1], reverse=True)
        # print(sort_dict)
        return sort_dict[0][0]
    elif not dict_freq:
        pass


def finish_sentence(sentence, n, corpus, random=False):
    curr_sentence = sentence
    punk = [".", "?", "!"]
    while len(curr_sentence) < 10 and curr_sentence[-1] not in punk:
        new_token = select_next(sentence, n, corpus, random=False)
        curr_sentence.append(new_token)

    return curr_sentence


# if __name__ == "__main__":
# pylint: disable=no-value-for-parameter
#     add_cli()
