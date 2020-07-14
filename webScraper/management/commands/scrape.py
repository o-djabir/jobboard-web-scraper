'''
Created on Jul 14, 2020

@author: amiwill
'''
from django.core.management.base import BaseCommand

import requests
from bs4 import BeautifulSoup

from webScraper.models import Offre

# function to get the url of the pages we want to scrape from indeed
def get_all_URLs_indeed(URL):
    urls = []
    urls.append(URL)
    newURL = ""
    for i in range(10, 30, 10):
        newURL = URL+"&start="+str(i)
        urls.append(newURL)
    urls.reverse()
    return (urls)

# function to get the url of the pages we want to scrap from letudiant 
def get_all_URLs_letudiant():
    urls = []
    urls.append("https://jobs-stages.letudiant.fr/offre-alternance/offres/domaines-242/region-ile-de-france/page-2.html")
    urls.append("https://jobs-stages.letudiant.fr/offre-alternance/offres/domaines-242/region-ile-de-france.html")
    return (urls)

# function to turn an array of urls into soups
def all_soups(URLs):
    soups_array = []
    for url in URLs:
        # requesting the page from the URL
        page = requests.get(url)
        # parsing the page to read it
        soup = soup = BeautifulSoup(page.text, "html.parser")
        soups_array.append(soup)
    return (soups_array)

# function to extract all job titles from indeed, and when they were posted
def get_job_titles_indeed(soup):
    titles = []
    for div in soup.find_all(name="div", attrs={"class":"row"}):
        _ = ""
        for a in div.find_all(name="a", attrs={"data-tn-element":"jobTitle"}):
            _ = a["title"]
        
        for div1 in div.find_all(name="div", attrs={"class": "result-link-bar"}):
            for span in div1.find_all(name = "span", attrs={"class":"date"}):
                _ = _ + ", " + span.text.strip()
                titles.append(_)
    titles.reverse()
    return (titles)

# function to extract all job titles from letudiant
def get_job_titles_letudiant(soup):
    titles = []
    for div in soup.find_all(name="div", attrs={"class":"c-search-result__main"}):
        for a in div.find_all(name="a", attrs={"class":"c-search-result__title"}):
            titles.append(a.text.strip())
    titles.reverse()        
    return (titles)

# function to get all the company names from indeed
def get_company_names_indeed(soup):
    companies = []
    for span in soup.find_all(name="span", attrs={"class":"company"}):
        if len(span.text.strip()) > 0:
            companies.append(span.text.strip())
        else:    
            for a in span.find_all(name="a", attrs={"data-tn-element":"companyName"}):
                companies.append(a.text.strip())
    companies.reverse()
    return(companies)  

# function to get all the company names from letudiant
def get_company_names_letudiant(soup):
    _ = []
    for div in soup.find_all(name="div", attrs={"class":"c-search-result__secondary-information__item"}):
        for span in div.find_all(name="span"):
            _.append(span.text.strip()) 
    companies = []
    for i in range(0, len(_), 2):
        companies.append(_[i]) 
    companies.reverse()
    return (companies) 

# function to extract all links from indeed 
def get_links_indeed(soup):
    links = []
    for div in soup.find_all(name="div", attrs={"class":"row"}):
        for a in div.find_all(name="a", attrs={"data-tn-element":"jobTitle"}):
            link = "https://www.indeed.fr" + a["href"]
            links.append(link)
    links.reverse()
    return (links) 

# function to extract all links from letudiant 
def get_links_letudiant(soup):
    links = []
    for div in soup.find_all(name="div", attrs={"class":"c-search-result__main"}):
        for a in div.find_all(name="a", attrs={"class":"c-search-result__title"}):
            links.append("https://jobs-stages.letudiant.fr" + a["href"])
    links.reverse()
    return (links)


class Command(BaseCommand):
    help = 'collect alternance job postings'
    
    def handle(self, *args, **options):
        
        # the URLs for the first 2 pages from letudiant
        ALL_URLS_LETUDIANT = get_all_URLs_letudiant()
        
        for soup1 in all_soups(ALL_URLS_LETUDIANT):
            job_titles = get_job_titles_letudiant(soup1)
            company_names = get_company_names_letudiant(soup1)
            all_links = get_links_letudiant(soup1)
            
            for j in range(len(job_titles)):
                # create the job posting from letudiant
                try:
                    job_t = job_titles[j]
                    company_n = company_names[j]
                    job_l = all_links[j]
                    
                    Offre.objects.create(
                        job_title = job_t,
                        company_name = company_n,
                        job_link = job_l,
                        jobboard = "jobs-stages.létudiant.fr"   
                    )
                    print('%s ajouté' % (job_t))
                except:
                    print('%s existe déjà' % (job_t))
            
        self.stdout.write("Scraping completed for letudiant!")
        
        # the URLs for the first 3 pages from indeed
        url_indeed = "https://www.indeed.fr/emplois?q=alternance+informatique&l=%C3%8Ele-de-France&sort=date"
        ALL_URLS_INDEED = get_all_URLs_indeed(url_indeed)
        
        for soup in all_soups(ALL_URLS_INDEED):
            job_titles = get_job_titles_indeed(soup)
            company_names = get_company_names_indeed(soup)
            all_links = get_links_indeed(soup)
            
            for i in range(len(job_titles)):
                # create the job posting from indeed
                try:
                    job_t = job_titles[i]
                    company_n = company_names[i]
                    job_l = all_links[i]
                    
                    Offre.objects.create(
                        job_title = job_t,
                        company_name = company_n,
                        job_link = job_l,
                        jobboard = "indeed.fr"  
                    )
                    print('%s ajouté' % (job_t))
                except:
                    print('%s existe déjà' % (job_t))
            
        self.stdout.write("Scraping completed for indeed!")                
