from django.urls import path
from . import views

### url 패턴을 추가

urlpatterns = [
    path('', views.post_list, name = 'post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail')
]
# post_list라는 view가 루느 url에 할당되어 이 패턴은 빈 문자열에 매칭이 되며, 장고 url확인자는 전체 경로에서 접두어에 포함되는 도메인 이름을 무시하고 받아들임
# 이 패턴이 views.post_list를 보여주라고 함. name = 'post_list'는 url에 이름을 붙인 것으로 뷰를 식별

