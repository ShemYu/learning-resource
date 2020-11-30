# Anaconda 入門基礎知識

[Anaconda 官網](https://www.anaconda.com/products/individual)安裝最新版本。

## 版本查詢
```bash
$ conda -V
conda 4.9.2
```
若要更新 conda 版本及其內建 module
```bash
conda update conda
```

---
## 虛擬環境
### 創建
```bash
$ conda create --name {env_name} python={python.version}
```
- env_name

    Customize env_name for ```activate```.

- python.version

    Python version you want to create.

### 啟動
```bash
$ activate {env_name}
```

### 查詢
```bash
$ conda env list
```
列出所有已創建的虛擬環境資訊

### 刪除
```bash
$ conda env remove --name {env_name}
```
刪除指定的虛擬環境

---
## module

基本上就是以 ```conda``` 取代 ```pip```

### 安裝
```bash
$ conda install {module_name}
```

### 解安裝
```bash
$ conda remove --name {env_name} {module_name}
```