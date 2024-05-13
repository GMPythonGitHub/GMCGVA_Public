# **Note on gound stress analysis:** ***層状地盤の応力解析***

## 概要
ここでは２つの数値型の変数を有するクラスを紹介します。
基本的なクラスから始め，これを段階的に更新することによってクラスの機能を強化していきます。

各クラスの構成は以下のようです。

[GMNumbersA: gm_class_numbers_a.py](gm_class_numbers_a.py)
> インスタンス変数と初期化関数だけが所属する基本的なクラスです  
>> インスタンス変数： aa, bb   
> 初期化関数 \_\_init\_\_()  
> 
> [GMNumbersB: gm_class_numbers_b.py](gm_class_numbers_b.py)
> 幾つかのインスタンス関数を導入しています。  
>> インスタンス変数： aa, bb  
> 初期化関数 \_\_init\_\_()  
> インスタンス関数 **add()**, **sub()**, **calc()**  
> 
> [GMNumbersC: gm_class_numbers_c.py](gm_class_numbers_c.py)
> インスタンス変数をpriveに設定し，Setting関数とGettinng関数を導入しています。  
>> インスタンス変数： **\_\_aa, \_\_bb**  # private  
> 初期化関数 **\_\_init\_\_(aa, bb)**  
> Setting関数 **set_aabb()**， Getting関数 **aa()**, **bb()**  
> インスタンス関数 calc()  
> 
> [GMNumbersD: gm_class_numbers_d.py](gm_class_numbers_d.py)
> 文字列関数を導入しています。  
>> インスタンス変数： \_\_aa, \_\_bb  
> 初期化関数 \_\_init\_\_(aa, bb)， 文字列関数 \_\_str\_\_()  
> Setting関数 set_aabb()， Getting関数 aa(), bb()  
> インスタンス関数 calc()  

---

## [GMNumbersA: gm_class_numbers_a.py](gm_class_numbers_a.py)

ここで紹介する最初のクラスGMNumbersAはとても基本的なもので，
2つの数値型変数がインスタンス変数として所属し，初期化変数を導入しています。

### **[section_class]**
クラスが所属するインスタンス変数とインスタンス関数を記述しています。  

**［section_ca］**  クラスGMVectorAでインスタンスを作成するときに起動する，初期化関数__init__()を記述しています。
```python
print('### --- section_class: (GMNumbersA) describing class --- ###')
class GMNumbersA():
    ## --- section_ca: initializing class instance --- ##
    def __init__(self) -> None:
        self.aa, self.bb = None, None  # instance variables
```
インスタンス変数aaとbbをNoneで初期化します。これによって，２つのインスタンス変数aaとbbが定義されたことになります。

### **[section_main]**
クラスのパフォーマンスをチェックする目的で，基本的なプログラムを記述しています。
クラスの記述に続くこの部分は，このファイルを起動したときのみ実行され，
外部からクラスをimportしたときは実行されません。

**［section_ma］**  
```python
print('### --- section_main: (GMMumbersA) main process --- ###')
## --- section_ma: calculating arithmetics --- ##
numbs = GMNumbersA()  # creating instance
numbs.aa, numbs.bb = 3, 2
print(f'{numbs.aa = }, {numbs.bb = }')
add, sub = (  # using instance variables
    numbs.aa + numbs.bb, numbs.aa - numbs.bb )
print(f'{add = }, {sub = }')
# ---------------------------------------------------------
numbs.aa, numbs.bb = 7, 3  # setting instance variables
print(f'{numbs.aa = }, {numbs.bb = }')
add, sub = (  # using instance variables
    numbs.aa + numbs.bb, numbs.aa - numbs.bb )
print(f'{add = }, {sub = }\n')
```
最初に，クラスGMVectorAのインスタンスnumbsを生成し，
続く２行で，インスタンス変数aaとbbを数値(3,4)に更新し，表示します。
その後，インスタンス変数の和と差を計算し表示します。
インスタンス変数を更新したり参照したりするときは，インスタンス名に続くピリオドに続けて変数名を記述します。  
後続の行では，aaとbbを(7,3)に変更し，同様な操作を繰返します。

