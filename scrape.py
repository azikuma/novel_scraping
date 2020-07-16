import time
from urllib import request
from bs4 import BeautifulSoup

num_parts = 478  # 作品の全話数を指定

with open("novel.txt", "w", encoding="utf-8") as f:
    for part in range(1, num_parts+1):
        # 作品本文ページのURL
        url = "url/{:d}/".format(part)

        res = request.urlopen(url)
        soup = BeautifulSoup(res, "html.parser")

        # 本文を指定
        honbun = soup.select_one("#novel_honbun").text
        honbun += "\n"  # 次の部分との間は改行しておく
        
        # 保存
        f.write(honbun)
        
        print("part {:d} downloaded".format(part))  # 進捗を表示

        time.sleep(1)  # 次の取得まで1秒間空ける
