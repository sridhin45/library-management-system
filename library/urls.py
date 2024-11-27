from django.urls import path
from library import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login_here',views.login_here,name='login_here'),
    path('add_category',views.add_category,name='add_category'),
    path('book',views.book,name='book'),
    path('book_view',views.book_view,name='book_view'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('logout',views.logout,name='logout'),
    path('home',views.home,name='home'),
    path('viewhistory',views.viewhistory,name='viewhistory'),
    path('viewreturn',views.viewreturn,name='viewreturn'),
    path('accept/<int:id>',views.accept,name='accept'),
    path('changeadmin',views.changeadmin,name='changeadmin'),
    path('adminpassaction',views.adminpassaction,name='adminpassaction'),


    
    
]
