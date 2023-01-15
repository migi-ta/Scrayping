import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# アクセス先URL
url = "https://scraping-for-beginner.herokuapp.com/login_page"

# Chromeブラウザのオートバージョン管理の状態を保持する
chrome_driver = webdriver.Chrome(ChromeDriverManager().install())
chrome_driver.get(url)

"""_ヘッドレスモードの利用_

    # ヘッドレスモードのライブラリをインポート
    # from selenium.webdriver.chrome.options import Options
    
    Optionsのインスタンス化
    options = Options()
    
    ヘッドレスモードを設定
    options.add_argument('--headless')
    
    ドライバーにヘッドレスモードを設定
    chrome_driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
    
"""

# アクセスする要素を取得
elem_name = chrome_driver.find_element_by_id("username")
elem_pass = chrome_driver.find_element_by_id("password")
elem_btn = chrome_driver.find_element_by_id("login-btn")

# アクセスする要素に値を挿入
elem_name.send_keys("imanishi")
elem_pass.send_keys("kohei")

#ログインボタンのクリック
elem_btn.click()

# テキスト上の値を表示
elem_name = chrome_driver.find_element_by_xpath('//*[@id="name"]').text
print(elem_name)

elem_hobby = chrome_driver.find_element_by_id("hobby").text
print(elem_hobby)

# 複数のタグ要素を一度に取得
elems_th = chrome_driver.find_elements_by_tag_name("th")

# 複数の値をリストで一つにする
keys = []
for elem_th in elems_th:
    key = elem_th.text
    keys.append(key)
print(keys)

"""_csv出力に用いるPandasライブラリの利用_
    
    ターミナル or コマンドプロンプトにて
    pip install pandas
    
    pandasの宣言
    import pandas as pd
    
    データフレームを使用
    空のデータフレームを作成
    df = pd.DataFrame()
    
    配列宣言
    subject = ["算数","国語","理科","社会","英語"]
    num = [60,70,80,30,100]
    
    データフレームのカラム名を作成し、値を代入
    df["項目"] = subject
    df["点数"] = num
    
    print(df)

    csv出力（指定した階層にcsv作成 / 特定の列のみ出力 / 追記モード ）
    df.to_csv("/Users/migita/Desktop/dev/create_to_csv_file.csv" , index=False, columns=["項目","点数"] , mode="a")

"""

time.sleep(3)
chrome_driver.close()