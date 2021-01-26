# Pre-commit 官方文件調研

> [Pre-commit - Intro](https://pre-commit.com/#intro)

# Abstract

本次調研主要想解決以下疑問:

1. Confguration 彈性

1. Pre-commit vs Makefile 

1. 能否做到針對 commit file，執行例如檔案

# Flexity of pre-commit's configurations

Pre-commit 預設的 configuration file 位置是 `root` 底下之 `.pre-commit-config.yaml`

創建好 `.pre-commit-config.yaml` 便可在內撰寫想設置的 hooks 或相關設置

Example configs:
```yml
repos: # top-level
-   repo: https://github.com/pre-commit/pre-commit-hooks # clone pre-commit-hooks repo
    rev: v2.3.0 # 設定欲使用的版本(git tags)
    hooks: # 設定要使用 hooks id
    -   id: check-yaml 
    -   id: end-of-file-fixer
    -   id: trailing-whitespace
-   repo: https://github.com/psf/black # clone black repo
    rev: 19.3b0 
    hooks:
    -   id: black
```

Pre-commit 設置較為豐富，彈性也很大，但須注意執行的 hook script 會影響每次執行 commit(或是設定成 Push 等)

> ## Note:
> 使用 flake8 進行代碼風格檢查時須注意，exclude files 相關設置需配置於 .pre-commit-config.yaml 當中。其他配置則會去使用**已經commit**的 configrations。

# Pre-commit vs Makefile

並不衝突 pre-commit 是針對 Staged changes 快速檢查修正，減少每次版本發布時累積的技術債，而 Makefile 則是針對整體檢查進行簡單的 cmd 指令集合，簡單化操作。

# Only check or fix the files staged change

Pre-commit 預設便是僅針對 Git Staged Changes 進行修正