from rest_framework.generics import ListAPIView
from api.models import Student
from api.serializer import StudentSerilalizer
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter,OrderingFilter 
from .MyPaginationClass import MyPagination
# from django_filters.rest_framework.DjangoFilterBackend

# Create your views here.

class StudentViewset(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerilalizer
    
    
    
    # ##----------Pagination-----
    # pagination_class=PageNumberPagination  # For global
    # pagination_class=MyPagination
   
    #-------------OrderingFilter--------
    
    # filter_backends=[OrderingFilter]
    # ordering_fields = ['name']
    
    
    
    
    ##-----------------Search Filter----------
    # filter_backends=[SearchFilter]
    # search_fields =['city']
    # search_fields=['name','city']
    # search_fields = ['^name']
    
   #filterset_fields = ['city','name']
   
   ##---------------filter by user------------------
    # def get_queryset(self):
    #     ''' Filter by User  '''
    #     user = self.request.user
    #     return Student.objects.filter(pass_by = user)
    
