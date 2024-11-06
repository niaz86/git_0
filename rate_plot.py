import requests
import datetime
import pandas as pd
from lxml import html
import os

url = "https://www.bajus.org/gold-price"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "en-US,en;q=0.9,bn;q=0.8",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": "XSRF-TOKEN=eyJpdiI6InlNYlM0aXlTOW1oSC9rbUtaWktpZUE9PSIsInZhbHVlIjoieWtsUGFGQ01BNDFuT0t2cG13YXY1WUlvZ3V6empFRWhISkZkVXpDK0tuUDFmVm1tQ3A1Y3oySTJEbEQ1ZFJ2ZFdCbEg4QlBWK0tsT1gyTWtiNCthaklCNnVJZzk3YlgwUExob1NDQU5zdVhlb2hxbUJtTEN3eHJTTEgxTnhmYUEiLCJtYWMiOiI5ZjNmOGY4ZDgyZGJiNDY4MDQ2ZjlhM2E5N2ViNGE0Y2IwYTk2NjkzZDMwNzAwYmVmNzMyNTI1N2QxNTI5MjZhIiwidGFnIjoiIn0%3D; bajus_session=eyJpdiI6IlRuMzJlcVlaZlVyZ2htOTBEL29idWc9PSIsInZhbHVlIjoiQjlpK202bVpUbE1BWHQ1MUFReHlxQmg1TjBON0tGa3hhSzBUVW5xckM2Sk90UkJLNDVuSitpTkgxT1JMWTBrQ2dWb0xhcGNVampKeFM5cHNRclozeGo3MWViVmI3UzQxMXNFMVk0Y0pjL0E5Uzk1UGYxRzNMWlRseUN1Z0VZWXUiLCJtYWMiOiI3OTZmNDY2YTdlN2YwMmMwOTY4YTUxYzhmMWE0ZDc3NTY1MzEzYmMzOGVjNjRjZTYxMDdmNmU2ZWQzOWM1YzU2IiwidGFnIjoiIn0%3D",
    "Referer": "https://www.google.com/",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"'
}

# Send GET request with the headers
response = requests.get(url, headers=headers)

# Check the status code
print(response.status_code)

tree=html.fromstring(response.content)

Time=datetime.datetime.now().strftime('%d:%B:%Y')
Gold_pro_name=[]
Silver_pro_name=[]
for i in tree.xpath('/html/body/section/div/div//table/tbody/tr/th/h6/text()'):
    names=i.strip()
    if 'Gold' in names:
        Gold_pro_name.append(names)
    else:
        Silver_pro_name.append(names)

prices=tree.xpath('/html/body/section/div//div/table/tbody/tr/td/span/text()')

Gold_price=[]
for i in prices[0:4]:
    k=int(i.split(' ')[0].replace(',',''))
    Gold_price.append(k)
Silver_price=[]
for i in prices[4:]:
    k=int(i.split(' ')[0].replace(',',''))
    Silver_price.append(k) 

file_path='Analysis of Silver marketing.csv'    
if Silver_price!=None:
    z={}
    for x,y in zip(Silver_pro_name,Silver_price):
        z[x]=[y]      
    data=pd.DataFrame(z,index=[Time]) 
    if os.path.exists(file_path):
        data.to_csv(file_path,mode='a',header=False)
    else:
        data.to_csv(file_path)
file_path='Analysis of Gold marketing.csv'
if Gold_price!=None:
    z={}
    for x,y in zip(Gold_pro_name,Gold_price):
        z[x]=[y]      
    data=pd.DataFrame(z,index=[Time]) 
    if os.path.exists(file_path):
        data.to_csv(file_path,mode='a',header=False)
    else:
        data.to_csv(file_path)
  