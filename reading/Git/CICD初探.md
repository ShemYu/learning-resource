# CICD 

# Abstract 

## CICD 是什麼

### 持續整合
部屬於版控上，能在開發者進行特定行為時，    
自動觸發的**行為流程**。    
這些**行為流程**其中常包括包裝、測試、部屬等流程，    
目的是達到自動化的**持續整合**，   
也降低人工重複繁瑣且無意義的流程。

## CICD 如何運行的
在各 CI 框架指定的 yaml file 當中部屬 CICD 相關配置，    
並藉由該框架為基礎之 Docker 作為 runner 去執行，    
藉由 docker in docker 的方式，    
讓 runner 去部屬並執行 CICD 流程。


## CI 中的幾個單位
CICD 部屬的每個階段都稱為一個 `Stage`，   
每個 Stage 當中可以有許多獨立，可併行的 `Step`。   
每個 Stage 都可以藉由 `dependence` 去選擇依賴的 `Stage`，   
在依賴的 `Stage` 尚未結束前不能執行。

