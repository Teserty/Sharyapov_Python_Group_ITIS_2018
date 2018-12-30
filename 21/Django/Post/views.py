from django.shortcuts import render
from Post.models import *


def postList(request):
    list = Post.objects.order_by("created_date")
    return render(request, "post/postList.html", {'postList': list})
# Create your views here.
