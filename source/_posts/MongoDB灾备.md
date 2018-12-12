---
title: MongoDB 灾备
date: 2018-12-12 10:48:49
tags: 写作 
categories: MongoDB
---

周一下午，总监说让我出个方案，有个客户想做MongoDB的灾备。了解下来，场景如下：用户目前用的是腾讯云的MongoDB服务，需要灾备到其他区域。

赶紧去腾讯云开了MongoDB测试，发现腾讯的MongoDB只能同一VPC网络下的设备可以访问，并且创建时设置的密码一直无效，拿着旧密码重新设定新密码倒是可以。手动😁

网上搜索了一下MongoDB的灾备方案，偶然看见阿里MongoDB的异地双活服务,决定沿袭大佬的步伐。
[阿里异地双活方案](https://help.aliyun.com/document_detail/86946.html?spm=5176.100249.0.0.7bd74231W3bxXz)


整理流程如下：

1.腾讯云其他区域建立Mongo副本集。
2.准备Kafka或MQ集群
3.通过MongoDump一次性做数据同步
4.启动MongoSourceProducer按照规则抓取Oplog，存入消息队列，运行在同一VPC
5.启动MongoTargetConsumer消费消息队列的内容，写入灾备的Mongo副本集

MongoSourceProducer和MongoTargetConsumer需要开发。在整个过程中，发现腾讯云平台提供了MongDB的迁移方案，可惜这个服务不能跨区，而灾备的话跨区是基本要求。

记录下dump及restore 命令

``` shell
./bin/mongodump  -h 172.17.0.9 -u mongouser -p Aa12345678  -o . --authenticationDatabase admin

./bin/mongorestore -h 172.17.0.11 -u mongouser -p Aa12345678 -d mydb --authenticationDatabase admin  ./test
```


