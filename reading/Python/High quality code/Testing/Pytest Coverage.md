# Pytest-cov

## Abstract 

pytest-cov 是

## Run

Runing pytest in ```bash``` with ```arg_values```.

```bash
pytest --cov={path_for_testing_coverage} {tests_path}
```

- path_for_testing_coverage

    The path of module, pytest-cov will check all .py file under this path, and calculate the persentage of ```Cover```

- tests_path

    The path of all tests files, .py file, class or function, just like ```pytest```.

## Pytest-cov's argumentations

| Options      | Description                                                                                                                                                           |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| --cov-report | report type<br> =term-missing : print line num of missing.<br>=html : Save the result as a index.html, default save at './htmlcov'.<br>=xml : save report as xml.<br> |
| --cov-cofing | Select the file of configs, and run coverage with configs.                                                                                                            |


# Report definition

| Column  | Definition                                                 |
| ------- | ---------------------------------------------------------- |
| Stmts   | refers to the number of statements in your code.           |
| Miss    | refers to the number of statements that have not been run. |
| Cover   | is test coverage, or (Stmts - Miss) / 100.                 |
| Missing | contains the line numbers of the Miss statements.          |


# 進階應用，更彈性的使用方式

pytest-cov 也可結合 `tox` 做使用，    
在針對各版本環境測試的同時，也將 cov-report 做累計，    
最後藉由 `$ coverage report` 指令輸出報表，     
`$ coverage report --fail-under=n` 則可在 coverage rate 未達標(n) 時自動報錯，    

## example:tox.ini

- [Pytest-cov exmaple](https://github.com/pytest-dev/pytest-cov/blob/master/examples/src-layout/tox.ini)
    ```ini
    [tox]
    envlist = py27,py38,report

    [tool:pytest]
    testpaths = tests
    addopts =
        --cov-report=term-missing

    [testenv]
    setenv =
        py{27,38}: COVERAGE_FILE = .coverage.{envname}
    commands = pytest --cov {posargs:-vv}
    deps =
        pytest
        coverage
    # Note:
    #     This is here just to allow examples to be tested against
    #     the current code of pytest-cov. If you copy this then
    #     use "pytest-cov" instead of "../.."
        ../..

    depends =
        report: py27,py38

    [testenv:report]
    skip_install = true
    deps = coverage
    commands =
        coverage combine
        coverage html
        coverage report --fail-under=100
    ```
- [Pytest-cov documentation - Tox](https://pytest-cov.readthedocs.io/en/latest/tox.html)
    ```ini
    [tox]
    envlist = clean,py27,py36,report

    [testenv]
    commands = pytest --cov --cov-append --cov-report=term-missing
    deps =
        pytest
        pytest-cov
    depends =
        {py27,py36}: clean
        report: py27,py36

    [testenv:report]
    deps = coverage
    skip_install = true
    commands =
        coverage report
        coverage html

    [testenv:clean]
    deps = coverage
    skip_install = true
    commands = coverage erase
    ```