# Tutorial of python coding style

## What is coding style, why coding style 

> 本文使用 Python3 

在我剛接觸 coding style 時，認真覺得這是一門玄學，在我心中他的地位跟沒事找事沒兩樣，相較 docstyle 更讓我不能理解，但是實際了解後便會明白 coding style 存在他的偉大之處。

> 這個世界最難的事莫過於在多變的世界裡維持不變的關係 -《[分開旅行 The Long Goodbye](https://news.readmoo.com/2019/12/25/the-long-goodbye/)》

附上一本與 Coding style 完全無關的小說，但這句話恰巧訴說著 Coding style 的重要性，也就是**合作**。我相信只要做過畢專分過組的我和你都明白，一個團隊長期合作肯定免不了吵架，大從對專案方向的意見分歧，小至合作期間工作分配，一個長期緊密接觸的團隊免不了摩擦磨合，Coding style 絕對會是其中一項導火線，當然你可能很幸運不用接觸這些，但你試著想想在未來某間公司你豪邁地寫著 code，在你以為完成專案時主管卻開始叫你一行一行的修正你代碼上不好的習慣，像 `import` module 的順序、變數名稱從 snake_case 改成 CamelCase、撰寫更詳細的 annotations。

> 此時再來為 coding style 付出代價痛苦值就很高了，因此一起隨手養成 Python 好習慣

## Python coding style 

Python 使用者當中較具有地位與權威的兩大 Coding style 便是 `PEP8`, `google style`，前者是 Python 老大哥自己規範的，後者是 Google 老大哥規範的。

但不管哪個，其中都會規範例如變數需多行撰寫時應如何縮排、`=` 的左右應有多少空白鍵、空行當中不得包含空白鍵等規定，目的都是要規範好統一的 Coding style，在維運時才不會花太多時間在理解別人的 Code。

舉個例子，Python dictionary 如果以單行撰寫可讀性就沒有多行撰寫好，有時候多行撰寫的 Coding style 的確可以降低維護成本。

```python
# one-line
response = {'status': 200, 'data': {'name': 'Jack', 'family': [...]}}
# multi-line
response = {
    'status': 200,
    'data': {
        'name': 'Jack',
        'family': [
            ...
        ]
    }
}
```

> [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)\
> [Google style guide](https://google.github.io/styleguide/pyguide.html)

雖然講了兩個老大哥級別的 Coding style，但要如何選擇呢？ Coding style 的選擇其實不是重點，而是統一標準才是，即便不使用老大哥們的 Coding style 也沒有關係，只要制定出統一標準，在一個規範上執行就好，遵守老大哥的標準只是方便統一口徑而已。

> 但是規範這麼複雜我要怎麼確定我有沒有寫錯呢？

---
## Linter

Linter 簡而言之就是幫你檢查或修正，解決麻煩的檢查工作，也不用擔心 code 交出去後被別人唸東唸西，也因此依照功能性質分為兩種，一種只會幫你檢查出錯誤在哪、錯了什麼，第二種則會幫你自動修正，想當然爾只有較為簡單的問題可以自動修正。在我寫這篇文章時廣受大家喜愛的幾款 linter module 有 `isort`, `black`, `flake8`, `pylint`，其中後兩者較為相近，但都各司其職，待我娓娓道來。

### isort

[isort](https://pypi.org/project/isort/) 主要想解決的是 `import` module 可讀性的問題，試想今天你的同事 `import` 了一個看起來名字取的非常正式的 module，但你上網怎麼 Google 都查不到到底是什麼 module，最後 Trace code 才發現是你同事自己寫的。

> 倘若一開始從格式上就能看出 module 屬於官方、外部還是內部，便可減少開發成本

isort 除了能夠找出有沒有符合格式的 `import` module 外，還能 auto reformat 幫你修為正確的排序。