from django.views.generic import ListView, DetailView
from django.contrib import messages
from .models import *
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import  *


class IndexLV(ListView):
    model=Goods
    template_name = 'goods/index.html'
    context_object_name = 'goods_list'


def detail(request,goods_id):
    goods = get_object_or_404(Goods, pk=goods_id)
    context = {'goods': goods}
    return render(request,'goods/detail.html', context)









@login_required()
def goods_create(request):
    if request.method == 'POST':
        form = GoodsForm(request.POST, request.FILES['image'])

        if form.is_valid():
            goods = form.save(commit=False)
            goods.author = request.user
            goods.image = request.FILES['image']
            goods.save()
            return redirect('goods:index')
    else:
        form = GoodsForm()
    return render(request, 'goods/create.html')


@login_required(login_url='common:login')
def goods_delete(request, goods_id):
    goods = get_object_or_404(Goods,pk=goods_id)
    if request.user != goods.author:
        messages.error(request, '작성자가아닙니다'),
        return redirect('goods:detail',goods_id=goods_id)
    goods.delete()
    return redirect('goods:index')


@login_required(login_url='common:login')
def comment_create(request, goods_id):
    pass
    if request.method == 'POST':
        goods = get_object_or_404(Goods, pk=goods_id)
        goods.comment_set.create(text=request.POST.get('text'), author=request.user)
        return redirect('goods:detail',goods_id=goods_id)


def comment_delete(request,comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request,'삭제권한이 없습니다')
    else:
        comment.delete()
    return redirect('goods:detail', goods_id=comment.goods.id)


@login_required(login_url='common:login')
def comment_modify(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('goods:detail',goods_id=comment.goods.id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment.save()
            return redirect('goods:detail', goods_id=comment.goods.id)


@login_required(login_url='common:login')
def modify(request, goods_id):
    goods = get_object_or_404(Goods, goods_id)
    if request.user != goods.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('goods:detail', goods_id=goods_id)

    if request.method == 'POST':
        form = GoodsForm(request.POST, instance=goods)
        if form.is_valid():
            goods.save()
            return redirect('goods:detail', goods_id=goods_id)












def index(request):
    goods_list = Goods.objects.all()
    context = {'goods_list': goods_list}

    return render(request, 'goods/index.html', context)