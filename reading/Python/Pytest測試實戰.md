# Pytest 測試實戰
###### Brian Okken 著
---
# Abstract

## Why Pytest

1. 可讀性強

1. 易上手

1. 簡單編寫

1. 原生 assert 的運用，相較 unittest 彈性許多

1. 可以運行 unittest, nose 撰寫的測試程式

## Test strategy

- 單元測試

    測試一段落的 code
    e.g. Class, function etc.

- 集成測試

    測試一些段落的 code
    e.g. Class, sub sysyem etc.

- 系統測試

    測試一個系統的 code，包含環境、所有 code 的測試

- 功能測試

    測試系統當中的功能運行

## 執行

直接執行 ```pytest``` 會從當前目錄及子目錄搜尋 **test_** 開頭或 **_test** 結尾的測試函數進行測試
```bash
$ pytest
```
亦可指定測試程式/目錄
```bash
$ python {*.py or path/u/want}
```

## Naming rules

1. 測試程式以 **test_** 開頭或 **_test** 結尾

1. 測試 function 以 **test_** 開頭

1. 測試之類別以 **Test** 開頭

例如 **test_eat()** 就會是針對 **eat()** 做的單元測試

而一個好維護的測試目錄結構，應與被測試之 Module 相對應。

    ├ src
    |   ├ target_module
    |       ├ __init__.py
    |       ├ package_1.py
    |       ├ package_2.py
    |
    ├ tests
        ├ test_taget_module
            ├ test_package_1.py
            ├ test_package_2.py
# More about Pytest

## Just using ```assert```

Pytest 在撰寫測試程式時，Pytest 繼承並覆寫了 Python 原生的 assert keyword 使之提供更多詳細資訊。

```python
def test_value_is_correct():
    a = get_value()
    b = 'CorrectValue'
    assert a == b
```

當 assert 判斷式回傳結果為 False 時便會判斷為測試失敗。