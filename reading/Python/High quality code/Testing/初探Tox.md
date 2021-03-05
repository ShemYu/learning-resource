# 初探 Tox

Tox 是一款自動化測試工具，藉由虛擬環境、命令行驅動 Python 執行測試，可以單獨在 Local 端調用也可以藉由 CI 框架持續整合。    
藉由 Tox 整合測試的優勢在於多變化的環境組合，例如今天有測試多版本 python、不同資料庫的環境，假設有 **4 個版本**的 Python、**2 種**資料庫的情況下進行測試，就可以組合出 $4×2=8$ 種組合，若逐一手動建置環境，部屬上十分繁瑣，部屬出來的環境也很龐大，甚至在執行測試時需要冗長的代碼來執行。

若使用 Tox 建置環境，僅須透過 keyword 就可指定測試環境組合，組出你想要測試的環境。例如:

```bash
# 透過 -e 指定想要的環境名稱
$ tox -e {py36, py37, py38, py39}-unittest
py36-unittest ...
py37-unittest ...
py38-unittest ...
py39-unittest ...
```

即可對應到你配置 Configuration 當中的環境:

```toml
[testenv:{py36, py37, py38, py39}-unittest]
description = unittest from py36 to py39
deps = 
	pytest
	pytest-doctestplus
	pytest-xdist
	pytest-cov
depends = 
commands = 
	python -V
	python -m pip install .
	python -m pytest path/to/tests/
```

其中 `deps` 可以指定該環境需要預先安裝的 modules，`commands` 則代表該環境會執行哪些命令進行測試。

> ## [Tox documentation](https://tox.readthedocs.io/en/latest/)
