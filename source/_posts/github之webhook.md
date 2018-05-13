---
title: Github 之 Webhooks
date: 2018-05-13 17:23:49
tags: 写作 
categories: Hexo
---

Hexo自身支持程序一键部署到Git、Heroku等。对于自己的服务器，其实也可以借助Github的Webhooks实现自动发布。

Webhooks allow external services to be notified when certain events happen. When the specified events happen, we’ll send a POST request to each of the URLs you provide。

可以看出，我们创建一个webhooks，然后创建一个可以接受post请求的web服务，服务器执行脚本就可以完成这个过程。

# 一、先用Flask写个最简单server

很多冗余代码，其实只要能接收Post请求就行。

```Python
import os
import logging
from flask import Flask
from logging.handlers import TimedRotatingFileHandler
import json


class NonASCIIJSONEncoder(json.JSONEncoder):
    def __init__(self, **kwargs):
        kwargs['ensure_ascii'] = False
        super(NonASCIIJSONEncoder, self).__init__(**kwargs)

    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        elif isinstance(o, bytes):
            return o.decode('utf-8')

        return json.JSONEncoder.default(self, o)


def create_app():
    app = Flask(__name__)
    logfile = os.path.join(app.root_path, 'log/log.log')
    if not os.path.exists(os.path.dirname(logfile)):
        os.mkdir(os.path.dirname(logfile))
    file_handler = TimedRotatingFileHandler(logfile, 'D', 1, 15)
    file_handler.setFormatter(
        logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
        ))
    # app.logger.setLevel(app.config.get('LOGGING_LEVEL'))
    file_handler.setLevel(app.config.get('LOGGING_LEVEl', logging.DEBUG))
    app.logger.addHandler(file_handler)

    app.json_encoder = NonASCIIJSONEncoder
    return app


app = create_app()
sh_path = os.path.join(app.root_path[:app.root_path.rfind('/')], 'publish.sh')


@app.route('/', methods=['POST'])
@app.route('/deploy')
def index():
    os.system(sh_path)
    return 'ok'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6767, debug=False, threaded=True)

```

## 二、创建一个publis.sh

web server 拿到post请求后执行这个脚本。

```bash
#!/bin/bash

git pull
hexo g -d
cd public 
cp -rf * /usr/share/nginx/html
service nginx restart

```

## 创建webhooks

进入github需要配置的项目Settings->Webhooks->add webhooks
![add webhooks](http://p4djts42a.bkt.clouddn.com/github-webhooks.png)
Payload URL:必须是指向web server的公网地址，其余的都默认。

## 校验

代码每次push的时候，github都会发起一次post请求到web server，然后执行脚本，自动化发布就完成了。
本人的阿里云服务器和github通信经常不稳定，所以在server上又加了一个deploy路由，我们可以半自动的去发布。
