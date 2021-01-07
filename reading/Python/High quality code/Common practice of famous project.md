# Common practice of famous Python Library
> Note: Did they respect code quality?

調研大型的 python library，學習比較一般的代碼品質控管作法，使用的 framework，以及自動化、手動的步驟

# Pandas

提供高速、彈性且可擴充的資料結構 Dataframe 的 Python library，Pandas 在 code quality 個人認為十分嚴謹

## Testing 

- 測試框架使用 `pytest`, `pytest-cov`
- coverage 標準: 
  - each_feature: 85%
  - each_patch: 50%

## Coding style

- 使用 `flake8`, `black`, `isort`, `mypy`
- Makefile 內置 `lint-diff`
  
  ```bash
  $ gitdiff {branch} -u -- "*.py" | flake8 --diff 
  ```
- pre-commit 較為複雜

# scikit-learn

## Testing
- 使用 `pytest`, `pytest-cov` 確保測試
- 為確保 package 的順利，使用 `check-manifest` 自動化生成打包用的 `Manifest.in`
  
    ```yml
    [check-manifest]
    # ignore files missing in VCS
    ignore =
        sklearn/linear_model/_sag_fast.pyx
        sklearn/utils/_seq_dataset.pxd
        sklearn/utils/_seq_dataset.pyx
    ```

- codecov.yml 設置 codecov io 門檻

## Docs
## Coding style

- 使用 `flake8`, `mypy`, `pylint`
- 比較特別的地方是，同時使用 `flake8`, `pylint`
- `pre-commit`
  - check-yaml, end-of-file-fixer, trailing-whitespace
  - `flake8`, `mypy`


# transformers

## Testing

使用 `pytest`

## Docs

使用 Sphinx 生成文件

## Coding style

使用 `isort`, `flake8`, `black` 以及 transformers 自定義的 code quality python program
> [Makefile.extra_quality_checks](https://github.com/huggingface/transformers/blob/master/Makefile)


# Snorkel

## Testing 

`pytest`, `tox`

Coverage limit: 95%

### tox

整合 Testing, Docs, Coding style

## Docs

`pydocstyle`, `doctest`

## Coding style

`flake8`, `mypy`, `isort`, `mypy`

# PytorchLightning

使用 `check-maifest` 自動提供撰寫建議

## Testing

`pytest`, `pytest-cov`
## Docs

`pydocstyle`

## Coding style

`flake8`, `isort`, `mypy`, `autopep8`, `black`

`pre-commit`: isort, trailing-whitespace, end-of-file-fixed, mypy

> # Note
> ## Did python library which is famous respect to code quality?
> Yes, they do.  Famous python library will contributing with thousands of programer, if they don't respect to code quality, it will be pretty hard to co-work.
>
> However, they don't want to waste too much time at it.  They using formatter framework such like isort, black, mypy to fix simple problem, combine coding style without any human involement.
>
> About compare in pylint and flake8, it's a big question, let's talk about it at Coding style section's Coding style reading.

