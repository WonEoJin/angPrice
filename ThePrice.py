from pathlib import Path
from urllib.request import urlretrieve

base_url = "https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/data/"

# 저장위치 지정과 생성
data_path = Path() / "data"
data_path.mkdir(parents=True, exist_ok=True)

def myWget(filename):
    # 다운로드 대상 파일 경로
    file_url = base_url + filename

    # 저장 경로와 파일명
    target_path = data_path / filename

    return urlretrieve(file_url, target_path)
  
target_path, _ = myWget("shopA.txt")

with open(target_path, encoding="utf-8", mode="r") as f :
  shop = f.read()

shop = shop.replace("오레ㄴ지", "오렌지")

with open(target_path, mode='w', encoding='utf-8') as f:
    f.write(shop)

with target_path.open(mode='r', encoding='utf-8') as f:
    shop_dict = {}
    
    for line in f:
      price_of_goods = line.strip().split()
      if price_of_goods != []:
        goods, price = price_of_goods 
      if price != 'A':  
        shop_dict[goods] = int(price.rstrip('원'))

def shopping(shop_file):
    shop_dict = {} # 생성할 사전 객체

    with open(data_path / shop_file, mode='r', encoding='utf-8') as f:    
      for line in f:
        price_of_goods = line.strip().split() 
        if price_of_goods != []:      
          goods, price = price_of_goods 
        if price != shop_file[4]:
          shop_dict[goods] = int(price.rstrip('원'))

    return shop_dict


def item_price(shop_file, item):
    return shopping(shop_file)[item]


