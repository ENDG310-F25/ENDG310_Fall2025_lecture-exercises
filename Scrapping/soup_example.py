import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Beautiful_Soup_(HTML_parser)'
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }
response = requests.get(url,headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extracting all links
    Links = soup.find_all('a')
    Links_dic = {"Titles":[L.get_text() for L in Links] , "Links": [L.get('href') for L in Links]}
    Links_table = pd.DataFrame(Links_dic, index=list(range(len(Links_dic['Titles']))))
    count = 1
    for Link in Links:
        title = Link.get_text()
        print(count,". Title:", title)
        print("\tLink",Link.get('href'))
        count += 1

        
    print(Links_dic)
    print(Links_table)