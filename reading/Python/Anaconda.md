# Anaconda basic

# Abstract

Anaconda(簡稱 conda) 是 Python 其中一種建構虛擬環境的方式，    
特色在於 conda 會把環境建置在系統目錄當中，     
而非一般虛擬環境建構於專案目錄之下，
相比之下 conda 環境移植性較好，
但獨立性也較差。

> 如果需求偏向跨 project 共用環境，使用 Conda 就較為適合，    
> 但是 Conda 也提供安裝於指定目錄的方法，與使用 virtualenv 的方式雷同

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
## Virtual environment CRUD
### Create
### Basic
```bash
$ conda create --name {env_name} python={python.version}
```
- env_name

    Customize env_name for ```activate```.

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
但建議**盡量使用pip**安裝 Package 

### Conda install
```bash
$ conda install {module_name}
```

### Conda remove

刪除指定環境底下的 module
```bash
$ conda remove --name {env_name} {module_name}
```