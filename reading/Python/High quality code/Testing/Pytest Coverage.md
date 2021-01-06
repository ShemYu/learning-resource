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