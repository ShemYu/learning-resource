# Pydocstyle

自動化檢查 docstyle 是否符合使用者選擇的規範，除了能提升 code quality，也能使用 Sphinx 自動化生成文件。

> 例如 : google style, numpy style, PEP 257 etc.

- [Pydocstyle documentation](http://www.pydocstyle.org/en/stable/)

# Installation

依照[官方文件](http://www.pydocstyle.org/en/stable/usage.html#installation) 使用 `pip` 安裝
```bash
$ python -m pip install pydocstyle
```

# Usage

Command line 當中直接使用 `pydocstyle` 指令針對想要檢查的目錄執行
```bash
$ pydocstyle {path_todo}
```

# Error Codes

[Docs.Error Codes](http://www.pydocstyle.org/en/stable/error_codes.html)

Error codes 主要分為四大類

1. Missing Docstrings
   > 實際缺少 Docstrings，**重要性最高**
2. Whitespace Issues
   > 不當使用空白鍵，有時會導致文件跑版，有時會導致 Doctest 出錯，有時也不影響結果，**重要性第三**
3. Quotes Issues
   > 針對撰寫 Docstrings 的區塊所使用的 `"""` (Quotes) 進行除錯，例如 Docstrings 若包含需要 Escape 的字元或 Unicode 等，由於時常會導致跑版**重要性第二**
4. Docstring Content Issues
   > 針對不當空行、排版等，有時會導致跑版，**重要性第四**

# Default convetions 

從 Configuration file 當中的 convetion 指定想遵循 (respect) 的 coding style:

- google
- numpy
- PEP 257

```ini
[pydocstyle]
convention = "Coding style u want" 
```

# Configuration

`pydocstyle` 支援 ini 型態的設置檔案，而他的優先順序如下:

- setup.cfg
- tox.ini
- .pydocstyle
- .pydocstyle.ini
- .pydocstylerc
- .pydocstylerc.ini

並從中尋找 `[pydocstyle]` 的區塊

```ini
[pydocstyle]
...
```

| Configuration options | Description                                                      |
| --------------------- | ---------------------------------------------------------------- |
| convention            | 指定想要遵循的 code style<br> - google<br> - numpy <br> - PEP257 |
| select                | 挑選要偵測的 error codes                                         |
| ingore                | 挑選要忽略的 error codes                                         |
| add-select            | 在原有的 error codes list 增加想偵測的 error codes               |
| add-ignore            | 在原有的 error codes list 增加想忽略的 error codes               |
| match                 | 藉由正則 match 需要執行 pydocstyle 檢查的檔案                    |
| match                 | 藉由正則 mathc 需要執行 pydocstyle 檢查的目錄              檢查的目錄 |