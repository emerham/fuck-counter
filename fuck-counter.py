#!/bin/env python
import requests, json
from bs4 import BeautifulSoup

def count_words(words, dict):
    """Count the number of words and add them to a dictionary.
    """
    if words[-1] in ['.', ',', '?', '!']:
        words = words[0:len(words) - 1]
    
    if words in dict:
        dict[words] += 1
    else:
        dict.update({words: 1})
    return dict

website = requests.get("https://www.mcsweeneys.net/articles/oh-my-fucking-god-get-the-fucking-vaccine-already-you-fucking-fucks")
data = website.text
soup = BeautifulSoup(data, "html.parser")

# Tokenize the text for the site.
web_body_tokens = soup.body.text.split()

# Create an empty dictionary
fucking_counter = {}

for word in web_body_tokens:
    word = word.lower()
    if 'fuck' in word:
        count_words(word, fucking_counter)
    elif 'shit' in word:
        count_words(word, fucking_counter)

print(json.dumps(fucking_counter, indent=4, sort_keys=True))
