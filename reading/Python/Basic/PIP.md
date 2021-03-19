# PIP install 入門

`pip` 是 Python standard module 之一，主要用來做 module 相關的工作，例如最常用的 `pip install` 就是用來安裝 module 的 command；`pip freeze > requirements.txt` 用來將現在環境當中安裝的套件及版本匯出至 `requirement.txt` 當中。   
pip 的安裝是藉由使用者給的 module name，從 [pypi server](https://pypi.org/) 上搜尋同名稱的 module 進行下載安裝，使用者也能藉由 options 更換成不同的 pypi server。

> ## [Pypi server](https://zh.wikipedia.org/wiki/PyPI)
> PyPI（英語：Python Package Index，簡稱PyPI）是Python的正式第三方（ official third-party）軟體包的軟體存儲庫，它類似於CPAN（Perl的存儲庫）。一些軟體包管理器例如pip，就是默認從PyPI下載軟體包。用戶通過PyPI可以下載超過235,000個Python軟體包。
## 常用指令

- 安裝 Install
    
    ```bash-
    $ pip install {module_name}
    ```
- 更新 Update
    
    ```bash
    $ pip install -U {module_name}
    ```
- 安裝指定版本 Select version
    
    ```bash
    $ pip install -v {module_name}=={version}
    ```
- 解除安裝 Uninstall

    ```bash
    $ pip uninstall {module_name}
    ```
- 列出已安裝的 module

    ```bash
    $ pip list
    ```
- 匯出已安裝 module 到指定檔案

    ```bash
    $ pip freeze > {file_name}
    ```
    file_name 通常命名為 requirements.txt

- 從 ```pip freeze``` 匯出的檔案安裝 module

    ```bash
    $ pip install -r {file_name}
    ```

## Reference

1. [【Python教學】pip install 指令大全](https://www.maxlist.xyz/2019/07/13/pip-install-python/)