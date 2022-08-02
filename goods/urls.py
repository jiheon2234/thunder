from django.urls import path
from . import views


app_name='goods'
urlpatterns=[
    path('', views.IndexLV.as_view(),name='index'),
    path('<int:goods_id>', views.detail, name='detail'),
    path('goods_create',views.goods_create,name='create'),
    path('goods_delete/<int:goods_id>', views.goods_delete, name='delete'),
    path('comment_create/<int:goods_id>',views.comment_create, name='comment_create'),
    path('comment_delete/<int:comment_id>', views.comment_delete, name='comment_delete'),
    path('comment_modify/<int:comment_id', views.comment_modify, name='comment_modify')
    # path('goods_modify/<int:goods_id>',views.goods_modify, name='modify'),
]