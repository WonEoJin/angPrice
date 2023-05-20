from pathlib import Path
from urllib.request import urlretrieve

데이터가 저장된 텍스트 파일 서버 주소는 다음과 같다.

base_url = "https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/data/"

현재 작업 디렉토리의 `data` 하위 디렉토리에 파일을 다운로드해서 저장할 준비를 한다.

# 저장위치 지정과 생성
data_path = Path() / "data"
data_path.mkdir(parents=True, exist_ok=True)

`myWget()` 함수는 파일 서버에서 지정된 파일을 동일한 파일명으로 지정된 디렉토리에 저장한다.

def myWget(filename):
    # 다운로드 대상 파일 경로
    file_url = base_url + filename

    # 저장 경로와 파일명
    target_path = data_path / filename

    return urlretrieve(file_url, target_path)

**쇼핑몰 파일 관련**

**문제 1**

`shopA.txt` 파일은 쇼핑몰A에서 판매하는 상품의 가격을 담고 있음을 확인해보자.
먼저 해당 파일을 다운로드 한다.

target_path, _ = myWget("shopA.txt")

이제 파일 전체 내용을 출력하는 코드를 작성하라.

힌트: `with-as` 명령문, `open()` 함수, `readlines()` 또는 `read()` 파일 메서드.

# 코드를 작성하세요.

with open(target_path, encoding="utf-8", mode="r") as f :
  print(f.read())

**문제 2**

`shopA.txt` 파일의 내용을 확인하면, 오타가 있다. 
'오레ㄴ지' 를 '오렌지'로 변경한 후에
`shopA.txt` 파일을 열어 오타가 수정되었는지를 확인하여라.  

힌트: 파일의 `read()` 메서드, 문자열의 `replace()` 메서드

* 파일 읽기: `read()` 메서드 활용

# 파일내용을 하나의 문자열로 생성하는 코드를 작성하라.

with open(target_path, encoding="utf-8", mode="r") as f :
  shop = f.read()

shop

* 오타 수정: `replace()` 문자열 메서드 활용

# 오타를 수정하는 코드를 작성하라.

shop = shop.replace("오레ㄴ지", "오렌지")
shop

* 파일 저장

# 오타가 수정된 문자열을 파일로 저장하는 코드를 작성하라.

with open(target_path, mode='w', encoding='utf-8') as f:
    f.write(shop)

* 파일 내용 확인

# 오타가 수정되었음을 확인하는 코드를 작성하라.

with target_path.open(mode='r', encoding='utf-8') as f:
    print(f.read())

**문제 3**

상품명과 가격을 키-값의 쌍으로 갖는 아래 모양의 딕셔너리를 만들어라.
단, 오타가 수정된 파일을 이용해야 한다.

```python
{'우유': 2540,
 '계란': 7480,
 '생수': 980,
 '짜장라면': 3220,
 '두부': 1450,
 '콩나물': 1680,
 '김': 5480,
 '닭고기': 5980,
 '식빵': 2480,
 '바나나': 4980,
 '오렌지': 990,
 '카레': 2480,
 '만두': 6980,
 '어묵': 7980,
 '참치': 11880,
 '김치': 7980,
 '간장': 10800}
```

with target_path.open(mode='r', encoding='utf-8') as f:
    shop_dict = {}
    
    for line in f:
      price_of_goods = line.strip().split()
      if price_of_goods != []:
        goods, price = price_of_goods 
      if price != 'A':  
        shop_dict[goods] = int(price.rstrip('원'))

shop_dict

**문제 4** 

`shopA.txt` 와 같이 상품명과 가격으로 이루어진 쇼핑 리스트가 포함된 파일의 이름을 입력받으면
상품명과 가격을 각각 키와 값으로 갖는 사전 객체를 반환하는 함수 `shopping()` 을 구현하라.



# 아래 코드를 완성하라. 

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
print(shopping("shopA.txt"))

**문제 5**

쇼핑 리스트와 상품을 인자로 지정하면 상품의 가격을 반환하는 함수 `item_price()` 를 구현하라.



# 함수를 완성하라.

def item_price(shop_file, item):
    return shopping(shop_file)[item]

print(item_price("shopA.txt", '김치'))

**문제 6**

`shopB.txt` 파일은 쇼핑몰B에서 판매하는 상품의 가격을 담고 있으며,
`shopA.txt` 파일과 동일한 방식으로 다운로드할 수 있다.

myWget("shopB.txt")

사용자가 상품을 입력하면, 쇼핑몰A와 쇼핑몰B 중 어느 쇼핑몰에서 구입하는 것이 얼마나 저렴한지를 보여주는
함수 `price_comparison()`를 작성하라.

# 코드를 완성하라.

def price_comparison(item):
    shopA_dict = shopping("shopA.txt")
    shopB_dict = shopping("shopB.txt")

    conparison_price = shopA_dict[item] - shopB_dict[item]
    if conparison_price < 0:
        return f"shopA가 {abs(conparison_price)}원 더 저렴합니다. (shopA의 가격 : {shopA_dict[item]}원, shopB의 가격 : {shopB_dict[item]}원)"
    elif conparison_price == 0:
        return "두 쇼핑물에서의 가격이 같습니다."
    else:
        return f"shopB가 {conparison_price}원 더 저렴합니다. (shopB의 가격 : {shopB_dict[item]}원, shopB의 가격 : {shopB_dict[item]}원)"

print(price_comparison('김치'))

**다이빙 기록 관련**

**문제 7**
myWget("results10m.txt")

scores_10m = {}

with open("data/results10m.txt", 'r') as f:
    for line in f:
        name, s_10m = line.split()[:2]
        
        try:
            scores_10m[name] = float(s_10m)
        except:
            continue

sorted_scores_10m = sorted(scores_10m.items(), key = lambda item: item[1], reverse=True)

print("10미터 다이빙 경기 결과\n")

count = 1
for item in sorted_scores_10m:
    print(f"{count:>3}등: {item[0]} {item[1]}")
    count += 1

**문제 8**

5미터 다이빙 기록과 10미터 다이빙 기록의 합에 대해 등수를 확인하는 코드를 작성하라.

# 코드를 작성하라.
myWget("results5m.txt")
with open("data/results5m.txt") as f:
    results_5m_dict = {}
    for line in f:
        name, score = line.strip().split()
        if score != '점수':
            results_5m_dict[name] = score

with open("data/results10m.txt") as f:
    results_10m_dict = {}
    for line in f:
      name, score = line.strip().split()
      if score != '점수':
        results_10m_dict[name] = score

all_diving_results_dict = {}

for name in results_5m_dict:
    score_5m = float(results_5m_dict[name])
    score_10m = float(results_10m_dict[name])
    all_diving_results_dict[name] = (score_5m + score_10m)

sorted_all_diving_results = sorted(all_diving_results_dict.items(), key = lambda item: item[1], reverse=True)

print("5미터, 10미터 다이빙 경기 결과의 총합\n")

count = 1
for item in sorted_all_diving_results:
    print(f"{count:>3}등: {item[0]} {item[1]:.2f}")
    count += 1
