# What is Decorator

- Decorator 是 Python 當中的避免重工的一種語法，能藉由傳遞 function 做參數的方式大量簡化程式碼。

- Decorator 可以是一個 function 也可以是一個 class，主要目的相同，皆為避免重工。

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