from django.urls import path
from student import views

urlpatterns = [
    path('user_register',views.user_register,name='user_register'),
    path('student_home',views.student_home,name='student_home'),
    path('view_book',views.view_book,name='view_book'),
    path('book_ing/<int:id>',views.book_ing,name='book_ing'),
    path('reserved',views.reserved,name='reserved'),
    path('returned/<int:id>',views.returned,name='returned'),
    path('myhistory',views.myhistory,name='myhistory'),
    path('profile',views.profile,name='profile'),
    path('changestudent',views.changestudent,name='changestudent'),
    path('studentpassaction',views.studentpassaction,name='studentpassaction'),
    path('forgot',views.forgot,name='forgot'),
    path('detailsaction',views.detailsaction,name='detailsaction'),
    path('useraction',views.useraction,name='useraction'),
    path('finalaction',views.finalaction,name='finalaction')


    
]
