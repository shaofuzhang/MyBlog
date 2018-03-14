---
title: Hexo主题yilia使用总结
date: 2018-02-03 16:57:49
tags: 写作 
categories: Hexo
---

由于想上传图片，但是云存储尚未申请下来，此篇博客暂时不更。烂尾。
yilia 一个简洁优雅的hexo主题。在应用过程中，发现github主页上的使用说明比较简陋且不完整，踩了几个坑，故此记录下。在看此文之前，请确保已经能给运行Hexo server。如果还没能运行，可以参考[Hexo官方文档](https://hexo.io/zh-cn/docs/)

## 一、配置运行

### 安装
在博客根目录下
```
$ git clone https://github.com/litten/hexo-theme-yilia.git themes/yilia
```
### 配置
修改博客根目录下的 _config.yml ： theme: yilia

## 二、配置

### 配置主题 
即配置themes/yilia/_config.py。主页上说主题配置文件在主目录下的_config.yml，请根据自己需要修改使用。 完整配置例子，可以参考[我的博客备份](https://github.com/litten/BlogBackup)。这里就埋了个坑。该备份项目中themes/yilia/_config.yml中第56行是不被兼容的。
```
# 是否在新窗口打开链接
open_in_new: true
```
所以还是用源码里自带的config自行配置，作者的备份文件作为参考。这里先简单配置一下。


### 配置项目
即配置博客根目录下的_config.yml。简单按照自己的信息配置下e.g.
```
title: SF Zhang 的博客
subtitle: 攻城狮
description: 青菜的博客
author: SF Zhang
```

## 三、运行

