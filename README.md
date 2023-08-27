

# Nitter

## This project is no longer maintained.

Simple **Twitter** scraper using **[Nitter](https://nitter.moomoo.me/)**

For now, It's used only to scrap media (images)

## 

## How To Install

You can use the following command to install it.

```
pip install nitter
```

## Getting Started

```python
from nitter import Nitter

n = Nitter()
from nitter import Nitter

nitter = Nitter()
username = "X"

for media in nitter.get_media(username):
    print("Caption:", media.caption)
    print("Pub Date:", media.pub_date)
    print("Images:", "\n".join(img.src for img in media.images), "\n")
```

## Licence

[MIT](https://github.com/iAliF/Nitter/blob/master/LICENSE)
