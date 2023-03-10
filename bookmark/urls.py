import imp
from django.urls import path
from bookmark import views

app_name = 'bookmark'

urlpatterns = [
    #/bookmark/
    path('',views.BookmarkLV.as_view(), name='index'),
    #/bookmark/99
    path('<int:pk>/',views.BookmarkDV.as_view(), name ='detail'),
    
    #/bookmart/add/
    path('add/',views.BookmarkCreateView.as_view(), name="add",),
    #/bookmark/change/
    path('change/',views.BookmarkChangeLV.as_view(), name="change",),
    #/bookmark/99/update/
    path('<int:pk>/update/',views.BookmarkUpdateView.as_view(), name="update",),
    #/bookmark/99/delete/
    path('<int:pk>/delete/',views.BookmarkDeleteView.as_view(), name="delete",),

]




