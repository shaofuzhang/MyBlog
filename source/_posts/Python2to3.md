---
title: Python2 to Python3
date: 2018-03-014 13:57:49
tags: 写作 
categories: Python
---

## 为什么要用python3？
1.By the end of 2019 the scientific stack will stop supporting Python2. As for numpy, after 2018 any new feature releases will only support Python3.
2.python3的很多特性确实很棒
看这哥们整理的一份简短的python3特性介绍
> https://github.com/arogozhnikov/python3_with_pleasure

## 2to3
这两天在查看python3.6新特性的时候，偶然发现一个存在已久的一个python2转换为python3的官方工具。深感它就是最便捷的转换工具，特地整理下。
> https://docs.python.org/3/library/2to3.html?highlight=2to3
2to3是脚本的名称，是随着python解释器一起安装的。
文章中介绍了几种使用方法，我们使用文件夹转换的方式

```
2to3 --output-dir=python3-version/mycode -W -n python2-version/mycode
```

这个命令会递归的把python2-version/mycode路径下需要做转换的文件输出到python3-version/mycode路径下，如不需要转换的不会输出到新目录。对于已存在的项目，会存在诸如env，static的文件夹，在转换的时候要注意排除。
转换后

## 坑
这里的内容会在继续更新

1.python3和低版本的xlwt不兼容，所以有用到这个包且版本较低的话需要升级到最新。目前最新的1.3.0

2.email模块的调整
```
from email.mime.multipart import MIMEMultipart  # import MIMEMultipart
from email.mime.text import MIMEText  # import MIMEText
from email.mime.base import MIMEBase  # import MIMEBase
from email.encoders import encode_base64
# 发送附件时文件名
filename=('gbk', '', file_name)
```

3.write函数
参数必须是bytes类型
```
with open(dst + '/cfg.json', 'wb') as f:
    f.write(str.encode(scfg))
```