---

## [GMNumbersB: gm_class_numbers_b.py](gm_class_numbers_b.py)

先に紹介したクラスGMNumbersAを更新し，クラスに演算する機能を追加しています。
具体的には，３つのインスタンス変数を用意しています。

### **[section_class]**

**［section_ca］**  初期化関数__init__()に変更はありません。
```python
print('### --- section_class: (GMNumbersB) describing class --- ###')
class GMNumbersB():
    ## --- section_ca: initializing class instance --- ##
    def __init__(self) -> None:
        self.aa, self.bb = None, None  # instance variables
```

**［section_cb］**  インスタンス関数の四則演算をするためのインスタンス関数を導入しています。
```python
    ## --- section_cb: functions for arithmetics --- ##
    def add(self) -> float: return self.aa + self.bb
    def sub(self) -> float: return self.aa - self.bb
    def calc(self) -> tuple:
        return self.add(), self.sub()
```
－ 関数add()は，aaとbbの和を計算して返します。
－ 関数sub()は，aaとbbの差を計算して返します。
－ 関数calc()は，関数add()と関数sub()を利用して，aaとbbの和と差を一緒にtuple型で返します。

### **[section_main]**
演算を行えるようにクラスの機能を強化したので，その機能の利用方法を紹介します。

**［section_ma］**  
```python
print('### --- section_main: (GMMumbersB) main process --- ###')
## --- section_ma: calculating arithmetics --- ##
numbs = GMNumbersB()  # creating instance
numbs.aa, numbs.bb = 3, 2
print(f'{numbs.aa = }, {numbs.bb = }')
add, sub = numbs.calc()  # using instance functions
print(f'{add = }, {sub = }')
# ---------------------------------------------------------
numbs.aa, numbs.bb = 7, 3  # setting instance valuables
print(f'{numbs.aa = }, {numbs.bb = }')
add, sub = numbs.calc()  # using instance functions
print(f'{add = }, {sub = }\n')
```
最初に，クラスGMVectorAのインスタンスnumbsを生成し，
インスタンス変数aaとbbを数値(3,4)に更新し，表示します。
インスタンス関数culc()が返すaaとbbの和と差を表示します。  
後続の行では，aaとbbを(7,3)に変更し，同様な操作を繰返します。

---

## [GMNumbersC: gm_class_numbers_c.py](gm_class_numbers_c.py)

クラスにおけるカプセル化を実現するために，先に紹介したクラスGMNumbersBを変更しています。
具体的には，インスタンス変数の特性をprivateに変更することで，
インスタンスの参照と変更といったアクセスを厳密に制御します。  
以下では，変更箇所を中心に説明します。

### **[section_class]**

**［section_ca］**  インスタンス変数のprivate化に適用するように，
初期化関数__init__()を更新しています。
```python
class GMNumbersC():
    ## --- section_ca: initializing class instance --- ##
    def __init__(self, aa, bb) -> None:
        self.__aa, self.__bb = None, None  # private instance variables
        self.set_aabb(aa, bb)
```
初期化関数が２角引数aaとbbを受け取るように更新しています。
インスタンス関数は名前を変更して__aaと__bbとします。
このように名前の前にアンダースコアを２つ着けることにより変数の特性をprivateにし，
クラスの外からは変数を参照することも更新することも直接には出来なくなります。  
最初に，インスタンス変数__aaと__bbをNoneで初期化します。
その後，次で説明するSetting関数set_aabb()に引数aa,bbを渡すことによりインスタンス変数を更新します。

