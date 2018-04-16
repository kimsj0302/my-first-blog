from django.shortcuts import render
from django.utils import timezone # 현재 시간을 알기 위해 timezone 모듈을 불러옴
from .models import Post # models.py 파일에 정의된 모델 가져오기, ‘.’은 현재 디렉토리를 의미

def post_list(request):
    # 글 목록을 게시일 published_date 기준으로 정렬
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # 글 목록을 템플릿에 딕셔너리 형태로 전달함
    return render(request, 'blog/post_list.html', {'posts': posts})