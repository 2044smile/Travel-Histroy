from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()

class Border(models.Model):
    title = models.CharField(max_length=100)
    # AUTH_USER_MODEL은 현재 프로젝트에서 사용하는 인증용 이용자 모델이 위치한 경로를 문자열로 지정하고 있다.
    author = models.CharField(max_length=30)
    text = models.TextField(max_length=500)
    photo = models.ImageField(upload_to='config/static', default='config/static/no_image.png')
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):

        return self.title
