---
title: Redis cluster
date: 2018-08-23 21:13:49
tags: Redis
categories: Redis
---

## 前言

近期在掘金买了一本《Redis深度历险：核心原理与应用实践》小册，看到Redis安全通信章节的时候，里面有一段

```HTML
spiped 可以同时支持多个客户端链接的数据转发工作，它还可以通过参数来限定允许的最大客户端连接数。但是对于服务器 spiped，它不能同时支持多个服务器之间的转发。意味着在集群环境下，需要为每一个 server 节点启动一个 spiped 进程来代收消息，在运维实践上这可能会比较繁琐。
```

对这段感到疑惑，诸如nginx做负载均衡的时候，nginx负责一个出口，那只要针对nginx的端口做ssl加密即可，redis集群为什么要互相通信呢？

纸上得来终觉浅，绝知此事要躬行。

开始动手搭建一个Redis集群。

## 环境
ubuntu 18.04.1 LTS

## 开始搭建

1. 下载Redis

```shell
wget http://download.redis.io/releases/redis-4.0.8.tar.gz
```

1. 解压Redis

```shell
tar -zxvf redis-4.0.8.tar.gz
```

2. 编译安装

``` shell
cd redis-4.0.8
make
make install
```

3. 创建Redis实例

    * 创建7000到7005文件夹

```shell
cd ~
mkdir redis-cluster
cd redis-cluster
mkdir 7000 7001 7002 7003 7004 7005
```

.把redis4.0.8中的配置文件copy到6个文件夹

```shell
cp ~/redis-4.0.8/redis.conf 7000
cp ~/redis-4.0.8/redis.conf 7001
cp ~/redis-4.0.8/redis.conf 7002
cp ~/redis-4.0.8/redis.conf 7003
cp ~/redis-4.0.8/redis.conf 7004
cp ~/redis-4.0.8/redis.conf 7005
```

.修改6个配置文件,分别修改对应的端口

```shell
vim 7000/redis.conf
port 7000 #修改端口号，7000到7005
cluster-enabled yes
cluster-config-file nodes.conf
cluster-node-timeout 5000
appendonly yes
daemonize yes #后台启动，这个官方文档没给出
```

.启动6个实例

```shell
cd 7000
redis-server redis.conf
cd ../7001
redis-server redis.conf
cd ../7002
redis-server redis.conf
cd ../7003
redis-server redis.conf
cd ../7004
redis-server redis.conf
cd ../7005
redis-server redis.conf
```

.检查实例启动情况

```shell
ps -ef |grep redis
#看到6个进程即可
```

4. 创建集群

.安装redis-trib

```shell
sudo apt install -y ruby
gem install redis
```

.使用redis-trib创建集群

```shell
cd ~/redis-4.0.8/src
./redis-trib.rb create --replicas 1 127.0.0.1:7000 127.0.0.1:7001 127.0.0.1:7002 127.0.0.1:7003 127.0.0.1:7004 127.0.0.1:7005
```

.检查集群是否正常

```shell
./redis-trib.rb  check 127.0.0.1:7000
#最后有相关输出即可
[OK] All nodes agree about slots configuration.
>>> Check for open slots...
>>> Check slots coverage...
[OK] All 16384 slots covered.
```
