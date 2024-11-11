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

## route authentication

<!-- post register : http://127.0.0.1:8000/register
post login : http://127.0.0.1:8000/login
get users: http://127.0.0.1:8000/user -->

## route users

<!--
get list user : http://127.0.0.1:8000/users/add
post user( cái này có thể để đó hoặc xoá cũng được vì
cái này tạo user khôg có token vì cái này được làm trước authentication): http://127.0.0.1:8000/users/add
get ,put : http://127.0.0.1:8000/users/add/{id}/
 -->

## route company

<!--
get : http://127.0.0.1:8000/company/add
post: http://127.0.0.1:8000/company/add
delete: http://127.0.0.1:8000/company/add/{id}/
put : http://127.0.0.1:8000/company/add/{id}/
-->

## route supplier

<!--
get, post: http://127.0.0.1:8000/supplier/add
put, delete: http://127.0.0.1:8000/supplier/add/{id}/
<!--
## route product
 get, post : http://127.0.0.1:8000/product/add
 put, delete: http://127.0.0.1:8000/product/add/{id}/
-->

## route bank

 <!--
 get , post : http://127.0.0.1:8000/banker/add
 put, delete: http://127.0.0.1:8000/banker/add/{id}/
-->

## route material

<!--
get, post : http://127.0.0.1:8000/material/add
put, delete: http://127.0.0.1:8000/material/add/{id}/
-->

## route role

<!--
get , post: http://127.0.0.1:8000/settings/roles/add
put , delete: http://127.0.0.1:8000/settings/roles/add/{id}/ -->
