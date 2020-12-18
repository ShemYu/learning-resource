# Docker 從入門到實踐

## Abstract 

Docker 是一款高效率、高效能建立虛擬機的服務，除執行的應用外，幾乎不消耗多餘資源。

Docker 在 DevOps 領域上，能使用包裝好的映象檔快速部屬測試、維運環境，一次建立或設定好，再任意地方正常執行。

## Docker 基本概念
1. Image 映像檔

    唯獨的模板，可以用來建立 Container，Docker 提供簡單的機制**建立**或是**更新**映像黨，快速從他人那下載已經做得好的映像檔。

2. Container 容器

    實作的 Image，可看作簡易 Linux 環境，實作時會在最上層建立一個可寫層。

3. Repository 倉庫

    映像檔儲存的場所，Repository 又可以儲存於例如 Docker Hub, Docker Pool 這註冊伺服器。
    
    如同 Github 可以建立 local repository。
    
    概念跟 Git repo. 相似，註冊伺服器就如同 GitHub 這種託管服務。

## Instatllation

Docker 內建 Ubuntu 套件，可以直接安裝，以快速安裝舉例。

```console
$ curl -sSL https://get.docker.com/ubuntu/ | sudo sh
```

## [Image](https://philipzheng.gitbook.io/docker_practice/image)


基本概念中 Docker 三大組件之一，執行容器需在本地端存在對應的映像檔，若否則自動從映像檔倉庫下載(預設是從 Docker Hub)。

下列指令運用 ```docker pull``` 從預設的 DockerHub 下載 Ubuntu 12.04 版本。

```console
$ sudo docker pull ubuntu:12.04
Pulling repository ubuntu
ab8e2728644c: Pulling dependent layers
511136ea3c5a: Download complete
5f0ffaa9455e: Download complete
a300658979be: Download complete
904483ae0c30: Download complete
ffdaafd1ca50: Download complete
d047ae21eeaf: Download complete
```

因此其效果等同於以下指令，

```console
$ sudo docker pull dl.dockerpool.com:5000/ubuntu:12.04
Pulling dl.dockerpool.com:5000/ubuntu
ab8e2728644c: Pulling dependent layers
511136ea3c5a: Download complete
5f0ffaa9455e: Download complete
a300658979be: Download complete
904483ae0c30: Download complete
ffdaafd1ca50: Download complete
d047ae21eeaf: Download complete
```

運用 ```docker run``` 執行映像檔建立容器。

```console
$ sudo docker run -t -i ubuntu:12.04 /bin/bash
root@fe7fc4bd8fc9:/#
```

```docker image``` 則會列出已經有的映像檔。

```console
$ sudo docker images
REPOSITORY       TAG      IMAGE ID      CREATED      VIRTUAL SIZE
ubuntu           12.04    74fe38d11401  4 weeks ago  209.6 MB
ubuntu           precise  74fe38d11401  4 weeks ago  209.6 MB
ubuntu           14.04    99ec81b80c55  4 weeks ago  266 MB
ubuntu           latest   99ec81b80c55  4 weeks ago  266 MB
ubuntu           trusty   99ec81b80c55  4 weeks ago  266 MB
...
```



# Reference

1. [《Docker —— 從入門到實踐­》正體中文版](https://philipzheng.gitbook.io/docker_practice/introduction)

1. [Docker 10 大 QA](https://www.ithome.com.tw/news/91847)