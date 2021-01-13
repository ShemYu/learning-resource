#  不用懂git也能用GitHub Pages架設靜態網站並綁定網域

藉由 github repository 架設靜態網頁

步驟:

1. 建立一個乾淨的 repo
2. Github 設定內，使用 git pages 功能鍵立預設模板    
   再改成自己的內容
   此時已可透過 repo io 網址連接到你的網站   
   `https://{account}.github.io/{repo name}/`
3. 回到設定內的 git pages，綁定申請好的網域名稱
4. Clone repo
5. 在 Domain 供應商，設定 DNS server 相關資料
6. 部屬上靜態網站
7. 為確保安全連線，部屬 https   
   作者尚未實作，僅提供 ref.
   1. [輕鬆擁有綠鎖頭 https](https://blog.dmoon.tw/github-pages-custom-domain/)


# Reference

1. [不用懂git也能用GitHub Pages架設靜態網站並綁定網域](https://medium.com/@NorthBei/%E4%B8%8D%E7%94%A8%E6%87%82git%E4%B9%9F%E8%83%BD%E7%94%A8github-pages%E6%9E%B6%E8%A8%AD%E9%9D%9C%E6%85%8B%E7%B6%B2%E7%AB%99%E4%B8%A6%E7%B6%81%E5%AE%9A%E7%B6%B2%E5%9F%9F-c60c02bc470c)

1. [Github pages](https://guides.github.com/features/pages/)