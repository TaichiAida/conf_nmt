# The model of NMT

from __future__ import unicode_literals, print_function, division
from io import open
import unicodedata
import string
import re
import random

import torch
import torch.nn as nn
from torch import optim
import torch.nn.functional as F

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"{device}:{type(device)}")

SOS_token = 0
EOS_token = 1

class Lang:
    def __init__(self,name):
        self.name = name
        self.word2index = {}
        self word2count = {}
        self.index2word = {0:"SOS", 1:"EOS"}
        self.n_words = 2

    def addSentence(self,sentence):
        for word in sentence.split(" "):
            self.addWord(word)

    def addWord(self,word):
        if word not in self.word2index:
            self.word2index[word] = self.n_words
            self.word2count[word] = 1
            self.index2words[self.n_words] = word
            self.n_words += 1
        else:
            self.word2count[word] += 1
