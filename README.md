# Eelで作ってみるWHOISアプリとスライド

## これは何？

みんなのPython勉強会#32の懇親会中LTで発表したスライド(デモを含む)のソース一式です。

## 動作環境について

- Google Chrome（デフォルトパスでインストールされていること）
- Python3.6系以上
    - 1箇所だけ、f-stringを使っている箇所があります

## 動かし方（例）

```
$ git clone https://github.com/attakei/eel-demo-with-slide.git
$ cd eel-demo-with-slide
$ pip install -r requirements.txt
$ python main.py
```

[このようなスライド](https://speakerdeck.com/attakei/eeldezuo-tutemiru-whoisapurito-suraido)になります。

### 注意点メモ

- Eel 0.9.1時点でのスライドです。更新されるとスライドの内容と変わる場合があります。
- デモ部分のWHOIS用フォームはEnterを押すとスライドのトップに遷移してしまいます。
