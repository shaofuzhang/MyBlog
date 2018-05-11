#!/bin/bash
cd ..
git pull
hexo g -d
cd public 
cp -rf * /usr/share/nginx/html
service nginx restart
