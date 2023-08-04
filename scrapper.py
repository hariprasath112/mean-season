from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import time, requests
global breaker
breaker=False
def main():
    query =input("Enter a search term below: ")
    driver= webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.imdb.com/")
    searchBar=driver.find_element("xpath",'//*[@id="suggestion-search"]')
    searchBar.send_keys(query)
    time.sleep(2)
    firstResult=driver.find_element("xpath",'/html/body/div[2]/nav/div[2]/div[1]/form/div[2]/div/div/div/ul/li[1]/a/div[2]/div[1]')
    firstResult.click()
    time.sleep(1)
    ratingsURL=driver.current_url.split("?")[0]
    ratingsURL+="ratings"
    try:
        driver.get(ratingsURL)
    except NoSuchElementException:
        print("Failed to GET. Connectivity issues.")
        main()
    time.sleep(2)
    try:
        sideArrow=driver.find_element('xpath',"/html/body/div[2]/main/div/section/div/section/div/div[1]/section[3]/div[2]/div[2]/div[3]")
        tempDict=sideArrow.location_once_scrolled_into_view
        time.sleep(2)
        try:
            sideArrow.click()
            sideArrow.click()
            sideArrow.click()
            time.sleep(1)
        except:
            pass
    except:
        print("Failed to GET. Invalid entry.")
        global breaker
        breaker=True
        driver.close()
    if (breaker!=True):
        try:
            source=driver.page_source
            soup=BeautifulSoup(source,'html.parser')
            seriesName=soup.find('h2',class_="sc-f794c697-10 htsAyt").text
            avgRating=soup.find('span', class_="sc-5931bdee-1 jUnWeS").text
            totalVoters=soup.find('div',class_="sc-5931bdee-3 dWymrF").text
            table=soup.find('table',class_="sc-8e832255-3 cAfagm ratings-heatmap__table").find_all('tr')
            dataList=[]
            for tr in table:
                dataList.append([td.text for td in tr.find_all('td')])
            print("___________________________________________________","\nName: ",seriesName,"\nAvg. Ratings: ",avgRating,"\tTot. Voters: ",totalVoters,"\n___________________________________________________")
            for i in range(len(dataList)):
                if (i!=0):
                    tempList=[eval(j) for j in dataList[i]]
                    print("Season ",i,":",round(sum(tempList)/len(dataList[i]),2))        
        except:
            print("Error parsing data")
        main()
    else:
        main()
main()
