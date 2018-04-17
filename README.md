# AfterEnd

> 均采用面向对象形式

都采用面向对象的方法，不要直接写方法

> 项目结构

1.model: 数据库对象（mysql，mongodb（暂时不用），redis（缓存））

2.utils: 工具类，数据流转文件存储、图片url地址设置

3.service: 业务逻辑（注册信息的处理，从数据获取的对象进行相应数据格式化（json），信息安全验证......）

4.static: 存放网页静态资源的文件夹

5.templates: 存放网页文件（html）文件

> 后端进度

#### 1.2018-4-9
在admin内增加录入主席照片的功能
由于使用了ImageField，到时候环境需要安装pillow

#### 2.2018-4-9
使用`pip3 install pymysql`模块，使得可以在python3.x版本中的django使用mysql数据库。添加了了数据库连接设置，具体连接信息请联系github:chuntaojun

#### 3.2018-4-14
请仔细看每个方法的注释信息！！！

#### 4.2018-4-14
登录相关的操作,所返回的就送数据格式按照wiki】上面的来

> 服务器部署

1. pip install nginx;
2. pip install uwsgi
3. 在项目根目录下（可选，其实其他地方写uwsgi配置文件也没什么毛病）新建script文件夹，在内新建uwsgi配置文件my_uwsgi.ini(名字可变)

```C
[uwsgi]

#http = :8080 #如果是只用uwsgi的话，从http走
socket = 127.0.0.1:8080
chdir = /home/ubuntu/AfterEnd 
module = ICSHDU.wsgi
master = true
processes = 6 #设置成cpu个数仿佛能体验比较好的性能
threads = 2
vacuum = true
logto = /tmp/my_uwsgi.log 
```

4. 修改/etc/nginx/nginx.conf（地址也许有变，可通过nginx -t查看）

   在http{}内添加

```
upstream django{
	server 127.0.0.1:8080;#与uwsgi保持一致
}
server {
    listen         80; 
    server_name    localhost;#可改为域名
    charset utf-8;
    access_log      /var/log/nginx/myweb_access.log;
    error_log       /var/log/nginx/myweb_error.log;

    client_max_body_size 75M;

    location / { 
        include /etc/nginx/uwsgi_params;
        uwsgi_pass django;
       
    }   
    location /static/ {
        alias /home/ubuntu/AfterEnd/static/;
     }
 }
```



「在此文件首行，把user改成了root」

接着**把  include /etc/nginx/sites-enabled/*; 注释掉！**

然后 nginx -t 检查一下是否有错

再执行 nginx -s reload 重新加载

5. 进入项目根目录，执行 python manage.py collectstatic  整合静态资源
6. 记得将settings.py里的 DEBUG改为False
7. 执行 uwsgi --ini /路径/my_uwsgi.ini

> 待办事项

1. 修改settings.py中的 ALLOWED_HOSTS

​