from django.shortcuts import render
from django.views.generic import ListView,TemplateView,CreateView,DetailView,DeleteView
from  library_app.models import Books, Student, BookUser
from django.urls import reverse,reverse_lazy
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class IndexView(LoginRequiredMixin,TemplateView):
    login_url = 'accounts/login/'
    logout_url = ''
    template_name = "index.html"



class BooksListView(LoginRequiredMixin,ListView):
    logout_url = ''
    template_name = "books_list.html"
    context_object_name = 'books'
    model = Books

    def get_queryset(self):
       result = super(BooksListView, self).get_queryset()
       query = self.request.GET.get('search')
       if query:
          postresult = Books.objects.filter(title__contains=query)
          result = postresult
       else:
           result = Books.objects.all()
       return result


class StudentListView(LoginRequiredMixin,ListView):
    logout_url = ''
    template_name = "student_list.html"
    context_object_name = 'students'
    model = Student

    def get_queryset(self):
       result = super(StudentListView, self).get_queryset()
       query = self.request.GET.get('search')
       if query:
          postresult = Student.objects.filter(name__contains=query)
          result = postresult
       else:
           result = Student.objects.all()
       return result


            
    

class BookUserCreateView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    logout_url = ''
    model = BookUser
    fields = ('books','student','date_of_issue')    

    def get_success_url(self):
       
        return reverse('library_app:bookuser_list', kwargs={'pk': self.object.student.id})
    

    def get_initial(self):
        initial = super(BookUserCreateView, self).get_initial()
        initial['student'] = Student.objects.get(pk=self.kwargs['pk'])
        return initial

    # def update_db_field(self,name,field,value):
    #     Books.objects.get(name=name).update(field=value)



class BookUserListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    logout_url = ''
    model = BookUser
    context_object_name = "bookusers"
    template_name = 'library_app/bookuser_list.html'


    def get_queryset(self):
        queryset =  super().get_queryset()
        return queryset.filter(student =self.kwargs.get('pk') )


class BookUserDeleteView(LoginRequiredMixin,DeleteView):
    logout_url = ''
    model = BookUser

    # success_url = reverse_lazy("library_app:student_list")

    def get_success_url(self):
        return reverse_lazy('library_app:bookuser_list', kwargs={'pk': self.object.student.id})




class StudentDetailView(LoginRequiredMixin,DetailView):
    login_url = '/login/'
    logout_url = ''
    model = Student
    context_object_name = "student_detail"


# class BookUserStudentListView(ListView):

#     model = BookUser
#     context_object_name = ['student','bookstudent']


#     def get_queryset(self):
#         self.model= BookUser.objects.get(pk=self.kwargs['student'])
#         return  self.model



        


    






