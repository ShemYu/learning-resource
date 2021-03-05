# Pytest 測試實戰
###### Brian Okken 著
---
# Abstract

## What is Pytest, Why Pytest

[Pytest](https://docs.pytest.org/en/3.0.1/contents.html) 是一款 Python 的測試框架，而 [Pytest-cov](https://pypi.org/project/pytest-cov/) 則是 Pytest 的一個 Plugin，提供測試覆蓋度相關，方便的功能模組。

Pytest 有以下幾項優點：

1. 簡單編寫

    原生 assert 的運用

    ```python
    # Pytest
    assert a == b
    # unittest
    self.assertEqual(a, b)
    ```

1. 可讀性強

1. 易上手

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

- 從指定目錄偵測偵測測試程式並執行，若未指定則是從根目錄開始偵測

    - 偵測方式 : 
        
        從當前目錄底下搜尋 ```test_``` 開頭或是 ```_test``` 結尾之測試程式檔案進行測試
        

    ```bash
    $ pytest {Options} {test_path}
    ```

- 指定目錄

    透過```::```指定程式當中的方法或類別，可同時指定多個目錄或檔案

    ```bash
    $ python {*.py or path/u/want}::{function_name or ClassName}
    ```
    或甚至指定類別當中的特定方法
    ```bash
    $ pytest {*.py or path/u/want}::{ClassName}::{function_of_the_Calss}
    ```
    例如
    ```
    $ pytest tests/creature/animal.py::Dog::eat
    ```


- Options of pytest

    |Options |Description|
    |---|---|
    |--collect-only| 不實際執行測試，而是依據命令先行列出全部會執行的**測試程式**|
    |-v, --verbose| 印出詳細測試細節|
    |-k| 使用給訂的 substring 去查找所有 functions, classes 當中，<br>名稱包含該 substring 的執行測試，可使用 and, or, not 等基本邏輯閘<br>例如 : ```pytest -k "asdict not defaults"```|
    |-m| 指定運行藉由 pytest decorator 自定義的標籤底下之測試程式，有別於目錄可用自定義的維度橫向串聯測試方法<br>例如 : ``` pytest -m project_1``` 會執行藉由 ```@pytest.mark.project_1``` 標記的測試方法 |
    |-x, --exitfirst| 測試進行中只要出現 **FAILED** 便停止測試|
    |--maxfail=num| 測試進行中只要出現之 **FAILED** 達到門檻值 num 便停止測試|
    |--capture=(no or sys or fd)| no : 關閉所有輸出的擷取<br>sys : 擷取 sys.stdout/stderr<br>fd : 當 file descriptor 為 1 or 2 則輸出至臨時文件|
    |-s| --capture=no 的縮寫|
    |--lf, --lastfailed| 上一輪測試失敗的優先測試，且若失敗後停止測試|
    |--ff, --failed-first| 上一輪測試失敗的優先測試，且運行全部其他測試|
    |-q, --quiet| 簡化輸出結果，與 -v 效果相反|
    |-l, --showlocals| 顯現局部變數以及他的值，詳細列出測試錯誤可能的點跟原因|
    |--tb=style|style 分為以下六種 : <br>1. `--tb=no` : 不印出任何錯誤回朔信息<br>2. `--tb=line` : 印出程式碼行號<br>3. `--tb=short` : 印出摘要型的錯誤回朔信息<br>4. `--tb=long` : 印出最為詳細的錯誤回朔信息<br>5. `--tb=auto` : 僅印出第一個及最後一個錯誤的詳細錯誤回朔信息<br> 6. `--tb=native` : 僅輸出 Python 標準庫錯誤回朔信息|
    |--duration=N| 會印出 N 個耗時最久的測試，及其階段 (call, setup, teardown)|
    |--version| 印出 pytest 版本|
    |-h, --help| 印出 pytest help 資訊|

<br>

- Setting default options

    [pytest.ini](https://docs.pytest.org/en/stable/customize.html) 可在 .ini 中 `[pytest]` 底下 `addopts` 設置預設的 options
    ```ini
    # pytest.ini
    [pytest]
    minversion = 6.0
    addopts = -ra -q
    testpaths =
        tests
        integration
    ``` 


---
## 測試目錄結構

為了便於維護，測試目錄結構應與被測試之 Module 相對應。

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

Pytest 會逐測試程式當中每個 function ，依照測試結果標記為以下六種結果類別：
|Type|PASSED|FAILED|SKIPPED|XFAIL|XPASS|ERROR|
|---|---|---|---|---|---|---|
|Description| 通過測試| 未通過測試| 跳過測試| 預期測試未通過<br>且測試未通過| 預期測試未通過<br>但測試通過| 測試用例以外的代碼觸發了錯誤|

<br>

### **skip**
```python
@pytest.mark.skip(reason="not done")
def test_function_1():
    do something
```
### **skipif**
```python
@pytest.mark.skipif(version < "0.2.0", reason="not support until ver. 0.2.0")
def test_function_2():
    do something
```

### **xfail**
預期測試失敗，例如想測試是否輸入錯誤的變數型態、
```python
@pytest.mark.xfail(reason="not done")
def test_function_1():
    do something
```

也由於 XPASS 的定義較為模糊，可以在 pytest.ini 中設定為嚴格模式，將 XPASS 視為 FAILED。
```ini
[pytest]
xfail_strict=true
```

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

## Parametrized testing

When testing some method should repeatly call the same method, you can use pytest decorater `@pytest.mark.parametrize` to loop the same method with different parameters.

當有些較為繁瑣，必須重複執行的測試，需要藉由 testcase 完整覆蓋測試邏輯時，可以藉由 `@pytest.mark.parametrize` 對同一個 method 迴圈輸入指定的參數。

```python
import ptest
@pytest.mark.parametrize('num', [1, 2, 3, 4, 5, 6, 7, 8, 9])
def test_is_odd(num):
    assert num%2 == 0
```

You can assign multi arguments for sure.

當然也可以輸入多個參數。

```python
@pytest.mark.parametrize('num1, num2', 
                        [
                            (1, 2),
                            (3, 4),
                            (5, 6)
                        ]
                        )
def test_add(num1, num2):
    assert add(num1, num2) == num1+num2
```

## Fixture 

fixture 是提供 pytest 測試前後配置的模塊，提供完整的測試配置、銷毀方法，一班藉由裝飾器 `@pytest.fixture()` 調用，也可以設置在 project/tests/conftest.py 當中。

conftest.py 也可以不只存在一個，conftest 生命週期為其所在位置之子目錄，可以把其視為該層級底下之 fixture 倉庫。


# Configuration of pytest

pytest 的預設 configurations file 優先序依照以下排序:
