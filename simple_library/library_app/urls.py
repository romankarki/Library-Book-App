from django.urls import path
from django.conf.urls import url
from  library_app import views

app_name = 'library_app'

urlpatterns = [
    
    path("books/",views.BooksListView.as_view(),name="books_list"),
    path("students/",views.StudentListView.as_view(),name="student_list"),
    path("bookuser/create/",views.BookUserCreateView.as_view(),name="create"),
    url(r'^students/(?P<pk>\d+)/$',views.StudentDetailView.as_view(),name="detail"),
    url(r'^students/bookuser/create/(?P<pk>\d+)/$',views.BookUserCreateView.as_view(),name="student_create"),
    url(r"^bookuser/list/(?P<pk>\d+)",views.BookUserListView.as_view(),name="bookuser_list"),
    url(r'^bookuser/delete/(?P<pk>\d+)/$',views.BookUserDeleteView.as_view(),name='delete'),
    #url(r"^bookuser/list/(?P<pk>\d+)/$",views.BookUserStudentListView.as_view(),name="bookuserstudent_list"),
    #url(r'^students/(?P<pk>\d+)/bookuser/list/$',views.BookUserListView.as_view(),name='student_bookuser'),

]

 