"""_ライブラリのインストール_
    
    requests（HTMLをダウンロード）
    → pip install requests
    
    BeautifulSoup4（HTMLを解析）
    → pip install BeautifulSoup4
    
    インポート
    import requests
    from bs4 import BeautifulSoup
    
"""

import requests
from bs4 import BeautifulSoup

url = "https://scraping-for-beginner.herokuapp.com/udemy"

# requests → HTML情報を取得
res = requests.get(url)
# レスポンスのステータスコードの表示
print(res)

#　BeautifulSoup → HTMLの構造解析
structure = BeautifulSoup(res.text,"html.parser")

# HTMLのインデントを整える
# print(structure.prettify())

# 指定した要素を全て取得
#print(structure.find_all("p"))

#print(structure.find_all("p")[0])
#print(structure.find_all("p")[1])
#print(structure.find_all("p")[2])
#print(structure.find_all("p")[2].text)

# 要素 > class の順で検索を絞り込む
subscribers = structure.find_all("p", attrs={"class": "subscribers"})[0].text
n_subscribers = subscribers.split("：")[1]
print(n_subscribers)

reviews = structure.find_all("p", attrs={"class": "reviews"})[0].text
n_reviews = reviews.split("：")[1]
print(n_reviews)



