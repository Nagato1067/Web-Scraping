import pandas as pd
import bs4 as bs
import urllib.request
source = urllib.request.urlopen('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html').read()
soup = bs.BeautifulSoup(source, 'lxml')
first_stage = soup.find_all('span', class_ = 'short-desc')

explanation = [] 
lies = []
date = []
url = []
for orange in first_stage:
    d = orange.find('strong').text[0:-1]+', 2017'
    date.append(d)
    lie = orange.contents[1][1:-2]
    lies.append(lie)
    ex = orange.find('span', class_ = 'short-truth').text
    explanation.append(ex)
    link = orange.find('a').get('href')
    url.append(link)
      
Trump = pd.DataFrame()
Trump['Date'] = date
Trump['Lies'] = lies
Trump['Explanation'] = explanation
Trump['URL'] = url

# This can be done in another way, The way DataSchool completed the task.


#data = []
#for trump in first_stage:
#    date = trump.find('strong').text[:-1]+ ', 2017'
#   lie = trump.contents[1][1:-2]
#    explanation = trump.find('span', class_ = 'short-truth').text # OR explanation = trump.find('a').text[1:-1]
#    url = trump.find('a').get('href') # OR url = trump.find('a')['href']
#    data.append((date, lie, explanation, url))

#  tabular_data = pd.DataFrame(data, columns = ['Date', 'Lie', 'Explanation', 'URL'])



#Trump.to_csv("Trump's_Opinion.csv") #This is to convert the dataframe into a csv file. To use it just uncomment the line.
