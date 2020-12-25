# What is `black`

在了解 black 之前應該先明白 coding style 的重要性，除了前文 pydocstyle 當中的簡述，也可以參考以下文章，Why formatting your code is important 環節，當中提及的四大重點除了前文提及的**合作**以外，還有**可讀性**、**除錯**甚至用於未來面試，你的 code 都匯給人較好的印象。
 
> ### [How to auto-format your code with black](https://www.freecodecamp.org/news/auto-format-your-python-code-with-black/)

而 black 是一款針對 coding style 自動化偵測並修正的 coding style module，psf/black/README.md 提到:

> By using Black, you agree to cede control over minutiae of hand-formatting. In return, Black gives you speed, determinism, and freedom from pycodestyle nagging about formatting. You will save time and mental energy for more important matters.

意即「使用 Black 最大的意義在於省下你的時間，並讓你把它用在更有意義的事情上」

# Why not Pylint or flake8

## Pylint
Pylint 是最為嚴格、嚴謹，在 code smell 層級開始尋找可能由 coding style 引起的潛在錯誤，設置上也最為複雜、彈性最大，報告詳細，從 type error, recommend suggestions about refactored 到 code's complexity，詳盡的分析出所有細節，也因為他只分析錯誤，不提供 auto reformat，手動修正錯誤的成本往往是不選擇 pylint 的一大原因。

## Flake8
Flake8 相較 Pylint 最大的優勢在於更簡單的錯誤回報，針對輕量化程式的主軸去減少 `unused import`, `unused variable` 以及針對 code convention `Undefined name`, `not idented` 等問題重點回報，錯誤數量相較 pylint 重點化很多，如果 flake8 的預設判斷門檻符合專案需求，往往 open source project 就會選擇 flake8 作為 coding style 的除錯 module，原因就在於 flake8 在時間成本、結果上的平衡性。

## Black
本文主角 Black 的最大優勢在於，他相較 Pylint, Flake8 除了更為簡單、快速外，他還擁有 auto-reformat 的功能，讓時間成本直接接近於 0，但反之他也是三者中錯誤偵測數量最為簡單的。

| module | 報告詳細程度 | 時間成本 | 修正錯誤方式 | 設置彈性 | 優勢                           | 劣勢                                                                                                                                   |
| ------ | ------------ | -------- | ------------ | -------- | ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------- |
| Pylint | 高           | 高       | 手動         | 高       | 從 code smell 層級找到潛在錯誤 | 設置複雜因此學習成本較高，若需求與 default 配置相差太大，設置時間成本就隨之增加                                                        |
| flake8 | 中           | 中       | 手動         | 中       | 時間成本跟結果三者中最為平衡   | coding style 屬於不用這麼嚴謹的錯誤偵測，flake8 的方式比較像是一般程式 error message，雖然錯誤數量不多，但仍會有需要修正全部錯誤的方式 |
| black  | 低           | 低       | 自動         | 低       | 時間成本最低，自動化修正錯誤   | 錯誤的細節最少，雖然自動化修正，但是 auto-reformat 的正確性有待商榷 |

# Installation

> black - [#Installation](https://github.com/psf/black#installation)
```bash
$ pip install black
```

# Usage
> black - [#Usage](https://github.com/psf/black#usage)
```bash
# check
$ black --check {source}
Check reports ...
# auto reformat
$ black {source}
```

# Reference

1. [Black - github](https://github.com/psf/black)
2. [How to format your code by black](https://www.freecodecamp.org/news/auto-format-your-python-code-with-black/)