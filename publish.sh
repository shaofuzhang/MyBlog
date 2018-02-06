git pull
hexo g -d
cd public 
cp -rf * /usr/share/html
service nginx restart