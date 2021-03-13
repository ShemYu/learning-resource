# 解決 macos 底下 `python` 指令使用 python2.7 的問題

首先通過以下文章了解到問題成因：
> 我們來查看 /usr/local/bin 目錄下，你會發現並沒有 Python 3 提供的 python 可執行檔，而只有 python3 執行檔，因此當你輸入 python 時， Mac 因為來到 /usr/local/bin 目錄下沒有找到 python 可執行檔，才會保持原先的狀態，近一步往下一個位置找，並找到內建的版本，直接使用內建的 python 2.7。
> ##### [Python - 安裝 Python3 在 Mac 上 (Python 3.6.5 為例）](https://note.koko.guru/python-install-python3-on-mac.html)

換句話說就是因為抓不到 `./bin/python`，因此系統自作主張從 `/usr/bin/` 底下找到了內建的 `Python2.7` 來使用，導致了這個錯誤。    
因此若要修正他，僅需把當前裝置上的 Python3 路徑找到，並將所在的 `../bin` 加入環境變數 `$PATH` 當中，便能解決此問題。


# Referenece 

1. [How to switch between python 2.7 to python 3 from command line?
](https://stackoverflow.com/questions/18058389/how-to-switch-between-python-2-7-to-python-3-from-command-line)