# Abstract 

用來整理學習資源之 Repo.，包含網站上好文、論文等之讀書心得。

## Todo

- [ ] 整合 onenote 筆記至此

- [ ] auto-gen-contents module
    - Descriptions
      - 能自動化依據 reading 目錄下的結構、.md 生成目錄，於 root directory 內的 README 當中供讀者輕鬆找到想找的文章
	
	- Requirments
    	- 自動生成目錄
    	- Git hooks - pre-commit phase 自動執行

- [ ] Keyword 自動生成

	- 從文本當中超連結自動爬入字串，以較為泛用的方式前處理並提取關鍵詞

- [ ] Google sheets api

	- 簡易資料庫串接

- [ ] 偵測筆記較少的 md 標記為未讀文章

- [ ] 撰寫 CONTRIBUTING
- [ ] 撰寫單元測試

## Pre-commit 環境建置

```bash
# easy install by pip
$ pip install pre-commit

# install pre-commit framework to git hooks
$ pre-commit install

# Uninstall if you need
$ pre-commit uninstall
```
# Branch

分支操作使用自定義的形式，大部分規則與一般版控分支 common practice 雷同，規則如下:

| Branch name                 | Descriptions                                                                  |
| --------------------------- | ----------------------------------------------------------------------------- |
| master                      | stable version, include reading and ./bin done.                               |
| read                        | brand of updating feature reading, seam like `dev` branch in common practice. |
| {some feature develop name} | branch for develop feature.                                                   |

# Contents

- Reading

	1. [Data scientist roadmap](https://github.com/ShemYu/learning-resource/blob/master/reading/Data%20scientist%20roadmap.md)

	1. [親自動手寫一個 Python libary](https://github.com/ShemYu/learning-resource/blob/master/reading/親自動手寫一個%20Python%20libary.md)

	1. [資料科學五大 Q&A：如何成為資料科學家？資料科學產業的未來？](https://github.com/ShemYu/learning-resource/blob/master/reading/資料科學五大%20Q&A：如何成為資料科學家？資料科學產業的未來？.md)

