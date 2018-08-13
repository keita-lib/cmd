#! python3
# lucky.py グーグル検索結果をいくつか開く

import sys,webbrowser,requests,bs4

print("googling now ...")
search="+".join(sys.argv[1:])                  # コマンドラインの引数配列（＝検索ワード配列）　を+でつなげる 
url="https://www.google.com/search?q="+search   # 検索ワードをurlの後ろに接続する
res=requests.get(url)                           # urlのhtmlをゲット要求
res.raise_for_status()                          # レスポンスのエラーチェック

soup=bs4.BeautifulSoup(res.text)                #レスポンスのテキストをスープする
link_elems=soup.select(".r a")                  #cssセレクタが class="r"　かつ　タグが "a"　の要素を抽出

num_open=min(5,len(link_elems))                 # ブラウザタブを開く数を決める。最大で５、または数を調べて、小さいほう。

for i in range(num_open):
    webbrowser.open("https://www.google.com"+link_elems[i].get("href")) # 要素のhref属性から、値を抽出