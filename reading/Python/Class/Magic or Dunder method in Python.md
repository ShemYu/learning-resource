# Magic or Dunder method in Python

此篇會簡單介紹類別常用的 Magic method 及相關範例，參考文獻如下:
- [Magic method in Python](https://www.tutorialsteacher.com/python/magic-methods-in-python)

---
## `__new__`

Python 當中的類別到物件實作過程:

1. `__new__`
2. `__init__`

因此在設計了上述兩者的類別，Python 會先將類別 new 出物件，再藉由 init 實作，導致了以下結果:

```python
class Employee:
    def __new__(cls):
        print ("__new__ magic method is called")
        inst = object.__new__(cls)
                return inst
    def __init__(self):
        print ("__init__ magic method is called")
        self.name='Satya'
```

```bash
>>> emp = Employee()
__new__ magic method is called
__init__ magic method is called
```

---
## `__str__`

類別的字串型態之呈現邏輯，形同對該類別實作之物件使用 `str()` 方法。

```python
num = 12
str(num) # '12'
```

複雜一點的範例: 
```python
class Employee:
    def __init__(self):
        self.name='Swati'
        self.salary=10000
    def __str__(self):
        return 'name='+self.name+' salary=$'+str(self.salary)
```
```python
e1 = Employee()
print(e1) # name=Swati salary=$10000
```
---
## `__add__`

定義物件如何執行相加的動作。
```python
class distance:
    def __init__(self, x=None,y=None):
        self.ft=x
        self.inch=y
    def __add__(self,x):
        temp=distance()
        temp.ft=self.ft+x.ft
        temp.inch=self.inch+x.inch
        if temp.inch>=12:
            temp.ft+=1
            temp.inch-=12
            return temp
    def __str__(self):
        return 'ft:'+str(self.ft)+' in: '+str(self.inch)
```
```python
d1=distance(3,10)
d2=distance(4,4)
print("d1= {} d2={}".format(d1, d2))
# d1= ft:3 in: 10 d2=ft:4 in: 4
d3=d1+d2
print(d3)
# ft:8 in: 2
```
---
## `__ge__`

代表 `>=` 運算符

```python
class distance:
    def __init__(self, x=None,y=None):
        self.ft=x
        self.inch=y
    def __ge__(self, x):
        val1=self.ft*12+self.inch
        val2=x.ft*12+x.inch
        if val1>=val2:
            return True
        else:
            return False
```
```python
d1 = distance(2,1)
d2 = distance(4,10)
print(d1 >= d2)
# False
```
---

更多 Magic methods in Python 請見[參考文獻](https://www.tutorialsteacher.com/python/magic-methods-in-python)。