#! Python3

# pullAd.py -- Asks users to paste address of job ad. Once pasted, determines
# the site of the ad, determines type of job, and pulls text description of job.

import requests, bs4

#Have the user enter the website.
website = input('Paste the website of the job ad: ')
#TODO: Include a check that a website was entered.

#Function for if the website entered is from Indeed. Presently, Indeed uses
#just the one div class for the job ad description.

def indeed(website):
    adPull = requests.get(website)
    textPull = bs4.BeautifulSoup(adPull.text, 'lxml')
    return textPull.find('div', 'jobsearch-JobComponent-description icl-u-xs-mt--md').getText()

#Function for careerbuilder ad. Currently, careerbuilder uses the same div class
#for the job description and job requirements. The requirements section is just:
#as important, so it needs to be included.
    
def careerbuilder(website):
    adPull = requests.get(website)
    textPull = bs4.BeautifulSoup(adPull.text, 'lxml')
    #Need to find all the descriptor class tags
    jobDescriptor = textPull.find_all('div', 'description')
    consolidatedDescriptor = ''
    #Put all the descriptors together so they can be returned.
    for description in jobDescriptor:
        consolidatedDescriptor += description.getText()
    return consolidatedDescriptor
    

if 'indeed' in website:
    jobAd = indeed(website)
elif 'careerbuilder' in website:
    jobAd = careerbuilder(website)

print(jobAd)