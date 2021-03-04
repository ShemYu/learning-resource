# PIP install 入門

## 常用指令

- 安裝 Install
    
    ```bash
    $ pip install {module_name}
    ```
- 更新 Update
    
    ```bash
    $ pip install -U {module_name}
    ```
- 安裝指定版本 Select version
    
    ```bash
    $ pip install -v {module_name}=={version}
    ```
- 解除安裝 Uninstall

    ```bash
    $ pip uninstall {module_name}
    ```
- 列出已安裝的 module

    ```bash
    $ pip list
    ```
- 匯出已安裝 module 到指定檔案

    ```bash
    $ pip freeze > {file_name}
    ```
    file_name 通常命名為 requirements.txt

- 從 ```pip freeze``` 匯出的檔案安裝 module

    ```bash
    $ pip install -r {file_name}
    ```

## Reference

1. [【Python教學】pip install 指令大全](https://www.maxlist.xyz/2019/07/13/pip-install-python/)