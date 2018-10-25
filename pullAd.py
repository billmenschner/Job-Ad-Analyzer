#! Python3

# pullAd.py -- Asks users to paste address of job ad. Once pasted, determines
# the site of the ad, determines type of job, and pulls text description of job.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
from JobSites import *
from collections import Counter
from urllib.parse import urlparse

#User enters website, website is parsed, and website name is extracted
website = input('Paste the website of the job ad: ')
parsed_website = urlparse(website)
site_name = parsed_website.netloc.split('.')[1]

#Dictionary of job websites
job_websites = {'indeed': indeed, 'careerbuilder': careerbuilder,
                'simplyhired': simplyhired, 'dice': dice,
                'monster': monster, 'craigslist': craigslist,
                'ziprecruiter': ziprecruiter}

#Search for job website in dictionary and return code for extracting ad text.
#If site name is not in the dictionary, returns a message. Need to determine
#what happens besides the message if the website isn't recognized.
if site_name in job_websites:
    job_ad = job_websites[site_name](website)
else:
    print("""Oops, there was a problem. Either the website is not yet supported,
          or we don't recognize this as a website.""")
    
#Strip punctuation, make everything lowercase, remove new lines.

clean_job_ad = re.sub(r"""[,.;?!'@#$%&*"()/’:-]|\—|\" #Punctuation to remove.
                           """,
                           " ", #Replace with a single space.
                           job_ad, flags = re.VERBOSE).lower().replace('\n', ' ')

#Create list of words used in the ad and a list of words to exclude from
#analysis.

job_word_list = clean_job_ad.split(' ')
job_word_list = list(filter(None, job_word_list))

excluded_words = ('and', 'the', 'of', 'is', 'to', 'in', 'for', 'a', 'as', 'or',
                  'with', 'on', 'by', 'their', 'be', 'an', 'have', 'that',
                  'but', 'are')


#Create single-word list, eliminating articles and other superfluous words
single_word_list = [word for word in job_word_list if word not in excluded_words]

#Create double-word and triple-word lists.

doublet_list = []
word_index = 1
for word in job_word_list:
    if word_index < len(job_word_list):
        doublet = word + ' ' + job_word_list[word_index]
        doublet_list.append(doublet)
        word_index += 1

triplet_list = []
word_index = 1
for word in job_word_list:
    if word_index < len(job_word_list) - 1:
        triplet = word + ' ' + job_word_list[word_index] + ' ' + job_word_list[word_index + 1]
        triplet_list.append(triplet)
        word_index += 1
        
# Very basic word count list. This kind of works, but it would be better to not
#see words repeated. Also need to get rid of duplicate words. Also need to look
#into multi-word combos.
#for word in job_ad.split(' '):
#    print(word + ' = ' + str(job_ad.count(word)))
#    
#word_list = clean_job_ad.split(' ')
#
#d = Counter(word_list)
#
#df = pd.DataFrame(d, index=[0])
#df.head(10)

#print(Counter(single_word_list))