import requests
from bs4 import BeautifulSoup 


def new_arXiv_papers():
    """
    Searches through the arXiv website, extracts all new submissions, and returns those that satisfy certain key words :-)
    
    Author: Houda Haidar (h.haidar2 AT newcastle.ac.uk)
    Date: 21/01/23
    
    """
    
    #define url
    URL = "https://arxiv.org/list/astro-ph.GA/new" #only looks for new submissions
    #extract page
    page = requests.get(URL)

    #get status of page (200 is GOOD, 404 is not found)
    status = page.status_code
    if status == 200:
        print("Ready to extract data from: "+str(URL)) ; print(" ")
    else:
        raise ValueError(str(status)+" Failed to load website! ")
    
    #get text version of page
    txt = page.text

    #use BeautifulSoup package to extract info from html file (ie website)
    soup = BeautifulSoup(page.content, "html.parser") #makes sure parser is for html
    

    page_title = soup.title.text
    print("Page title: ", page_title)

    # Extract head of page
    page_head = soup.head

    # Extract body of page
    page_body = soup.body

    # Extract head of page
    page_head = soup.head
    
    
    #look for id "content" ps: this is specific for arXiv website & might vary for others :-).
    results = soup.find(id="content") 
    #extract list of all title submissions
    #again,  class_="list-title mathjax"  is specific to arXiv
    list_titles = results.find_all("div", class_="list-title mathjax" )
    print("Found "+str(len(list_titles))+" new submissions!! \U0001F601") ; print("  ")

    #these are my keys words I am interested in, I also add variations of them bc code not too sophisticated for now
    look_for = ["AGN","AGNs","active galactic nuclei", "Active Galacti Nuclei",\
                "BH","BHs","black hole","black holes",\
                "SMBH","SMBHs", "supermassive black hole","supermassive black holes",\
                "JWST", "James Webb Space Telescope", "james webb space telescope",\
               ]

    #now loop over the titles & find the ones that contain the words above!
    print("New submissions that might BH related....") ; print(" ")
    new_BH_papers = []
    for t in list_titles:
        title = t.text
        for key in look_for:
            if key in title:
                new_BH_papers.append(title)
                print(title)
                
              
    if len(new_BH_papers) == 0:
        print(" Sorry! Today's not your lucky day! Try again tomorrow \U0001F601")
                
    #to do: run everyday, set sleeper & set desktop notifications when new papers are in :-).
                
                
    return
    

new_arXiv_papers()
