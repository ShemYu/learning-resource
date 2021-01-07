# 略過簡單、繁瑣的自動化工作

# Abstract 

執行 Coding style 的檢查由於嚴重性並非特別大，因此往往在合作開發時被視為一件**麻煩**的工作，若建置在 CI/ CD 流程上，又會導致以嚴格標準審核(任何錯誤都導致 CI 流程中止) Coding style。

[Pre-commit](https://pre-commit.com/#intro) 會在使用者執行 `git commit` 時，讀取使用者自定義的 `yml` file，自動執行簡單、繁瑣的工作，且 pre-commit, pre-commit-hooks 已經提供大部分 repos 常使用的 Code quality 相關 framework，讓 Contributing 的流程變得更自動化，不再需要記住需執行的檢查步驟等。

# Installation

Using pip:
```bash
$ pip install pre-commit
```
Check if installation is successed:
```bash
$ pre-commit --version
```
# Usage

pre-commit 的運作邏輯是藉由設定的 Configuration，將 framework 安裝至 git hooks 當中，當開發者運行 `git commit` 時便會觸發並執行 framework

而其中 `pre-commit-hooks` 已經包裝了大部分常用的 framework，也有許多 Coding style formatter 有提供自己的 pre-commit 功能，也可以在，也可以在

pre-commit 的使用方法也非常簡單，建置一個 Configuration file 來告訴它，在每次使用者 `git commit` 時應該檢查些什麼
```yml
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v2.3.0
    hooks:
    -   id: check-yaml
    -   id: end-of-file-fixer
    -   id: trailing-whitespace
-   repo: https://github.com/psf/black
    rev: 19.3b0
    hooks:
    -   id: black
```
設定好 Configuration 後，執行指令將這些 framework 安裝在 git hooks 當中
```bash
$ pre-commit install
```
接下來當使用者執行 git commit 的同時，便會一起執行 hooks 當中所安裝的所有 framework 檢查

# Common practice

由於 Coding style 屬於一種撰寫程式的好習慣，因此觀察有名的大型多人專案，就可以學習他們合作的 common practice

Pandas 的 pre-commit-yaml 就設定的非常複雜，藉此在 `git-commit` 的同時多做些檢查，確保代碼品質

scikit-learn 僅執行 flake8、mypy 及一些文檔檢查，設置相較 Pandas 簡單許多

Pytorch 則是使用 isort、mypy 做 auto reformat

Numpy, Snorkel, Allennlp 則沒有使用 pre-commit

> [pre-commit-config.yaml of Pandas](https://github.com/pandas-dev/pandas/blob/master/.pre-commit-config.yaml) 
> 
> [pre-commit-config.yaml of scikit-learn](https://github.com/scikit-learn/scikit-learn/blob/master/.pre-commit-config.yaml)
> 
> [pre-commit-config.yaml of pytorchlighting](https://github.com/PyTorchLightning/pytorch-lightning/blob/master/.pre-commit-config.yaml)


# 

# Reference

1. [提升程式碼品質：使用 Pre-Commit (Git Hooks)](https://mropengate.blogspot.com/2019/08/pre-commit-git-hooks_4.html)
2. [Intro - pre-commit](https://pre-commit.com/#intro)
3. [pre-commit-hooks - github](https://github.com/pre-commit/pre-commit-hooks)
   