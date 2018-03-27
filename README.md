# 配置和安装
## 环境

Django-1.10.8  python2.7    Wndows/Mac

## 安装
python –m pip install –r requirements.txt

### 说明
Mac下安装mysql以及MySQL-python

brew install mysql
pip install MySQL-python

如果第二条安装出现"Failed building wheel for mysql-python"错误，则采用以下方法

LDFLAGS=-L/usr/local/opt/openssl/lib pip install mysql-python 

## 启动服务

建库

本地mysql需要新建配置文件中的数据库
settings.py文件：
DATABASES = {
    'default':{
     'ENGINE':'django.db.backends.mysql',
     'HOST':'127.0.0.1',
     'PORT':'3306',
     'NAME':'bugwrite',  # 数据库名
     'USER':'root',
     'PASSWORD':'root',
     'OPTIONS':{
         'init_command':"SET sql_mode='STRICT_TRANS_TABLES'"
     },
    }
}

## 建表
cd myweb01
python manage.py  makemigrations
python manage.py migrate

## 启服务

python manage.py runserver
