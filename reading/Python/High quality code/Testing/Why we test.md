# Why we testing

## Abstract 

測試在開發環節當中我認為是可小可大，小從簡單驗證預期書出結果，大至開發模式規模的測試。但不論何種測試，都是對程式穩定性有保證，且大大提升可靠度，好的測試我個人認為甚至是可以增加開發效率。

## 測試框架

Python 官方有提供測試框架 unittest，但測試語法需繼承測試類別，再用類別方法 assertTrue, aasertFalse。

Pytest 提供開源、容易上手的語法，且不同於 unittest 使用自定義方法進行檢查輸出結果，Pytest 使用原生的斷言 `assert` 進行判斷。且 Pytest 開源，因此相關插件資源豐富。