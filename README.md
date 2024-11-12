## Pre-Requisites

pip install django
pip install djangorestframework
pip install psycopg2

## DB connections

DATABASES = {
'default':{
'ENGINE': 'django.db.backends.postgresql',
'NAME': 'db_diy',
'USER': 'postgres',
'PASSWORD': '123456',
'HOST': 'localhost'
}
}

## link https://www.youtube.com/watch?v=jVr-E9qefOg&t=340s

## tutorial

## cách chạy project, cd backend_erp trước

<!-- 1: chỉ chạy lần lượt 2 câu lệnh này nếu có thay đổi về file models
python manage.py makemigrations
python manage.py migrate

2 chạy câu lệnh này để chạy server cho cả dự án
python manage.py runserver

3 cau lệnh để tạo ra folder mới thay db_diy thành tên folder khác, code class thì code trong file models
python manage.py startapp db_diy -->
