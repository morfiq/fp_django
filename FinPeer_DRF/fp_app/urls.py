from . import views
from django.urls import path

urlpatterns = [
    # path('', views.AllData.as_view()),
    path('', views.app_homepage, name='app_homepage'),
    path('contact_us', views.contact_us, name="contact_us"),
    path('upload', views.UploadFileView.as_view()),
    # path('upload', views.UploadFileView.as_view(), name='upload-file')
    path('register', views.register, name="register"),
    path('signin', views.signin, name='signin'),
    path('loggedin', views.loggedin, name='loggedin'),
    path('logout', views.logout, name="logout"),
    path('userlist', views.UserListView.as_view(), name='userlist'),
    path('userdetail/<int:pk>/',
         views.UserDetailView.as_view(template_name='user_detail.html'),
         name='userdetail'),
    path('usercreate/',
         views.UserCreateView.as_view(template_name='user_create.html'),
         name='usercreate'),
    path('userupdate/<int:pk>/',
         views.UserUpdateView.as_view(template_name='user_create.html'),
         name='userupdate'),
    path('userdelete/<int:pk>/',
         views.UserDeleteView.as_view(template_name='user_confirm_delete.html'),
        name='userdelete'),
    path('fpdata',views.all_data,name='fpdata'),
]