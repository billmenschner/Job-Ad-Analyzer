#! Python3

# pullAd.py -- Asks users to paste address of job ad. Once pasted, determines
# the site of the ad, determines type of job, and pulls text description of job.

import JobSites
from collections import Counter

#User enters websites
website = input('Paste the website of the job ad: ')

#Determines website and pulls ad text from it.
if 'indeed' in website:
    job_ad = indeed(website)
elif 'careerbuilder' in website:
    job_ad = careerbuilder(website)
elif 'simplyhired' in website:
    job_ad = simplyhired(website)
elif 'dice' in website:
    job_ad = dice(website)
elif 'monster' in website:
    job_ad = monster(website)
elif 'craigslist' in website:
    job_ad = craigslist(website)
elif 'ziprecruiter' in website:
    job_ad = ziprecruiter(website)


# Very basic word count list. This kind of works, but it would be better to not
#see words repeated. Also need to get rid of duplicate words. Also need to look
#into multi-word combos.
#for word in job_ad.split(' '):
#    print(word + ' = ' + str(job_ad.count(word)))
#    
#word_list = job_ad.split(' ')
#
#print(Counter(word_list).most_common(5))