#! Python3

# JobSites.py -- Directory of job listing websites.

import requests, bs4
from collections import Counter

#Function for if the website entered is from Indeed. Indeed shows ads inline
#and has a separate page for the ad. This method should send all ads to the
#separate page.

def indeed(website):
    if 'vjk=' in website:
        split_address = website.split('vjk=')
        website = 'https://www.indeed.com/viewjob?jk=' + split_address[1]
    ad_pull = requests.get(website)
    text_pull = bs4.BeautifulSoup(ad_pull.text, 'lxml')
    return text_pull.find('div', 'jobsearch-JobComponent-description icl-u-xs-mt--md').getText()
#    return text_pull.find('div', 'vjs-desc').getText()

#Function for careerbuilder ad. Currently, careerbuilder uses the same div class
#for the job description and job requirements. The requirements section is just:
#as important, so it needs to be included.
    
def careerbuilder(website):
    ad_pull = requests.get(website)
    text_pull = bs4.BeautifulSoup(ad_pull.text, 'lxml')
    #Need to find all the descriptor class tags
    job_descriptor = text_pull.find_all('div', 'description')
    consolidated_descriptor = ''
    #Put all the descriptors together so they can be returned.
    for description in job_descriptor:
        consolidated_descriptor += description.getText()
    return consolidated_descriptor

#The simplyhired website currently puts the job descriptions in other windows.
#Can't pull the job description from the main website. The specific location 
#of the description needs to be cut from the web address and added to the 
#new address, where the description can be pulled.

def simplyhired(website):
    if 'job=' in website:
        split_address = website.split('job=')
        website = 'https://www.simplyhired.com/job/' + split_address[1]
    ad_pull = requests.get(website)
    text_pull = bs4.BeautifulSoup(ad_pull.text, 'lxml')
    return text_pull.find('div', 'viewjob-description').getText()

#Dice.com function.

def dice(website):
    ad_pull = requests.get(website)
    text_pull = bs4.BeautifulSoup(ad_pull.text, 'lxml')
    return text_pull.find('div', 'highlight-black').getText()

#Monster.com function.

def monster(website):
    if 'jobid' in website:
        split_address = website.split('jobid=')
        website = 'https://job-openings.monster.com/' + split_address[1]
    ad_pull = requests.get(website)
    text_pull=bs4.BeautifulSoup(ad_pull.text, 'lxml')
    return text_pull.find('div', 'details-content is-preformated').getText()

#Craigslist function.

def craigslist(website):
    ad_pull = requests.get(website)
    text_pull = bs4.BeautifulSoup(ad_pull.text, 'lxml')
    return text_pull.find('section', id='postingbody').getText()
    
#Glassdoor function.
    
#ZipRecruiter function.

def ziprecruiter(website):
    ad_pull = requests.get(website)
    text_pull = bs4.BeautifulSoup(ad_pull.text, 'lxml')
    return text_pull.find('div', 'job_content').getText()