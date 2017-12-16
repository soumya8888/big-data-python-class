#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
from textblob import TextBlob as tb
import glob, os
import sys

reload(sys)
sys.setdefaultencoding("latin-1")

def tf(word, blob):
	return (float)(blob.words.count(word)) / (float)(len(blob.words))

def n_containing(word, bloblist):
	return (float)(sum(1 for blob in bloblist if word in blob))

def idf(word, bloblist):
	return math.log(len(bloblist) / (float)(1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
	return (float)((float)(tf(word, blob)) * (float)(idf(word, bloblist)))

folder = "C:/Users/srbal/OneDrive/Documents/GitHub/big-data-python-class/Homeworks/Homework5/SherlockHolmesBooks/"
os.chdir(folder)
files = glob.glob("*.txt") # Makes a list of all files in folder
bloblist = []
for file1 in files:
    with open (file1,'r') as f:
		data = f.read() # Reads document content into a string
		document = tb(data.decode("latin-1")) # Makes TextBlob object
		bloblist.append(document)
	
for i, blob in enumerate(bloblist):
    print("Top words in document {}".format(i + 1))
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for word, score in sorted_words[:3]:
        print("Word: {}, TF-IDF: {}".format(word, round(score, 5)))
		
			