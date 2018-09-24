import pandas as pd
import bs4 as bs
import urllib.request
sauce = urllib.request.urlopen('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html').read()
soup = bs.BeautifulSoup(sauce, 'lxml')
first_stage = soup.find_all('span', class_ = 'short-desc')

explanation = [] 
lies = []
date = []
url = []
for asshat in first_stage:
    d = asshat.find('strong').text[0:-1]+', 2017'
    date.append(d)
    lie = asshat.contents[1][1:-2]
    lies.append(lie)
    ex = asshat.find('span', class_ = 'short-truth').text
    explanation.append(ex)
    link = asshat.find('a').get('href')
    url.append(link)
      
Trump = pd.DataFrame()
Trump['Date'] = date
Trump['Lies'] = lies
Trump['Explanation'] = explanation
Trump['URL'] = url

#Trump.to_csv("Trump's_Opinion.csv") #This is to convert the dataframe into a csv file. To use it just uncomment the line.