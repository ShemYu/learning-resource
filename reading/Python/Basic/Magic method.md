# Magic method of Python

Magic method 指的是 Pyhton 為類別預定義的一些常用方法，例如定義類別的字串形式、實作時執行的方法、運算單元處理的方法等。

```python
class Example():
    def __init__(self):
        # 實作時觸發
    def __str__(self):
        # 字串形式
        return "Str type of class"
    def __add__(self, value):
        return self.A + value
```
---
## `__init__` 及 `__new__` 差別是什麼
其中最常使用的就是 `__init__`，實作 class 時會觸發的方法。    
雖然並非必須使用，但往往會遇到實作時需要處裡的類別，例如從生日計算年齡、從體重身高推算 BMI，甚至給定資料路徑，初始化先 loading 資料進物件當中，在依據使用者需求作客製化處理等。

```python
class human():
    def __init__(self, birth):
        self.age = time.today().year - self.birth.year
        self.birthday = birth
```
    
跟 `__init__` 十分相近的則是 `__new__`，不同的是 init 是在類別實作成物件時觸發，而 new 是在實作類別本身時就會觸發，也因此他的引數不是代表該實作**物件**本身的 `self`，而是代表**類別**本身的 `cls`。

```python
class human():
    def __new__(cls, name, age):
        print("Do when you new a `class`.")
        return super(human, cls).__new__(cls, name, age)
```

在以下文章當中有詳細關於 `__init__`, `__new__` 的調用邏輯，可供參考。    
> ## [Python 中的 `__init__` 和 `__new__`](https://www.zlovezl.cn/articles/__init__-and__new__-in-python/)
> `__init__` 和 `__new__` 最主要的区别在于：
> - `__init__` 通常用于初始化一个新实例，控制这个初始化的过程，比如添加一些属性， 做一些额外的操作，发生在类实例被创建完以后。它是实例级别的方法。
> - `__new__` 通常用于控制生成一个新实例的过程。它是类级别的方法。

在 Python 的官方文件當中，`__new__` 被說明為以下兩種用途:
- 當你在繼承一些無法複寫的類別時，可以使用 `__new__` 來做一種自定義
- 實作自定義之 `metaclass`

---