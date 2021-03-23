# Switch case in Python
大家有這個經驗嗎，想要撰寫一隻程式統一街口，給定使用者參數選擇運算用的底層邏輯，因此寫出這樣的方法:

```python
def _similarity_fun(x, y, similarity_func):
    if isinstance(similarity_func, str):
        if similarity_func == "hamming_distance":
            result = hamming_distance(x, y)
        elif similarity_func == "levenshtein_distance":
            result = levenshtein_distance(x, y)
        elif similarity_func == "levenshtein_similarity":
            result = levenshtein_similarity(x, y)
        elif similarity_func == "jcro_similarity":
            result = _jcro_similarity(x, y)
        elif similarity_func == "jaro_winkler_similarity":
            result = _jaro_winkler_similarity(x, y)
        elif similarity_func == "damerau_levenshtein_distance":
            result = _damerau_levenshtein_distance(x, y)
        elif similarity_func == "common_sequence_distance":
            result = _common_sequence_distance(x, y)
        elif similarity_func == "jaccard_score":
            result = jaccard_score(x, y)
        elif similarity_func == "jaccard_distance":
            result = jaccard_distance(x, y)
        elif similarity_func == "manhattan_distance":
            result = manhattan_distance(x, y)
        elif similarity_func == "euclidean_distance":
            result = euclidean_distance(x, y)
        elif similarity_func == "euclidean_distance_square":
            result = euclidean_distance_square(x, y)
        elif similarity_func == "euclidean_distance_centred":
            result = euclidean_distance_centred(x, y)
        elif similarity_func == "cosine_similarity":
            result = cosine_similarity(x, y)
        elif similarity_func == "cosine_distance":
            result = cosine_distance(x, y)
        else:
            raise ValueError("Not yet support similarity function")
    else:
        result = similarity_func(x, y)
    return result
```
上面這種寫法除了**複雜度**過高外，也存在使用上的問題，例如今天這個方法的複雜度是否有高到使用者會願意去記住你的參數(輸入的 string name)，還是使用者記得數學邏輯會自己寫一個方式來算。這種時候學過其他語言的朋友可能會說:

    可以用 Swtich case 阿，怎麼不用 Swtich case

但實際上在 Python 程式語言當中，其實不存在 Swtich case 語法，因此我會建議使用物件導向的方式解決這種問題，以物件導向方式限制使用者的輸入:
```python
class Similarity():
   @classmethod
   def method1(cls, x, y):
       return dosomething.. 
```

祥見 [Enum code example](https://github.com/ShemYu/learning-resource/blob/read/reading/Python/Basic/Enum.ipynb)