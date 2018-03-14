---
title: Python2 to Python3
date: 2018-03-014 13:57:49
tags: 写作 
categories: Python
---

## 为什么要用python3？

1.到2020年官方不在对python2更新新特性，诸如Numpy等有名的第三方库也是如此。

2.python3的很多特性确实很棒，看这哥们整理的一份简短的[python3特性介绍](https://github.com/arogozhnikov/python3_with_pleasure)

这两天在查看python3.6新特性的时候，偶然发现一个存在已久的一个python2转换为python3的官方工具。深感它就是最便捷的转换工具，特地整理下。

## 2to3

[2to3](https://docs.python.org/3/library/2to3.html?highlight=2to3)是脚本的名称，是随着python解释器一起安装的。2to3 will usually be installed with the Python interpreter as a script. It is also located in the Tools/scripts directory of the Python root。

linux和mac下可以直接使用。基础的用法可以点击链接查看官网。

文章中介绍了几种使用方法，我们使用文件夹转换的方式，命令如下

```
2to3 --output-dir=python3-version/mycode -W -n python2-version/mycode
```

这个命令会递归的把python2-version/mycode路径下需要做转换的文件输出到python3-version/mycode路径下，如不需要转换的不会输出到新目录。

今天下午的时候本人把近2G的Flask正式项目做了一次转换，项目包含静态文件，在转换的时候要注意排除，以及env等文件夹也要绕过。转换过程不过几分钟，转换好后遇到了一些坑。

## 坑
注：这块内容会持续更新

1.python3.5和低版本的xlwt不兼容，所以有用到这个包且版本较低的话需要升级到最新。目前最新的1.3.0

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

把上面的坑解决后，项目就正常运行了。整个过程大概1个小时。有如此方便的神器，还有那么多新的特性，还不赶快把项目升级到python3？

人生苦短，我用python