from django.shortcuts import render

# Create your views here.


def index(request):
    result = 'asdfkgmdla;g'
    return render(request, 'blog/index.html', {'result': result})


def blog_post(request, post_id):
    res = post_id
    return render(request, 'blog/post.html', {'res': res})


def feedback(request):
    return render(request, 'blog/feedback.html', {})
