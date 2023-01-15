import requests
from bs4 import BeautifulSoup

"""_画像処理を行うPillowのインストール_
    pip install Pillow
    
    Pillowのインポート
    from PIL import Image
    
    ファイルの入出力を行うioのインポート
    import io

"""

from PIL import Image
import io

url = "https://scraping-for-beginner.herokuapp.com/image"

res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")
# print(soup)

# imgタグの取得
# img_tag = soup.find("img")
# print(img_tag) # <img class="materialbox responsive-img card" src="/static/assets/img/img1.JPG"/>

# 対象ホストを指定
root_url = "https://scraping-for-beginner.herokuapp.com"
# 対象ホストから画像までのURLを作成
# img_url = root_url + img_tag["src"] # https://scraping-for-beginner.herokuapp.com/static/assets/img/img1.JPG

# 画像データの取得と保存（単体の画像）
#img = Image.open(io.BytesIO(requests.get(img_url).content))
#img.save("/Users/migita/Desktop/dev/img/sample.jpg")

# 画像データの取得と保存（複数の画像）
# imgタグがついたタグをリスト形式で全て取得
img_tags = soup.find_all("img")
# for文 / enumerate関数
for i, img_tag in enumerate(img_tags,1):
    # 画像ファイルのフルパスを指定
    img_url = root_url + img_tag["src"]
    # 画像ファイルを取得
    img = Image.open(io.BytesIO(requests.get(img_url).content))
    # 指定フォルダに画像ファイルを保存 / format関数
    img.save("/Users/migita/Desktop/dev/img/sample{}.jpg".format(i))


