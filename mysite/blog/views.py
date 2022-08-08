from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {}) # request를 넘겨받아 render 메서드를 호출
