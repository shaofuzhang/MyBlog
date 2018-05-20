---
title: 图解Http阅读笔记
date: 2018-02-03 16:57:49
tags: http
categories: 笔记
---

## TCP/IP 协议

TCP/IP协议族按层次分别分为以下4层： 应用层、传输层、网络层和数据链路层。

### 应用层

应用层决定了向用户提供应用服务时通信的活动。Http协议就在这层。

### 传输层

传输层对上层应用层，提供处于网络连接中的两台计算机之间的数据传输。TCP和UDP在这里

### 网络层

网络层用来处理在网络上流动的数据包。

### 链路层

用来处理连接网络的硬件部分。

### TCP和HTTP分布关系

![HTTP/TCP分布图](http://p4djts42a.bkt.clouddn.com/http%E5%B1%82%E5%88%86%E5%B8%83.png)

### 三次握手

TCP位于传输层，提供可靠的字节流服务。
所谓的字节流服务是指将大块数据分割成以报文段为单位的数据包进行管理。为了准确无误的将数据送达目标处，TCP采用三次握手策略。发送端首先发送一个SYN标志的数据包给对方。接收端收到后，回传一个带有SYN/ACK标志的数据包以示传达确认信息。最后，发送端在回传一个带ACK标志的数据包，代表“握手”结束。如果某个阶段莫名终端，TCP协议会再次以相同的顺序发送相同的数据包。
![TCP三次握手](http://p4djts42a.bkt.clouddn.com/TCP%E4%B8%89%E6%AC%A1%E6%8F%A1%E6%89%8B.png)

### DNS

DNS 服务是和HTTP协议一样位于应用层的协议。它提供域名到IP地址之间的解析服务。DNS协议提供通过域名查找IP地址，或逆向从IP地址反查域名的服务。
![DNS服务](http://p4djts42a.bkt.clouddn.com/DNS%E6%9C%8D%E5%8A%A1.png)

### IP、TCP和DNS服务在HTTP协议通信过程流程

![HTTP通信](http://p4djts42a.bkt.clouddn.com/HTTP%E6%80%BB%E6%B5%81%E7%A8%8B.png)

## HTTP协议

### HTTP报文

HTTP协议交互的信息被称为HTTP报文。

### 内容编码

HTTP在传输数据时可以通过编码提升传输速率。
通常报文的主体等于实体主体。当传输时进行编码操作时，实体主体的内容发生变化，才导致它和报文主体产生差异。
压缩传输的内容编码。内容编码指明应用在实体内容上的编码格式，并保持实体信息原样压缩。内容编码后的实体由客户端接收并负责解码。(有效的加快网络传输，但是会增加客户端压力)
常见的内容编码有：gzip(GNU zip)、compress、deflate、identity(不进行编码)
![内容编码](http://p4djts42a.bkt.clouddn.com/%E5%86%85%E5%AE%B9%E7%BC%96%E7%A0%81%28%E5%8E%8B%E7%BC%A9%29.png)

### 范围请求

指定范围发送的请求叫做范围请求。对一份10000字节大小的资源，可以只请求5001~10000字节内的资源。用该特性可以实现文件断点下载功能。在首部使用Range字段来指定资源的byte范围。
![HTTP Range](http://p4djts42a.bkt.clouddn.com/HTTP%20Range.png)
针对范围请求，响应报文会返回状态码206Partial Content。对于多重范围的范围请求，响应会在首部字段Content-Type标明multipart/byteranges后返回响应报文。如果服务器无法响应范围请求，则返回200 OK和完整的实体内容。

### HTTP status code

![HTTP status code](http://p4djts42a.bkt.clouddn.com/Http%E7%8A%B6%E6%80%81%E7%A0%81.png)

### HTTP所支持的方法

![HTTP支持的方法](http://p4djts42a.bkt.clouddn.com/HTTP%E6%94%AF%E6%8C%81%E7%9A%84%E6%96%B9%E6%B3%95.png)



