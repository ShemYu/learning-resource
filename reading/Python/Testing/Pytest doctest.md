# Pytest doctestplus

[pytest-doctestplus](https://github.com/astropy/pytest-doctestplus)
Pytest plugin 之一，能提供方便功能撰寫並檢查 docstring，使 sphinx 生成高品質的說明文件。

## Why we need to do doctest?

一個多人合作的專案勢必有撰寫文件的需求，現已有非常方便的文件自動生成 module (如 [Sphinx - get started](https://www.sphinx-doc.org/en/master/usage/quickstart.html))，從 docstring 自動化生成文件的方式也提升了文件品質的重要性，尤其是當中的測試範例，而 `doctest` 正是針對 docstring 當中 example code 的格式、結果進行測試。

---
## Python test example in docstring

[doctest - Python 3.9.1 document](https://docs.python.org/3/library/doctest.html)

以官方文件範例代碼，一般 docstring 都是以 Description, Attributes, Returns and Example 組成，而官方範例僅包含 Description，需要特別注意的是所有的標題前須空一行(ERROR of doctest):

- Description: 第一行簡述對象，空一行選填詳細說明，通常不寫標題。

    ```python
    """Module of foo.

    Provide functional method to boo and bar.
    """
    ```

- Attributes: 敘述輸入輸出的參數

    ```python
    """Module of foo.

    Provide functional method to boo and bar.

    Attributes:

        name(str): required. Description of name.
        age(int): optional, default=1. Description of age.
    """
    ```
- Returns: 敘述回傳變數型態
    ```python
    """Module of foo.

    Provide functional method to boo and bar.

    Attributes:

        name(`str`): required. Description of name.
        age(`Union[int, str]`): optional, default=1. Description of age.
    
    Returns:

        `str`. Return boyfriend's name, girlfriend's name or None.
    """
    ```

- Example: 寫下範例代碼教人如何使用這支程式
    ```python
    """Module of foo.

    Provide functional method to boo and bar.

    Attributes:
        name(`str`): required. Description of name.
        age(`Union[int, str]`): optional, default=1. Description of age.
    
    Returns:
        `str`. Return boyfriend's name, girlfriend's name or None.

    Example:
        >>> foo('Jack', 15)
        None
    """
    ```

```python
"""
This is the "example" module.

The example module supplies one function, factorial().  For example,

>>> factorial(5)
120
"""

def factorial(n):
    """Return the factorial of n, an exact integer >= 0.

    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(30)
    265252859812191058636308480000000
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    Factorials of floats are OK, but the float must be an exact integer:
    >>> factorial(30.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    >>> factorial(30.0)
    265252859812191058636308480000000

    It must also not be ridiculously large:
    >>> factorial(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n too large
    """

    import math
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n+1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result
```

doctest 就是把其中的 example code 拿出做測試，檢查 docstring 是否符合規定，本文則是使用 [pytest plugin doctest-plus](https://github.com/astropy/pytest-doctestplus) 執行範例代碼測試。

---
## About base rule of writing example code

1. 預期輸出, Expected output

    當我們在範例代碼當中寫了一段程式後，如何判斷測試成功呢？就是去比對輸出結果與預期輸出結果是否相同，而預期輸出結果則是直接撰寫在 docstring 當中，如下：
    ```python
    """
    Example: 
        >>> john = {}
        >>> john['age'] = 20
        >>> print(john['age'])
        20
    """
    ```
    
    當執行 doctest 時便會去偵測 `print(john['age'])` 結果與預期的 `20` 是否相符，若相符則回傳 PASSED
    

1. 執行符號 `>>>` 後需要有一個空白鍵

    ```python
    """
    Example: 
        >>> import os
           ^
           Must have it!
    """
    ```

1. 以 `...` 區分生命週期
    
    如 `for` 迴圈
    ```python
    """python
    Example:
        >>> for a in range(10):
        ...     print(a)
    """
    ```
    `list` 展開式
    ```python
    """
    Example:
        >>> list_a = [
        ...     {...},
        ...     {...},
        ...     {...}
        ... ]
    """
    ```

---
# pytest-doctestplus 的四大優勢

## Floating point comparision

浮點數的比對常常因為環境的不同導致計算結果的小數末尾也不同 [1] [2]，




# Reference

1. [Calculation of float and double giving different results](https://stackoverflow.com/questions/30490259/using-float-and-double-for-calculation-giving-different-results)

1. [浮點樹運算:問題與限制](https://docs.python.org/zh-tw/3/tutorial/floatingpoint.html)