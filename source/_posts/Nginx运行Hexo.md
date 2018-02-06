---
title: Nginx运行Hexo
date: 2018-02-06 20:57:49
tags: 写作 
categories: Hexo
---

## 一、前言

hexo本身的命令并不支持后台运行，一旦关闭服务器连接就不能就行访问了。于是想到linux下的nohup

e.g.

```
nohup hexo server -p 80 &
```

嗯，确实可以了，但是感觉那么火的一个框架应该不会只借助nohup去实现后台运行吧。于是又去百度了一把。在知乎上看到一句
> 内容如下：不建议使用 hexo s。nodejs server 在生产环境连 Apache 都不如。建议 hexo g 后将独立页面部署到 nginx 等标准 webserver。原文地址：https://www.zhihu.com/question/57911494

深感其然，既然hexo最终是生成静态文件到其下的public，那用nginx去运行静态文件自然是首选。于是开始部署。

本文运行环境：阿里云 Ubuntu 14.04.5

## 二、配置

### 安装Nginx
```
# 阿里云首次开启root用户所以无需sudo
apt install nginx
```
配置文件在 /etc/nginx/，需要更改端口的可以去这里修改

nginx的运行目录在/usr/share/nginx

nginx安装后默认就是启动的，执行
```
curl http://localhost/
```
会出现Nginx的欢迎界面。

### 拷贝代码
```
cd Myblog
hexo g -d
cd public
# 拷贝hexo生成的静态文件到nginx运行目录
cp -rf * /usr/share/nginx/html
# 重启nginx
service nginx restart
```
这时候已经部署完成了，再次使用上面的验证命令
```
curl http://localhost/
```
这时就会出现hexo的网站。