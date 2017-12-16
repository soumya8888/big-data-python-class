
# coding: utf-8

# In[259]:

import numpy as np
from bitarray import bitarray
import random


# In[260]:

## define some helper methods

# @param ca,cb: hashing coefficients
# @param val: value to be hashed
# @param prime: size of hash table
# @return: hash 
def my_hash(ca, cb, val, prime): return (a*val + b) % prime

# set True to @position in @bitar:bitarray
def update_bloom(position, bitarr): bitarr[position] = 1

# find next prime number
def find_next_prime(n): return find_prime_in_range(n, 2*n)

def find_prime_in_range(a, b):
    for p in range(a, b):
        for i in range(2, p):
            if p % i == 0:
                break
        else:
            return p
    return None

# test
print find_next_prime(19+1)


# In[261]:

# example list of spam emails
email_list = ["a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "could", "did", "do", "does", "doing", "down", "during", "each", "few", "for", "from", "further", "had", "has", "have", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "it", "it's", "its", "itself", "let's", "me", "more", "most", "my", "myself", "nor", "of", "on", "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "she", "she'd", "she'll", "she's", "should", "so", "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "we", "we'd", "we'll", "we're", "we've", "were", "what", "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "would", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves"]


# In[262]:

# initialise bloom filter
bloom_filter = bitarray(hashtable_size)
# set all bits to 0
bloom_filter[:] = False
print "Bloom Filter:", bloom_filter


# In[263]:

# calculate unicode sum of characters for every email-address
email_unicode_sum_list = [sum([ord(char) for char in email]) for email in email_list]
email_unicode_sum_list


# In[264]:

#The coefficients a and b are randomly chosen integers less than the maximum value of x. 
#c is a prime number slightly bigger than the maximum value of x.

# h_x = (a*x + b)%c

# choose 2 random numbers up to maximum unicode value 
# and set them to be hashing coefficients
a = random.randint(1, max(email_unicode_sum_list)-1)
b = random.randint(2, max(email_unicode_sum_list)-1)

print a,b


# In[265]:

# since we have fixed size of input, the hashtable could have 1.0 load factor
# yet, 0.75 load has much less colisions
# choose next prime number from the number of elements in email list
hashtable_size = find_next_prime(int(round(len(email_unicode_sum_list)*1.25)))
hashtable_size


# In[266]:

# hash emails
hash_list = [my_hash(a,b,unicode_sum,hashtable_size) for unicode_sum  in email_unicode_sum_list]


# In[267]:

# assign hash_values & unicode-sums to emails
[(email,"->",unicode_sum, "->", hashp) for email, unicode_sum, hashp in zip(email_list, email_unicode_sum_list, hash_list)]


# In[269]:

# update bloom filter
[update_bloom(index, bloom_filter) for index in hash_list]
# check updated bloom filter
bloom_filter


# In[271]:

## now do some tests
# for every email in the list check if it has already been seen by bloom filter
for email in email_list:
    if bloom_filter[my_hash(a,b,sum([ord(char) for char in email]),hashtable_size)] == True: 
        print email, "has ALREADY been seen";
    else:
        print email, "has NOT been seen";


# In[ ]:



