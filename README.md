"# django_pjt" 

1일차
conda activate cakd_dj

pip install django==3.2

pip install django-allauth django-crispy-forms django-markdownx

django-admin startproject [프로젝트폴더] .

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

http://127.0.0.1:8000/admin

python manage.py startapp homepage
python manage.py startapp blog

settings.py -> INSTALLED_APPS -> 'blog', 'homepage' 추가

2일차

cakdpjt/models.py 수정
cakdpjt/admin.py 수정

python manage.py makemigrations
python manage.py migrate

python manage.py runserver 실행 후 post add 글 써보기

cakdpjt에서 urls.py 설정

homepage - templates\homepage 폴더 생성
homepage - templates\homepage - about_me.html & landing.html 생성
homepage - urls.py 생성
homepage - views.py 설정

blog 폴더도 동일
blog - templates\blog 폴더 생성
blog - templates\blog - post_list.html & post_detail.html 생성
blog - urls.py 생성
blog - views.py 설정

python manage.py runserver 실행하여 확인

blog - templates\blog - post_list.html 수정

blog - templates\blog - post_detail.html 수정

3일차

base.html - link & script 추가

fontawesome 사이트에 들어가 회원가입 후 kit-code 입력 -> head - script 부분 수정

navbar.html & footer.html 생성

bootstrap 사이트 -> ver4.5 -> components -> navbar 고르기

navbar.html & footer.html 데이터 추가

base - body 수정
{% include 'blog/navbar.html' %}
{% block main_area %}{% endblock %}
{% include 'blog/footer.html' %}

base - body - script 추가

post_list 수정
{% extends 'blog/base.html' %}
{% block main_area %}
{post_list 내용}
{% endblock  %}

post_detail 수정
{% extends 'blog/base.html' %}
{% block head_title %} {{post.title}} - Blog {% endblock %}
{% block main_area %}
{post_detail 내용}
{% endblock  %}
