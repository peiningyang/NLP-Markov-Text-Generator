"""Markov Text Generator.

Patrick Wang, 2021

Resources:
Jelinek 1985 "Markov Source Modeling of Text Generation"
"""

import nltk

from mtg import finish_sentence


def test_generator():
    """Test Markov text generator."""
    corpus = nltk.corpus.gutenberg.raw('austen-sense.txt')
    corpus = nltk.word_tokenize(corpus.lower())

    words = finish_sentence(
        ['she', 'was', 'not'],
        3,
        corpus,
        deterministic=True,
    )
    assert words == ['she', 'was', 'not', 'in', 'the', 'world', '.']


if __name__ == "__main__":
    test_generator()
