# Abstract 

用來整理學習資源之 Repo.，包含網站上好文、論文等之讀書心得。

## Todo

### Development
- [X] auto-gen-contents module
    - Descriptions
      - 能自動化依據 reading 目錄下的結構、.md 生成目錄，於 root directory 內的 README 當中供讀者輕鬆找到想找的文章
	
	- Requirments
    	- 自動生成目錄
    	- Git hooks - pre-commit phase 自動執行
- [ ] Contents generator optimize and new feature
    - [ ] 依照筆記量釋出不同顏色標籤
      - [ ] 偵測筆記較少的 md 標記為`尚未完成
      - 實作
        - [X] 完成 Progressor 類別設計
    - [ ] 架構優化
    - [ ] Keyword 自動生成
    	- 從文本當中超連結自動爬入字串，以較為泛用的方式前處理並提取關鍵詞
  	- [ ] auto-gen module 建置於 pre-commit phase 自動執行產生目錄
  	- [ ] 閱讀狀況數據統計報表

### Operations
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

- reading
	1. [vscode.md](https://github.com/ShemYu/learning-resource/blob/read/reading/vscode.md)
	- Data science
		1. [Data science… without any data.md](https://github.com/ShemYu/learning-resource/blob/read/reading/Data%20science/Data%20science%E2%80%A6%20without%20any%20data.md)
		1. [資料科學五大 Q&A：如何成為資料科學家？資料科學產業的未來？.md](https://github.com/ShemYu/learning-resource/blob/read/reading/Data%20science/%E8%B3%87%E6%96%99%E7%A7%91%E5%AD%B8%E4%BA%94%E5%A4%A7%20Q%26A%EF%BC%9A%E5%A6%82%E4%BD%95%E6%88%90%E7%82%BA%E8%B3%87%E6%96%99%E7%A7%91%E5%AD%B8%E5%AE%B6%EF%BC%9F%E8%B3%87%E6%96%99%E7%A7%91%E5%AD%B8%E7%94%A2%E6%A5%AD%E7%9A%84%E6%9C%AA%E4%BE%86%EF%BC%9F.md)
	- Data scientist roadmap
		1. [Data scientist roadmap.md](https://github.com/ShemYu/learning-resource/blob/read/reading/Data%20scientist%20roadmap/Data%20scientist%20roadmap.md)
	- Design Pattern

		- Domain-Driven Design
			1. [1_初探.md](https://github.com/ShemYu/learning-resource/blob/read/reading/Design%20Pattern/Domain-Driven%20Design/1_%E5%88%9D%E6%8E%A2.md)
	- Docker
		1. [3_Docker 基本運作.md](https://github.com/ShemYu/learning-resource/blob/read/reading/Docker/3_Docker%20%E5%9F%BA%E6%9C%AC%E9%81%8B%E4%BD%9C.md)
		1. [Docker compose.md](https://github.com/ShemYu/learning-resource/blob/read/reading/Docker/Docker%20compose.md)
		1. [Docker入門.md](https://github.com/ShemYu/learning-resource/blob/read/reading/Docker/Docker%E5%85%A5%E9%96%80.md)
	- Git
		1. [CICD初探.md](https://github.com/ShemYu/learning-resource/blob/read/reading/Git/CICD%E5%88%9D%E6%8E%A2.md)
		1. [版本號的基本常識.md](https://github.com/ShemYu/learning-resource/blob/read/reading/Git/%E7%89%88%E6%9C%AC%E8%99%9F%E7%9A%84%E5%9F%BA%E6%9C%AC%E5%B8%B8%E8%AD%98.md)
		- Github pages
			1. [Github pages - 輕鬆架設靜態網頁.md](https://github.com/ShemYu/learning-resource/blob/read/reading/Git/Github%20pages/Github%20pages%20-%20%E8%BC%95%E9%AC%86%E6%9E%B6%E8%A8%AD%E9%9D%9C%E6%85%8B%E7%B6%B2%E9%A0%81.md)
	- Linux
		1. [鳥哥 Shell script.md](https://github.com/ShemYu/learning-resource/blob/read/reading/Linux/%E9%B3%A5%E5%93%A5%20Shell%20script.md)
	- Programing
		1. [Locust preformance testing tool.md](https://github.com/ShemYu/learning-resource/blob/read/reading/Programing/Locust%20preformance%20testing%20tool.md)
		1. [何謂DevOps.md](https://github.com/ShemYu/learning-resource/blob/read/reading/Programing/%E4%BD%95%E8%AC%82DevOps.md)
		- 前端
			1. [後端怎麼區分.md](https://github.com/ShemYu/learning-resource/blob/read/reading/Programing/%E5%89%8D%E7%AB%AF/%E5%BE%8C%E7%AB%AF%E6%80%8E%E9%BA%BC%E5%8D%80%E5%88%86.md)
			- img
				1. [20210312181535.png](https://github.com/ShemYu/learning-resource/blob/read/reading/Programing/%E5%89%8D%E7%AB%AF/img/20210312181535.png)
	- Python
		1. [Flask.md](https://github.com/ShemYu/learning-resource/blob/read/reading/Python/Flask.md)
		1. [如何用 Python 撰寫 APP.md](https://github.com/ShemYu/learning-resource/blob/read/reading/Python/%E5%A6%82%E4%BD%95%E7%94%A8%20Python%20%E6%92%B0%E5%AF%AB%20APP.md)
		1. [如何處理比 memory 更大的資料.md](https://github.com/ShemYu/learning-resource/blob/read/reading/Python/%E5%A6%82%E4%BD%95%E8%99%95%E7%90%86%E6%AF%94%20memory%20%E6%9B%B4%E5%A4%A7%E7%9A%84%E8%B3%87%E6%96%99.md)
		1. [親自動手寫一個 Python libary.md](https://github.com/ShemYu/learning-resource/blob/read/reading/Python/%E8%A6%AA%E8%87%AA%E5%8B%95%E6%89%8B%E5%AF%AB%E4%B8%80%E5%80%8B%20Python%20libary.md)
		- Basic
			1. [.gitingore.md](https://github.com/ShemYu/learning-resource/blob/read/reading/Python/Basic/.gitingore.md)
			1. [Anaconda.md](https://github.com/ShemYu/learning-resource/blob/read/reading/Python/Basic/Anaconda.md)
			1. [Decorator.md](https://github.com/ShemYu/learning-resource/blob/read/reading/Python/Basic/Decorator.md)
			1. [PIP.md](https://github.com/ShemYu/learning-resource/blob/read/reading/Python/Basic/PIP.md)
			1. [Python 在 DevOps 中的應用.md](https://github.com/ShemYu/learning-resource/blob/read/reading/Python/Basic/Python%20%E5%9C%A8%20DevOps%20%E4%B8%AD%E7%9A%84%E6%87%89%E7%94%A8.md)
			1. [Python 當中的 switch case.md](https://github.com/ShemYu/learning-resource/blob/read/reading/Python/Basic/Python%20%E7%95%B6%E4%B8%AD%E7%9A%84%20switch%20case.md)
			1. [`python` command 預設使用 Python3.md](https://github.com/ShemYu/learning-resource/blob/read/reading/Python/Basic/%60python%60%20command%20%E9%A0%90%E8%A8%AD%E4%BD%BF%E7%94%A8%20Python3.md)
			1. [函式基本概念.md](https://github.com/ShemYu/learning-resource/blob/read/reading/Python/Basic/%E5%87%BD%E5%BC%8F%E5%9F%BA%E6%9C%AC%E6%A6%82%E5%BF%B5.md)
			1. [底線與命名規則.md](https://github.com/ShemYu/learning-resource/blob/read/reading/Python/Basic/%E5%BA%95%E7%B7%9A%E8%88%87%E5%91%BD%E5%90%8D%E8%A6%8F%E5%89%87.md)
		- Class
			1. [Meta class.md](https://github.com/ShemYu/learning-resource/blob/read/reading/Python/Class/Meta%20class.md)
			1. [__new__ and __init__.md](https://github.com/ShemYu/learning-resource/blob/read/reading/Python/Class/__new__%20and%20__init__.md)
		- Error handling
			1. [Professional Error Handling With Python.md](https://github.com/ShemYu/learning-resource/blob/read/reading/Python/Error%20handling/Professional%20Error%20Handling%20With%20Python.md)
		- High quality code
			1. [Code quality.md](https://github.com/ShemYu/learning-resource/blob/read/reading/Python/High%20quality%20code/Code%20quality.md)
			1. [Common practice of famous project.md](https://github.com/ShemYu/learning-resource/blob/read/reading/Python/High%20quality%20code/Common%20practice%20of%20famous%20project.md)
			1. [PEP8.md](https://github.com/ShemYu/learning-resource/blob/read/reading/Python/High%20quality%20code/PEP8.md)
			- Coding style
				1. [black.md](https://github.com/ShemYu/learning-resource/blob/read/reading/Python/High%20quality%20code/Coding%20style/black.md)
				1. [Coding style.md](https://github.com/ShemYu/learning-resource/blob/read/reading/Python/High%20quality%20code/Coding%20style/Coding%20style.md)
				1. [pylint.md](https://github.com/ShemYu/learning-resource/blob/read/reading/Python/High%20quality%20code/Coding%20style/pylint.md)
				- pre-commit
					1. [1_調研 pre-commit.md](https://github.com/ShemYu/learning-resource/blob/read/reading/Python/High%20quality%20code/Coding%20style/pre-commit/1_%E8%AA%BF%E7%A0%94%20pre-commit.md)
					1. [2_pre-commit.md](https://github.com/ShemYu/learning-resource/blob/read/reading/Python/High%20quality%20code/Coding%20style/pre-commit/2_pre-commit.md)
					1. [3_pre-commit 三度調研.md](https://github.com/ShemYu/learning-resource/blob/read/reading/Python/High%20quality%20code/Coding%20style/pre-commit/3_pre-commit%20%E4%B8%89%E5%BA%A6%E8%AA%BF%E7%A0%94.md)
			- Docs
				1. [pydocstyle.md](https://github.com/ShemYu/learning-resource/blob/read/reading/Python/High%20quality%20code/Docs/pydocstyle.md)
			- Testing
				1. [Flaky test.md](https://github.com/ShemYu/learning-resource/blob/read/reading/Python/High%20quality%20code/Testing/Flaky%20test.md)
				1. [Pytest Coverage.md](https://github.com/ShemYu/learning-resource/blob/read/reading/Python/High%20quality%20code/Testing/Pytest%20Coverage.md)
				1. [Pytest doctest.md](https://github.com/ShemYu/learning-resource/blob/read/reading/Python/High%20quality%20code/Testing/Pytest%20doctest.md)
				1. [Pytest notebook.md](https://github.com/ShemYu/learning-resource/blob/read/reading/Python/High%20quality%20code/Testing/Pytest%20notebook.md)
				1. [Pytest 測試實戰.md](https://github.com/ShemYu/learning-resource/blob/read/reading/Python/High%20quality%20code/Testing/Pytest%20%E6%B8%AC%E8%A9%A6%E5%AF%A6%E6%88%B0.md)
				1. [初探Tox.md](https://github.com/ShemYu/learning-resource/blob/read/reading/Python/High%20quality%20code/Testing/%E5%88%9D%E6%8E%A2Tox.md)
		- Pyproject
			1. [How to setup.py.md](https://github.com/ShemYu/learning-resource/blob/read/reading/Python/Pyproject/How%20to%20setup.py.md)
		- Signals
			1. [基本概念.md](https://github.com/ShemYu/learning-resource/blob/read/reading/Python/Signals/%E5%9F%BA%E6%9C%AC%E6%A6%82%E5%BF%B5.md)
