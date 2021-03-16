# Professional Error Handling With Python
## 心得
文中有簡單介紹 Python 有哪些 Exceptions，並教學如何撰寫自定義 Exception，以及自定義的 Exception 類別當中，一般可以實作哪些參數，如何作錯誤處理，想了解 Error Handling 基礎知識建議看過此篇。

> ## [Professional Error Handling With Python](https://code.tutsplus.com/tutorials/professional-error-handling-with-python--cms-25950)
> In this tutorial you'll learn how to handle error conditions in Python from a whole system point of view. Error handling is a critical aspect of design, and it crosses from the lowest levels (sometimes the hardware) all the way to the end users. If you don't have a consistent strategy in place, your system will be unreliable, the user experience will be poor, and you'll have a lot of challenges debugging and troubleshooting.    
> 
> The key to success is being aware of all these interlocking aspects, considering them explicitly, and forming a solution that addresses each point.

## Python Excetions
```
BaseException
 
 +-- SystemExit
 
 +-- KeyboardInterrupt
 
 +-- GeneratorExit
 
 +-- Exception
 
      +-- StopIteration
 
      +-- StandardError
 
      |    +-- BufferError
 
      |    +-- ArithmeticError
 
      |    |    +-- FloatingPointError
 
      |    |    +-- OverflowError
 
      |    |    +-- ZeroDivisionError
 
      |    +-- AssertionError
 
      |    +-- AttributeError
 
      |    +-- EnvironmentError
 
      |    |    +-- IOError
 
      |    |    +-- OSError
 
      |    |         +-- WindowsError (Windows)
 
      |    |         +-- VMSError (VMS)
 
      |    +-- EOFError
 
      |    +-- ImportError
 
      |    +-- LookupError
 
      |    |    +-- IndexError
 
      |    |    +-- KeyError
 
      |    +-- MemoryError
 
      |    +-- NameError
 
      |    |    +-- UnboundLocalError
 
      |    +-- ReferenceError
 
      |    +-- RuntimeError
 
      |    |    +-- NotImplementedError
 
      |    +-- SyntaxError
 
      |    |    +-- IndentationError
 
      |    |         +-- TabError
 
      |    +-- SystemError
 
      |    +-- TypeError
 
      |    +-- ValueError
 
      |         +-- UnicodeError
 
      |              +-- UnicodeDecodeError
 
      |              +-- UnicodeEncodeError
 
      |              +-- UnicodeTranslateError
 
      +-- Warning
 
           +-- DeprecationWarning
 
           +-- PendingDeprecationWarning
 
           +-- RuntimeWarning
 
           +-- SyntaxWarning
 
           +-- UserWarning
 
           +-- FutureWarning
 
  +-- ImportWarning
 
  +-- UnicodeWarning
 
  +-- BytesWarning
  
```