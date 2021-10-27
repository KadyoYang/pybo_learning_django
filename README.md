### 교재
> `https://wikidocs.net/79091`

### 기본 설정
```bash
# 파이썬 가상환경 생성 및 가상환경 실행
# 해제하려면 deactivate
$mkdir venvs
$cd venvs
$python -m venv something
$./something/Scripts/activate


# 장고 설치
$pip install django==3.1.3


# 적당한 위치에 장고 프로젝트 생성 및 실행
# 실행 해제하려면 Ctrl+Pause
$django-admin startproject config .
$python manage.py runserver

# 프로젝트에 앱을 생성
$django-admin startapp pybo 
```

