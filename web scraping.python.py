''' WEB SCRAPING---> website data is collecting '''

# Import section
import requests
import pandas
from bs4 import BeautifulSoup

response=requests.get("https://www.flipkart.com/search?q=iphone+15&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=iphone+15%7CMobiles&requestId=708f95a7-ddfb-4476-9540-69d710e8f073")
# print(response) request to website

soup=BeautifulSoup(response.content,'html.parser')
# print(soup) raw data

names=soup.find_all('div',class_='KzDlHZ')
name=[]
for i in names[0:12]:
    d=i.get_text()
    name.append(d)
# print(names)


prices=soup.find_all('div',class_='yiggsN O5Fpg8')
price=[]
for i in prices[0:12]:
    d=i.get_text()
    price.append(d)
# print(price)



ratings=soup.find_all('div',class_='XQDdHH')
rate=[]
for i in ratings[0:10]:
    d=i.get_text()
    rate.append(d)
# print(rate) 



reviews=soup.find_all('span',class_='Wphh3N')
review=[]
for i in reviews[0:10]:
    d=i.get_text()
    review.append(d)
# print(review)    


features=soup.find_all('li',class_="J+igdf")
feature=[]
for i in  features[0:10]:
    d=i.get_text()
    feature.append(d)
# print(feature) 

images=soup.find_all('img',class_="DByuf4")
image=[]
for i in images[0:10]:
    d=i['src']
    '''d=i.div.img['src]'''
    image.append(d)   
# print(image)    

# df = pandas.DataFrame()
# print(df)


data={'names':name,
      'prices':price,
      'ratings':rate,
      'reviews':review,
      'features':feature,
      'images':image}
# print(data)

data={'names':pandas.Series(name),
      'prices':pandas.Series(price),
      'ratings':pandas.Series(rate),
      'reviews':pandas.Series(review),
      'features':pandas.Series(feature),
      'images':pandas.Series(image)
      }
df = pandas.DataFrame(data)
# print(df)

df.to_CSV("mobiles_data.csv")