**［section_cb］**  インスタンス関数として，
Setting関数set_aabb()とGetting関数aa()とbb()を記述しています。
```python
    ## --- section_cb: setting and getting functions --- ##
    ## setting functions
    def set_aabb(self, aa: float = None, bb: float = None) -> None:
        if aa is not None: self.__aa = aa
        if bb is not None: self.__bb = bb
    ## getting functions
    def aa(self) -> float: return self.__aa
    def bb(self) -> float: return self.__bb
```
－ Setting関数set_aabb()では，インスタンス変数self.__aaとself.__bbを引数 aaとbbで更新します。
ここでは，引数aaとbbのデフォルト値をNoneに設定することにより，
具体的な数値を渡したインスタンス変数self.__aaとself.__bbの両方，
あるいはどちらか一方だけを選択して更新できます。
－ Getting関数aa()とbb()がそれぞれself.__aaとself.__bbを返すことで，
インスタンス変数を参照できます。

**［section_cc］**  文字列関数に大きな変更はありませんが，ndarrayに適応した記述にしています。
```python
    ## --- section_cc: string function for print() --- ##
    def __str__(self) -> str:
        xx, yy = self.__xxyy; rr, th = self.rrth(True)
        return (
            f'(GMVectorC): xx = {xx:g}, yy = {yy:g}, '
            f'rr = {rr:g}, th(deg) = {th:g}' )
```

**［section_cd］** 以下のインスタンス関数には大きに変更はありません。
３つの関数の機能を１つの関数calc()にまとめています。
```python
    ## --- section_cc: functions for arithmetics --- ##
    def calc(self) -> tuple:
        return self.__aa + self.__bb, self.__aa - self.__bb
```

### **[section_main]**

**［section_ma］**  この部分に大きな変更はありません。
```python
print('### --- section_main: (GMMumbersC) main process --- ###')
## --- section_m0: calculating arithmetics --- ##
numbs = GMNumbersC(3, 2)  # creating instance
# print(f'{numbs.__aa = }, {numbs.__bb = }, ')
# AttributeError: 'GMNumbersC' object has no attribute '__aa'
print(f'{numbs.aa() = }, {numbs.bb() = }')
add, sub = numbs.calc()  # using instance functions
print(f'{add = }, {sub = }')
# ---------------------------------------------------------
numbs.set_aabb(aa=7, bb=3)  # setting instance variables
print(f'{numbs.aa() = }, {numbs.bb() = }')
add, sub = numbs.calc()  # using instance functions
print(f'{add = }, {sub = }\n')
```
最初に，クラスGMVectorCのインスタンスnumbsを生成するときに，(3,2)で初期化します。
インスタンス変数をインスタンス関数aa()とbb()で参照します。

---

## [GMNumbersD: gm_class_numbers_d.py](gm_class_numbers_d.py)

クラスインスタンスの属性の表示を簡潔にするために，GMNumbersを変更しています。
以下では，変更箇所のみを説明します。

### **[section_class]**

**［section_ca］**  初期化関数__init__()に変更はありません。

**［section_cb］**  Setting関数とGetting関数に変更はありません。

**［section_cc］**  関数print()でインスタンス名を指定すると起動する，文字列関数__str__()を記述しています。
```python
    ## --- section_cc: string function for print() --- ##
    def __str__(self) -> str:
        return f'(GMNumbersD): aa = {self.__aa:g}, bb = {self.__bb:g}'
```
インスタンスの属性（クラス名とインスタンス変数）を記述する文字列をf-string型で作成して返します。

**［section_cd］** 演算結果を返すインスタンス関数に変更はありません。

### **[section_main]**

**［section_ma］**  
```python
print('## --- section_main: (GMMumbersD) main process --- ##')
## --- section_ma: calculating arithmetics --- ##
numbs = GMNumbersD(3, 2)  # creating instance
print(numbs)
add, sub = numbs.calc()  # using instance functions
print(f'{add = }, {sub = }')
# ---------------------------------------------------------
numbs.set_aabb(aa=7, bb=3)  # setting instance variables
print(numbs)
add, sub = numbs.calc()  # using instance functions
print(f'{add = }, {sub = }\n')
```
関数print()にインスタンス名を引数として渡し，文字列関数からの戻される文字列を表示します。

