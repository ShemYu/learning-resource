# What is Decorator
- 中文名稱叫做**裝飾器**，好啦這不重要
- 輸入 function，在其外層增加一些點綴，再回傳這個 function，名符其實吧
- Decorator 可以是一個 function 也可以是一個 class，依照需求變動

馬上看看範例更有感覺:
```python
def print_func_name(func):
    def wrap():
        print("Now use function '{}'".format(func.__name__))
        func()
    return wrap


def dog_bark():
    print("Bark !!!")


def cat_miaow():
    print("Miaow ~~~")


if __name__ == "__main__":
    print_func_name(dog_bark)()
    # > Now use function 'dog_bark'
    # > Bark !!!

    print_func_name(cat_miaow)()
    # > Now use function 'cat_miaow'
    # > Miaow ~~~
```
上述案例當中的 `print_func_name` 就是一個裝飾器，但其實有 `syntax candy`:
```python
def print_func_name(func):
    def warp():
        print("Now use function '{}'".format(func.__name__))
        func()
    return warp


@print_func_name
def dog_bark():
    print("Bark !!!")


@print_func_name
def cat_miaow():
    print("Miaow ~~~")


if __name__ == "__main__":
    dog_bark()
    # > Now use function 'dog_bark'
    # > Bark !!!

    cat_miaow()
    # > Now use function 'cat_miaow'
    # > Bark !!!
```
只要用簡單的 `@` 就可以讓 Decorator 輕鬆地套用在 function 上。
> ### 補充: `sytax candy` 中文稱語法糖或語法糖衣，意旨原本需要複雜的語法完成的邏輯，用更為簡單的方式實現

# Deocrator 的執行優先性
Decorator 的優先性是比較需要注意的部分，雖然不難理解但若沒有了解過很容易弄錯
```python
def print_func_name(func):
    def warp_1():
        print("Now use function '{}'".format(func.__name__))
        func()
    return warp_1


def print_time(func):
    import time
    def warp_2():
        print("Now the Unix time is {}".format(int(time.time())))
        func()
    return warp_2


@print_func_name
@print_time
def dog_bark():
    print("Bark !!!")


@print_time
@print_func_name
def cat_miaow():
    print("Miaow !!!")


if __name__ == "__main__":
    dog_bark()
    # > Now use function 'warp_2'
    # > Now the Unix time is 1541239747
    # > Bark !!!

    cat_miaow()
    # > Now the Unix time is 1541239747
    # > Now use function 'cat_miaow'
    # > Miaow !!!
```
以 syntax candy 的形式來看，可能不好理解，但若以一般語法來看，應該就不難理解為什麼:    
`print_time(print_func_name(cat_miao))`

# Decorator 可以是一個 Class
Decorator 不局限於 function 的形式，Decorator 也可以是一個 Class:
```python
class Dog:
    def __init__(self, func):
        self.talent = func

    def bark(self):
        print("Bark !!!")


@Dog
def dog_can_pee():
    print("I can pee very hard......")


@Dog
def dog_can_jump():
    print("I can jump uselessly QQQ")


@Dog
def dog_can_poo():
    print("I can poo like a super pooping machine!")



if __name__ == "__main__":
    dog_1 = dog_can_pee
    dog_1.talent()
    # > I can pee very hard......

    dog_2 = dog_can_jump
    dog_2.talent()
    # > I can jump uselessly QQQ

    dog_3 = dog_can_poo
    dog_3.talent()
    # > I can poo like a super pooping machine!
```
上述例子便是把 input 進入 Dog 類別的 function 動態設定成一個 function，便可透過統一介面( `Dog.talent` )呼叫

# Decorator 甚至可以帶入參數
```python
import time


def print_func_name(time):
    def decorator(func):
        def warp():
            print("Now use function '{}'".format(func.__name__))
            print("Now Unix time is {}.".format(int(time)))
            func()
        return warp
    return decorator


@print_func_name(time=(time.time()))
def dog_bark():
    print("Bark !!!")



if __name__ == "__main__":
    dog_bark()
    # > Now use function 'dog_bark'
    # > Now Unix time is 1541296864.2953653.
    # > Bark !!!
```

# What is class method

一般寫在 Class 當中的 function，意味著該類別被宣告為物件後，該 function 啟動時藉由調用 self ，可調用該物件之屬性。

- ## 一般類別方法

    以下列 Person class 為例：

    ``` python
    class Person():
        def __init__(self, name, tall, fat):
            self.name = name
            self.tall = tall
            self.fat = fat
        
        def get_bmi(self):
            return (self.fat/100)**2/self.tall
    ```

    運用 Person class 宣告 Jack object

    ```python 
    Jack = Person('Jack', '180', '100')
    ```

    從 Jack 的屬性計算 BMI

    ```python
    Jack.get_bmi()
    ```
- ## Classmethod

    可以藉由 cls 參數使用該 class 原生屬性

    ```python
    class c:
        @classmethod
        def foo(cls):
            # do something..
    ```

# Reference

1. [整個程式都是我的咖啡館](https://medium.com/citycoddee/tagged/python-advanced)

1. [Decorator 基礎概念篇](https://medium.com/citycoddee/python%E9%80%B2%E9%9A%8E%E6%8A%80%E5%B7%A7-3-%E7%A5%9E%E5%A5%87%E5%8F%88%E7%BE%8E%E5%A5%BD%E7%9A%84-decorator-%E5%97%B7%E5%97%9A-6559edc87bc0)

1. [Python 基礎 - classmethod and staticmethod](https://blog.csdn.net/HeatDeath/article/details/76690468)

1. [classmethod v.s. staticmethod in Python](https://www.geeksforgeeks.org/class-method-vs-static-method-python/)