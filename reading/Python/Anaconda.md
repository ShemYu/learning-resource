# Anaconda basic

[Anaconda 官網](https://www.anaconda.com/products/individual)安裝最新版本。

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
## Virtual environment
### Create
Basic method
```bash
$ conda create --name {env_name} python={python.version}
```
- env_name

    Customize env_name for ```activate```.

- python.version

    Python version you want to create.

Create from yml.file
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

### Run
```bash
$ activate {env_name}
```

### List all env.
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

基本上就是以 ```conda``` 取代 ```pip```，但建議**盡量使用pip**安裝 Package 

### Conda install
```bash
$ conda install {module_name}
```

### Conda remove
```bash
$ conda remove --name {env_name} {module_name}
```