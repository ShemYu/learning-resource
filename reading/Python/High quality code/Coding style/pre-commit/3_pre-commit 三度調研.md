# Pre-commit

## 釐清 Pre-commit framework / git hooks pre-commmit phase

## 1. Git hooks pre-commit phase

Git hooks 當中用來掛在 commit 前執行用的 scripts。   
例如:    

- commit 前代碼風格檢查
- commit 前，篩選 staged files 是否有過大

## 2. Pre-commit framework

Python 撰寫的 framework，提供簡單的配置調用不同語言撰寫的 pre-commit scripts。    
Pre-commit framework 提供基本的 hooks script [pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks) 有許多常用、基本的方法可以調用     

Pre-commit 提供的基本配置可以使用 repo keyword 藉由 url 引入 pre-commit 配置     
例如常用來檢查、修正 Coding style 的 `isort`, `black`, `flake8`

``` yaml
repos:
-   repo: https://github.com/pre-commit/mirrors-isort
    rev: ''  # Use the revision sha / tag you want to point at
    hooks:
    -   id: isort
-   repo: https://github.com/psf/black
    rev: 19.10b0 # Replace by any tag/version: https://github.com/psf/black/tags
    hooks:
    -   id: black
        language_version: python3 # Should be a command that runs python3.6+
-   repo: https://gitlab.com/pycqa/flake8
    rev: ''  # pick a git hash / tag to point to
    hooks:
    -   id: flake8
        exclude: ^notebooks/|^data/
```

也提供調用自己撰寫的 local script，藉由程式執行的 status code 去分辨 `PASSED` or `FAILED`

``` yaml
-   repo: local
    hooks:
    -   id: test_local_script
        name: Test local script
        language: python
        entry: python scripts/test.py
```

Pre-commit 通常都會設置一些較為輕量的檢查，不要過於嚴謹而導致 commit 速度受到阻礙

---
## Pre-commit 移植性

可以撰寫專門用來給 Pre-commit 引用的 repo，一來可以整合規範，增加可移植性，         
也由於使用 repo url 引用 pre-commit 相關檢查與修正時，會 clone repo，    
初始化環境，在 `~/.cache` 當中存下不小的環境檔案，    
因此輕量的 repo 會增加環境建置的速度

> ## Note
> [Where does pre-commit install “environments”?](https://stackoverflow.com/questions/62539288/where-does-pre-commit-install-environments)   
> `pre-commit` by default places its repository store in ~/.cache/pre-commit -- this can be configured in two ways:    
> - `PRE_COMMIT_HOME`: if set, `pre-commit` will use that location instead.     
> - `XDG_CACHE_HOME`: if set, `pre-commit` will use `$XDG_CACHE_HOME/pre-commit` following the [XDG Base Directory Specification](https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html).


### 總結來說

Pre-commit framework 有以下兩項優點:
- **提供簡單配置接口**，省略撰寫代碼也能做很主流代碼風格修正與檢查
- **跨專案移植性佳**，藉由 Repository 作為介面接口

