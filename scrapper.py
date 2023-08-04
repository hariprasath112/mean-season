from selenium import webdriver
from bs4 import BeautifulSoup
import time, requests
print("Enter a search term. Series only, no Movies.")
query =input(">>")
driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.imdb.com/")
searchBar=driver.find_element("xpath",'//*[@id="suggestion-search"]')
searchBar.send_keys(query)
time.sleep(2)
firstResult=driver.find_element("xpath",'/html/body/div[2]/nav/div[2]/div[1]/form/div[2]/div/div/div/ul/li[1]/a/div[2]/div[1]')
firstResult.click()
time.sleep(2)
ratingsURL=driver.current_url.split("?")[0]
ratingsURL+="ratings"
driver.get(ratingsURL)
time.sleep(3)
sideArrow=driver.find_element('xpath',"/html/body/div[2]/main/div/section/div/section/div/div[1]/section[3]/div[2]/div[2]/div[3]")
tempDict=sideArrow.location_once_scrolled_into_view
time.sleep(3)
try:
    sideArrow.click()
    sideArrow.click()
    sideArrow.click()
except:
     pass
time.sleep(3)
try:
    source=driver.page_source
    soup=BeautifulSoup(source,'html.parser')
    avgRating=soup.find('span', class_="sc-5931bdee-1 jUnWeS").text
    totalVoters=soup.find('div',class_="sc-5931bdee-3 dWymrF").text
    table=soup.find('table',class_="sc-8e832255-3 cAfagm ratings-heatmap__table").find_all('tr')
    seasonNumber=0
    dataList=[]
    for tr in table:
        dataList.append([td.text for td in tr.find_all('td')])
    for i in range(len(dataList)):
        if (i!=0):
            tempList=[eval(j) for j in dataList[i]]
            print("Season ",i,":",round(sum(tempList)/len(dataList[i]),2))        
except:
    pass
