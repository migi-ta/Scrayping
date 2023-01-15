import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://scraping-for-beginner.herokuapp.com/ranking/"

res = requests.get(url)
tourist_info = BeautifulSoup(res.text,"html.parser")

# 指定したタグ・クラスの全ての要素を配列形式で取得
spots = tourist_info.find_all("div", attrs={"class": "u_areaListRankingBox"})

# 全ての情報を配列形式で格納する
data = []

for spot in spots:
    # 観光地の名称を取得
    spot_name = spot.find("div", attrs={"class": "u_title"})
    # 特定の要素を抽出（削除）する
    spot_name.find("span", attrs={"class": "badge"}).extract()
    spot_name = spot_name.text.replace("\n","")
    # print(spot_name)

    # 「評点」を取得する
    eval_num = float(spot.find("div", attrs={"class": "u_rankBox"}).text)
    # print(type(eval_num))

    # 各項目の「評点」を取得する
    category_items = spot.find("div", attrs={"class": "u_categoryTipsItem"})
    # print(category_items)
    category_items = category_items.find_all('dl')

    # 辞書型の利用（Javaで言うところのMap形式（key:value））
    # 辞書型の宣言
    details = {}
    
    for category_item in category_items:
        category = category_item.dt.text
        rank = float(category_item.span.text)
        details[category] = rank
    details["観光地名"] = spot_name
    details["評点"] = eval_num
    data.append(details)

#print(data)

df = pd.DataFrame(data)
# カラム名の取得
# print(df.columns)

print(df)
# カラムの位置を入れ替える
df = df[['観光地名', '評点', '楽しさ', '人混みの多さ', '景色', 'アクセス']]
print(df)
df.to_csv("観光地情報.csv", index=False)

