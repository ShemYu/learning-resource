# Pytest 測試實戰
###### Brian Okken 著
---
# Abstract

## What is Pytest, Why Pytest

一個強大好用的 Pytest 測試用 module

1. 可讀性強

1. 易上手

1. 簡單編寫

1. 原生 assert 的運用，相較 unittest 彈性許多

1. 可以運行 unittest, nose 撰寫的測試程式
---
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
---
## 執行

直接執行 ```pytest``` 會從當前目錄及子目錄搜尋 **test_** 開頭或 **_test** 結尾的測試函數進行測試
```bash
$ pytest
```
亦可指定測試程式/目錄，以及透過```::```指定欲測試的方法或類別
```bash
$ python {*.py or path/u/want}::{function_name or ClassName}
```
或甚至指定類別當中的特定方法
```bash
$ python {*.py or path/u/want}::{ClassName}::{function_of_the_Calss}
```
也可透過關鍵詞
---
## General naming rules

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
---
## Testing result type

測試結果分為以下四種
||Passed| Failed| xFailed| xPassed| Skipped|
|---|---|---|---|---|---|
|說明| 通過| 失敗|預期會失敗<br>且結果失敗| 預期失敗<br>但結果通過| 跳過|

---
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
---
## Expecting Exception

當有一些測試我們想以預期特定 input 會帶來特定 Exception 時，可以藉由預期錯誤的方式去撰寫測試。

```python
with pytest.raise(ValueError):
    do_something_wont_cause_valueerror()
```

上述範例藉由 ```pytest.raise(ValueError)``` 來保證會造成 ```ValueError```，當該測試回傳其他錯誤時，就與預期不相符，表示**測試失敗**。

```python
def test_of_something():
    with pytest.raise(ValueError) as excinfo:
        do_something_u_except_will_cause_ValueError()
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "Error message u expect"
```

上述範例利用 ```with``` 字句抓取測試時遇到 ```ValueError``` 的情況，儲存資訊至 excinfo 並從 value 當中取出 error message，最後利用 ```assert``` 字句比對是否是期望的失敗結果。
---
## Keyword testing

依據指定 keyword 進行測試

```bash
$ pytest -k _raise
```

上述指令會找到測試名稱包含 '_raise' 的方法進行測試

# Pytest coverage

## Abstract

