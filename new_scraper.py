from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests
# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

# Webdriver
browser = webdriver.Chrome("chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

scraped_data = []

# Define Exoplanet Data Scrapping Method
def scrape_dwarf_data(hyperlink):
     
        ## ADD CODE HERE ##
    try:
        page=requests.get(hyperlink)

        soup=BeautifulSoup(page.content, "html.parser")
        dwarf_stars_table=soup.find_all("table", attrs={"class":"wikitable sortable jquery-tablesorter"})
        temp_list=[]
        table_rows=dwarf_stars_table.find_all("tr")

        for rows in table_rows:
           table_col=rows.find_all("td")

           for col_data in table_col:
                 data=col_data.text.strip() 
                 temp_list.append(data)

           scraped_data.append(temp_list)
        
        stars_data=[]

        for i in range(0, len(scraped_data)):
              Dwarf_names=scraped_data[i][1]
              Distance=scraped_data[i][5]
              Mass=scraped_data[i][7]
              Radius=scraped_data[i][8]

              required_data=[Dwarf_names, Distance, Mass, Radius]
              stars_data.append(required_data)
    except:    
     # Calling Method    
        time.sleep(1)
        scrape_dwarf_data()

# Define Header
headers = ["Dwarf Name", "Distance", "Mass", "Radius"]

# Define pandas DataFrame   
star_df_1=pd.DataFrame(scraped_data, columns=headers)


# Convert to CSV
star_df_1.to_csv('scraped_data.csv', index=True, index_label="id")

    


