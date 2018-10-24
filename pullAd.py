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

#User enters websites
website = input('Paste the website of the job ad: ')

parsed_website = urlparse(website)
print(parsed_website)
craigslist_key = re.compile(r'.*?/.craigslist/.com')
if craigslist_key.match(parsed_website.netloc):
    print(True)
else:
    print(False)

job_websites = {'www.indeed.com': indeed, 'www.careerbuilder.com': careerbuilder,
                'www.simplyhired.com': simplyhired, 'www.dice.com': dice,
                'www.monster.com': monster, craigslist: craigslist,
                'ziprecruiter': ziprecruiter}

if parsed_website.netloc in job_websites:
    job_ad = job_websites[parsed_website.netloc](website)
elif 'craigslist' in website:
    job_ad = craigslist(website)
else:
    print("""Oops, there was a problem. Either the website is not yet supported,
          or we don't recognize this as a website.""")

##Determines website and pulls ad text from it.
#if 'indeed' in website:
#    job_ad = indeed(website)
#elif 'careerbuilder' in website:
#    job_ad = careerbuilder(website)
#elif 'simplyhired' in website:
#    job_ad = simplyhired(website)
#elif 'dice' in website:
#    job_ad = dice(website)
#elif 'monster' in website:
#    job_ad = monster(website)
#elif 'craigslist' in website:
#    job_ad = craigslist(website)
#elif 'ziprecruiter' in website:
#    job_ad = ziprecruiter(website)
    
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



#single_word_list = re.sub(r"""\band\b|\bthe\b|\bof\b|\bis\b|\bto\b|\bin\b|
#    \bfor\b|\ba\b|\bwith\b|\ban\b|\ball\b|\bthat\b|\bas\b|\bit\b|\bits\b|
#    \bon\b|\bat\b""",
#                     " ",
#                     clean_job_ad, flags = re.VERBOSE).split(' ')

#Create double-word and triple-word lists.

doublet_list = []
word_index = 1
for word in job_word_list:
    if word_index < len(job_word_list):
        doublet = word + ' ' + job_word_list[word_index]
        doublet_list.append(doublet)
        word_index += 1
#
#
#print(job_word_list)
    

   
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