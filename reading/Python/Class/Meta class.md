# Meta class 是什麼

Metaclass 在 Python 當中定義了`類別`的`類別`，簡單的演示一下會比較清楚在說什麼:

```python
class MyMeta(type):
    pass

class MyClass(metaclass=MyMeta):
    pass

class MySubclass(MyClass):
    pass

if __name__ == "__main__":
    MyClass = MyMeta()
    my_object = MyClass()
```

簡單的定義三種不同的類別:
- MyMeta: 繼承 `type`
- MyClass: metaclass = MyMeta
- MySubclass: 繼承 MyClass

```python
print(type(MyMeta))
print(type(MyClass))
print(type(MySubclass))
```
```bash
<class 'type'>
<class '__main__.MyMeta'>
<class '__main__.MyMeta'>
```

> ## [Introduction to Python Metaclass](https://www.datacamp.com/community/tutorials/python-metaclasses)
> ### In this tutorial, learn what metaclasses are, how to implement them in Python, and how to create custom ones.