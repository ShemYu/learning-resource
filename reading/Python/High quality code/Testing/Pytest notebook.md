# 如何針對 jupyter notebook 進行單元測試

調研一些框架後，個人選擇使用 [nbval](https://github.com/computationalmodelling/nbval)，原因比較之後發現該框架的實作、測試邏輯與 `doctestplus` 最為相近，因此在調研到實作之間不須學習新邏輯。例如要針對 `.ipynb` 進行測試，僅須在以 options 的形式實踐。

```bash
$ pytest --nbval path/to/test
```

安裝透過 pip 就不再贅述。`nbval` 的測試邏輯是依據使用者執行過的 input 作為輸入，實際運行後將 stdout 比對使用者先前執行站存的 output 做為測試模式。    
且在比對時，也可以藉由客製化的 `sanitize_file` 正規化 stdout 結果進行比對，例如將 a-z 視為同一字串、1-9 視為統一數字等。

```bash
[Section1]
regex: [a-z]*
replace: abcd

regex: [1-9]*
replace: 0000

[Section2]
regex: foo
replace: bar
```

不僅如此，他也可透過 `assert` 語法進行測試，整體邏輯十分通順。

而測試的基本單元則是以 notebook 當中，有撰寫程式碼的 `Cell` 為單位進行測試與結果評判。

```bash
FAILED tutorials/Data Preprocessing/data_preprocessing.ipynb::Cell 1
FAILED tutorials/Data Preprocessing/data_preprocessing.ipynb::Cell 2
FAILED tutorials/Data Preprocessing/data_preprocessing.ipynb::Cell 3
FAILED tutorials/Data Preprocessing/data_preprocessing.ipynb::Cell 6
FAILED tutorials/Data Preprocessing/data_preprocessing.ipynb::Cell 7
FAILED tutorials/Data Preprocessing/data_preprocessing.ipynb::Cell 10
FAILED tutorials/Data Preprocessing/data_preprocessing.ipynb::Cell 13
FAILED tutorials/Data Preprocessing/data_preprocessing.ipynb::Cell 15
FAILED tutorials/Data Preprocessing/data_preprocessing.ipynb::Cell 18
FAILED tutorials/template/tutorial_template.ipynb::Cell 1
FAILED tutorials/Data Preprocessing/data_preprocessing.ipynb::Cell 21
FAILED tutorials/Data Labelling/data_labelling.ipynb::Cell 8
```

預設使用 notebook 運行時配置的環境，但可透過 `--current-env` 指定為當前環境。

```bash
$ pytest --nbval --current-env path/to/test
... (test with current enviroment)
```

稍有美中不足的部分，目前遇到的是該框架的 document 較為簡陋，也沒有 Configuration, Options 相關說明，蠻多資料需要從 issue reported 當中結果去調研，是較為需要花時間的部分。

結果上來說，該框架引入以 `pytest`, `tox` 等框架為基礎之測試模組，是十分順暢無痛。

> ## Py.test plugin for validating Jupyter notebooks
> The plugin adds functionality to py.test to recognise and collect Jupyter notebooks. The intended purpose of the tests is to determine whether execution of the stored inputs match the stored outputs of the .ipynb file. Whilst also ensuring that the notebooks are running without errors.

