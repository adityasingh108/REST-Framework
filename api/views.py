from rest_framework.generics import ListAPIView
from api.models import Student
from api.serializer import StudentSerilalizer
# from django_filters.rest_framework.DjangoFilterBackend

# Create your views here.

class StudentViewset(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerilalizer
    filterset_fields = ['city','name']
    
    # def get_queryset(self):
    #     ''' Filter by User  '''
    #     user = self.request.user
    #     return Student.objects.filter(pass_by = user)
    
