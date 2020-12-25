# Pylint

# What is Pylint

> It's not just a linter that annoys you! - 《[Pylint documentation](https://github.com/PyCQA/pylint)》

Pylint 是一款從各種 coding style 之細節去偵測錯誤的 Python linter module。且良好的設置彈性更提供 Pylint 在經過調整後更貼近每個專案開發者習慣的 coding style 檢查，也因此相對來說一開始須付出的時間成本最高。

Pytlint 除了嚴謹、詳細的特色外，他的 reports 也是最為精確詳細的，從錯誤的位置類型 (module, class, method, function) 到統計 code, docstring, comment, empty 在專案中的分布，在依據 Pylint 規範的五大錯誤中的四種統計專案中各 module 錯誤的類型、占比等等，詳細的了解 Pylint reports 在提升專案 code quality 的維度上絕對有充分的資訊。

Pylint 還有一個小特色是他會幫專案目前的結果打分，也因此 CI 部屬階段可以藉由打分撰寫一支子程式，若檢測後分數達門檻則通過，若否則不通過。

# Installation

```bash
$ pip install pylint
```

# Usage

直接於專案執行 Pylint
```bash
$ pylint {source_path}
```

-j, --jobs=n 指定 n 個 worker 同步執行 Pylint 加速分析
```bash
$ pylint -j=5 {source_path}
```

> Note: Pylint 從 2014 年的版本起便一直有使用 -j 影響分數的問題，單執行緒與多執行緒算分結果不一，但統一標準(使用單或多執行緒) 便不影響使用 - 《[Issue: Different output with --jobs=1 and --jobs=2](https://github.com/PyCQA/pylint/issues?q=is%3Aissue+is%3Aopen+-j)》

若想客製化的設置 Pylint，需先生成 Configuration file，filename 預設搜尋順序 - [Pylint docs #Command line options](https://docs.pylint.org/en/1.6.0/run.html#command-line-options):

1. pylintrc in the current working directory
1. .pylintrc in the current working directory
1. If the current working directory is in a Python module, Pylint searches up the hierarchy of Python modules until it finds a pylintrc file. This allows you to specify coding standards on a module-by-module basis. Of course, a directory is judged to be a Python module if it contains an __init__.py file.
1. The file named by environment variable PYLINTRC
1. if you have a home directory which isn’t /root:
    1. .pylintrc in your home directory
   1. .config/pylintrc in your home directory
1. /etc/pylintrc

```bash
pylint --generate-rcfile > {filename}
```

> Pylint 許多 command line options 都能在 configuration files 當中找到對應的欄位設置

Command line
```bash
pylint -j 5 -r y -f colorized {source_path}
```
Configuration
```ini
[MASTER]
...
# Use multiple processes to speed up Pylint. Specifying 0 will auto-detect the
# number of processors available to use.
jobs=5 # -j=5
...
[REPORTS]
...
# Set the output format. Available formats are text, parseable, colorized, json
# and msvs (visual studio). You can also give a reporter class, e.g.
# mypackage.mymodule.MyReporterClass.
output-format=colorized # -f=colorized

# Tells whether to display a full report or only the messages.
reports=yes # -r=y
...
```

# Error types or pylint

Pylint 錯誤分為以下五種

| Error types  | Description                                                                                                                             |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------- |
| R, refactor  | “good practice” metric violation<br>建議養成的好習慣，通常是可能發生錯誤的 code smell                                                   |
| C, convetion | coding standard violation<br>建議符合的 coding style，提升代碼合作品質                                                                  |
| W, warning   | stylistic problems, or minor programming issues<br>通常針對程式做一些靜態檢查產生的錯誤(動態生成的物件會被判斷為錯誤)，或代碼長度太長等 |
| E, Error     | important programming issues (i.e. most probably bug)<br>較為嚴重的錯誤較為嚴重的錯誤                                                   |
| F, Fatal     | errors which prevented further processing                                                                                               |
