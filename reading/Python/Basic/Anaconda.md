# Anaconda basic

# Abstract

`Anaconda`(一般也簡稱 `conda`) 是 Python 的虛擬環境的框架之一，特色在於 conda 會把環境建置在系統目錄當中，而非一般虛擬環境建構於專案目錄之下，相比之下 conda 環境移植性較好，但獨立性也較差。

優勢:
- 環境移植性高   
  跨專案共用環境時很方便
- 易用性高   
  經整合專案
缺點:
- Conda 虛擬環境較為肥大
> [缺點補充文獻: 還我乾淨環境！怒砍Anaconda ! 手動移除windows Anaconda 殘留檔案！](https://medium.com/%E8%AA%A4%E9%97%96%E6%95%B8%E6%93%9A%E5%8F%A2%E6%9E%97%E7%9A%84%E5%95%86%E7%AE%A1%E4%BA%BAzino/%E9%82%84%E6%88%91%E4%B9%BE%E6%B7%A8%E7%92%B0%E5%A2%83-%E6%80%92%E7%A0%8Danaconda-%E6%89%8B%E5%8B%95%E7%A7%BB%E9%99%A4windows-anaconda-%E6%AE%98%E7%95%99%E6%AA%94%E6%A1%88-666d88eae69d)
  
> ## 虛擬環境是什麼
> 一般程式都是在系統環境下執行，倘若在同個系統開發多個專案，使用許多不同的 module 進行開發，便會無法區分這些專案分別相依於哪些 module，且可能發生套件(module)衝突。    
> 使用虛擬環境是進行開發的基本觀念，不管是不是使用 conda，只要使用了基本的虛擬環境框架(virtualenv, pyenv, ...) ，就可以在獨立環境下開發專案外，也能輕鬆匯出相依套件(例如 python 常用的 requirements.txt)

# Installation
## Windows 
從 [Anaconda 官網](https://www.anaconda.com/products/individual)下載並安裝最新版本。

## Linux, MacOS
使用 `brew` 安裝
```bash
$ brew install anaconda
```

## Check version
```bash
$ conda -V
conda 4.9.2
```
若要更新 conda 版本及其內建 module
```bash
conda update conda
```

---
## Virtual environment [CRUD](https://zh.wikipedia.org/wiki/%E5%A2%9E%E5%88%AA%E6%9F%A5%E6%94%B9)
### Create
### Basic


Create by env_name, and specific python.version(optional)
```bash
$ conda create --name {env_name} python={python.version}
```
- env_name

    Activate environment

    ```bash
    # Win
    $ conda activate {env_name}
    # Linux, MacOS
    $ source activate {env_name}
    ```

- python.version

    Python version you want to create.

### Create from yml.file
```bash
$ conda env create -f environment.yml
```
- example of yml file

    ```yml
    name: name-of-env
    channels:
    - defaults
    - conda-forge
    dependencies:
    - ipykernel   # must have for every env
    - cudatoolkit=10.1
    - python=3.8
    - pip
    - pycurl
    # What ever you wnat
    ```
> ## Note
> 預設創建環境的方法，使用 `conda create`，     
> 使用 yaml 則是使用 `conda env create`。    

### Create to specific path
This method could create the virtual environment in a specific path or in project.
```bash
$ conda create --prefix ./envs
```

- activate

    ```bash
    $ conda activate ./envs
    $ source activate ./envs
    ```

### Activate 啟動虛擬環境
```bash
$ activate {env_name}
```

### List all environments
```bash
$ conda env list
```
列出所有已創建的虛擬環境資訊

### Delete env.
```bash
$ conda env remove --name {env_name}
```
刪除指定的虛擬環境

---
## Install package

基本上就是以 ```conda``` 取代 ```pip```，     
但建議**盡量使用pip**安裝 Package 確保套件的完整性與正確性。

### Conda install
```bash
$ conda install {module_name}
```

### Conda remove

刪除指定環境底下的 module
```bash
$ conda remove --name {env_name} {module_name}
```