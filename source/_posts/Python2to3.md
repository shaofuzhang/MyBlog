---
title: Python2 to Python3
date: 2018-03-014 13:57:49
tags: 写作 
categories: Python
---

关于Python2还是Python3的讨论依然到处可见，我们一起来看看为什么要用Python3.

## 为什么要用python3？

Sat Mar 10 20:54:35 EST 2018，Python之父在开发者邮箱回复说，Python2.7的EOL日期是2020年1月1日，之后不会再有任何更新，包括源码的安全补丁。

在来看看众所周知的Django怎么说，
Since newer versions of Python are often faster, have more features, and are better supported, the latest version of Python 3 is recommended.
大致翻译为新版本的Python速度更快，特性更多，拥有更高的支持，所以推荐最新版本的Python3.

python3的很多特性确实很棒，看这哥们整理的一份简短的[python3特性介绍](https://github.com/arogozhnikov/python3_with_pleasure)

诸如Numpy等有名的第三方库也是和Django一样，针对旧版本的Python不会再去支持。

前两年有人说因为很多第三方包不支持Python3，但这个已经是过去时，当下活跃的第三方包都是在积极的去支持Python3.

综上，为何还不用Python3呢？

还有一分部人是因为老项目是Python2，迁移到Python3工作量较大，那接下来就是干货时刻，教你如何快速的把已有项目迁移到Python3

## 2to3

[2to3](https://docs.python.org/3/library/2to3.html?highlight=2to3)是脚本的名称，是随着python解释器一起安装的。2to3 will usually be installed with the Python interpreter as a script. It is also located in the Tools/scripts directory of the Python root。

linux和mac下可以直接使用。基础的用法可以点击链接查看官网。

文章中介绍了几种使用方法，我们使用文件夹转换的方式，命令如下

```
2to3 --output-dir=python3-version/mycode -W -n python2-version/mycode
```

这个命令会递归的把python2-version/mycode路径下需要做转换的文件输出到python3-version/mycode路径下，如不需要转换的不会输出到新目录。

本人把近2G的Flask正式项目做了一次转换，特别注意项目包含静态文件，在转换的时候要注意排除，以及env等文件夹也要绕过。
转换过程中terminal打印的一些信息：

```
# has_key转为in
@@ -405,7 +405,7 @@
 def sort_by_data(data_obj, desc=False):
     data_province = dict()
     for each_data in data_obj:
-        if data_province.has_key(each_data['name']):
+        if each_data['name'] in data_province:
             if each_data["value"] != "-":

# filter转为列表推导式
         last_result = graph_last(endpoint_counters)
-        last_result = filter(lambda x: x['counter'].find('name') > -1, last_result)
+        last_result = [x for x in last_result if x['counter'].find('name') > -1]
         last_result.sort(key=lambda x: x['value']['timestamp'], reverse=True)
-        last_result = filter(lambda x: x['value']['timestamp'] == last_result[0]['value']['timestamp'], last_result)
+        last_result = [x for x in last_result if x['value']['timestamp'] == last_result[0]['value']['timestamp']]
         last_result.sort(key=lambda x: x['value']['value'], reverse=True)

# urllib路径转换
-import urllib
-import urllib2
-import urlparse
+import urllib.request, urllib.parse, urllib.error
+import urllib.request, urllib.error, urllib.parse
+import urllib.parse

```

转换过程不过几分钟，但是转换好后遇到了一些没有转换好的坑。从转换开始到测试发现并解决这些坑为止，也只是一个用了1个小时时间。把坑共勉

## 坑

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
如后面发现其他坑，会再次更新。

把上面的坑解决后，项目就正常运行了。有如此方便的神器，还有那么多新的特性，还不赶快把项目升级到python3？

人生苦短，我用python3