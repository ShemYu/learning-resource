# Function's arguments

## Position arguments, Named arguments

### Position arguments

用引入順序（位置）做判斷的參數，或稱 `arguments`, `args`：

```python 
def function_a(a, b, c):
    pass

function_a(1, 2, 3)
```

### Named argumenst

用關鍵字為他命名的參數，或稱 `keyword arguments`, `kwargs`：

```python
def function_b(a=None, b=None, c=None):
    ...

function_b(a=1, b=2, c=3)
```

### Mixing

前兩者混合時，需注意 position arguments 需在 named arguments 的**前面**（由於 positions arguments 需藉由位置判斷，如果不做規範會混亂）：

```python
def function_mix(a, b, c=None):
    ...
```

## 不固定的參數介接方式

```python
def get()
```