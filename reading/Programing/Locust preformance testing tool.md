# API Performance Testing using Locust

Author: chloequyang@wisers.com

## API deployment

To test the performance of api, we need to limit cpus and memory  usages of docker. As shown below, `--cpus` is to limit the numbers of cpus, and `-m` is to limit the usages of memory. To determine how many cpus and memory to be limited, we can deploy a docker without limitation and check out the states of the docker.

```shell
docker run -d --cpus=cpuNum -m Mem --name containerName  imagesID 
```

To check out the states of docker:

```shell
docker stats containerID
```

## API test

#### Locust Introduction

What is [Locust](https://docs.locust.io/en/stable/index.html)? 

Locust is an easy to use, scriptable and scalable performance testing tool.

You define the behavior of your users in regular Python code, instead of using a clunky UI or domain specific language.

Features:

- **Write user test scenarios in plain-old Python**
- **Distributed & Scalable - supports hundreds of thousands of users**
- **Web-based UI**
- **Can test any system**
- **Hackable**

Locust vs JMeter:

- 如果只是做简单的接口测试、压力测试，没有需要写代码来扩展的特殊需求，首选JMeter；
- 如果某些测试场景需要写代码来扩展，你会Java的话，可以选择JMeter；
- 如果某些测试场景需要写代码来扩展，你会Python的话，可以选择Locust；
- 如果想在单台机器发起更大的压力的话，并且Python代码能力不错的话，可以选择Locust，记得一定要使用FastHttpLocust客户端

Installation: 

```shell
pip install locust
```

Locust Usage:

Step 1: Write a locustfile.py(The behaviour of a simulated user is represented by a class in your locust file. When you start a test run, Locust will create an instance of the class for each concurrent user.)

Step 2: Run a script or Web UI



Example locustfile.py:

```Python
from locust import HttpUser, task, TaskSet
import locust.stats

locust.stats.CSV_STATS_INTERVAL_SEC = 1  # default is 1 second
locust.stats.CSV_STATS_FLUSH_INTERVAL_SEC = 10  # Determines how often the data is flushed to disk, default is 10 seconds

# api setting
HOST = "http://ess19.wisers.com:7089"
URL = "/ess/entityextr/analyse"
TEST_INPUT = {"text": '王嘉爾作為唯一出席Adidas originals全球廣告影片的中國籍代言人確實牛逼啊！'}


class Testlen(TaskSet):
    @task
    def test(self):
        response = self.client.post(url=URL, json=TEST_INPUT)
        print("Response status code:", response.status_code)


class HttpRequester(HttpUser):
    tasks = [Testlen]


def runTest(u, r, file, t):
    import subprocess
    subprocess.call(
        "locust -f locustfile.py --host={} --headless --csv={} --csv-full-history -u{} -r {} -t {}".format(HOST, file, u, r, t))


if __name__ == '__main__':
    # normal test
    u = 1
    r = 1
    file = "normal_test"
    t = "1m"
    runTest(u, r, file, t)

    # stress test
    u_list = [100, 200]
    r = 1
    t = "1m"
    for u in u_list:
        file = "stress_test_u{}".format(u)
        runTest(u, r, file, t)
```

| params     | description                                                  | remark                                          |
| ---------- | :----------------------------------------------------------- | ----------------------------------------------- |
| --help     | show this help message and exit                              |                                                 |
| -f         | python module file to import                                 |                                                 |
| --host     | host to be test                                              |                                                 |
| --headless | to run locust without web UI                                 |                                                 |
| -csv       | retrieve test statistics in csv file                         | To keep all history, use `--csv-full-history` . |
| -u         | number of concurrent Locust users                            |                                                 |
| -r         | increase 2*r users each second                               |                                                 |
| -t         | Stop after the specified amount of time, e.g. (300s, 20m, 3h, 1h30m, etc.) |                                                 |

```python
# test without web UI
python locustfile.py
```



#### Locust UI

```shell
# test with web UI
$ locust -f locustfile.py
```

A web UI is applied on http://localhost:8089 when running locust.

![_images/webui-splash-screenshot.png](https://docs.locust.io/en/stable/_images/webui-splash-screenshot.png)

result

![image-20201126152419508](C:\Users\chloeouyang\AppData\Roaming\Typora\typora-user-images\image-20201126152419508.png)





#### Test Result 

The files will be named `example_stats.csv`, `example_failures.csv` and `example_history.csv` (when using `--csv=example`). The first two files will contain the stats and failures for the whole test run, with a row for every stats entry (URL endpoint) and an aggregated row. The `example_history.csv` will get new rows with the *current* (10 seconds sliding window) stats appended during the whole test run. By default only the Aggregate row is appended regularly to the history stats, but if Locust is started with the `--csv-full-history` flag, a row for each stats entry (and the Aggregate) is appended every time the stats are written (once every 2 seconds by default)

-  `example_stats.csv`
-  `example_failures.csv` 
- `example_history.csv`(`Request/s`, `Failure/s`)

```python
data = pd.read_csv('exampe_stats_history.csv')
# To find out the largest RPS without failure
data_success = data[data['Failures/s'].apply(lambda x: True if x == 0 else False)]
index = data_success['Requests/s'].idxmax()

# Get avetime and RPS
avgtime, RPS = data_success.loc[index]['Total Average Response Time'], data_success.loc[index]['Requests/s']
```



#### Test Settings



##### test data selection

- text classification(sentiment analysis): variant sequence length(25 percentile, 50 percentile, 75 percentile) 

- sequence tagging(NER): [batch_size(avg), max_seq(avg)]



##### normal test

docker guniorn worker number 1

locust setting u 1 r 1

```shell
locust -f locustfile.py --host=HOST --headless --csv=example --csv-full-history -u 1 -r 1 -t 1m
```



##### stress test

docker guniorn worker number depends on maximum workers within docker resources limit 

locust setting u 100 r 1

locust setting u 200 r 1

```shell
locust -f locustfile.py --host=HOST --headless --csv=example --csv-full-history -u 100 -r 1 -t 1m
```





#### Code Structure

- project root

  - locustfile.py
  - README.md

- deploy/test

  - locustfile.py

  - run_newman.sh

    