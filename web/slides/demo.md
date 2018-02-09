# デモ中身


### Python side

```python
import eel
from whois import whois

@eel.expose  # <-- ここで、フロントに渡す関数の定義
def get_whois(zone):
    w = whois(zone)
    return str(w)

eel.init('web')
eel.start('slide.html')
```


### JS side

```html
<script type="text/javascript" src="/eel.js"></script>
```

```javascript
document.getElementById('demo-zone-btn').addEventListener('click', () => {
    var val = document.getElementById('demo-whois-input').value;
    eel.get_whois(val);  // <-- ここで、Pythonの呼び出し
    let register = await eel.get_whois(val)();
    document.getElementById('demo-zone-output').innerText = register;
});
```


### ちょっとだけEelの中身

`__init__.py`

```python
import bottle as btl, bottle.ext.websocket as wbs
import eel.browsers as brw

def start(*start_urls, **kwargs):
    # (略)
    brw.open(start_urls, options)

    run_lambda = lambda: btl.run(host=options['host'], port=options['port'], server=wbs.GeventWebSocketServer, quiet=True)
    # (略)
```

`browsers.py`

```python
import webbrowser as wbr, sys, subprocess as sps, os

# (略)
def open(start_pages, options):
    # (略)
    sps.Popen(
        [chrome_path, '--app=%s' % url] + options['chromeFlags'],
        stdout=sps.PIPE, stderr=sps.PIPE)
    # (略)
```


### ざっくりとした実態

- bottleでサーバーを起動して
- Chromeで表示して
- Websocketを経由でPython側で色々処理する

要するに…

**ローカルで動かす用のWebアプリ+Chrome**というのが近い
