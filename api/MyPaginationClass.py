from rest_framework.pagination import PageNumberPagination

class MyPagination(PageNumberPagination):
    page_size=2
    page_query_param='records'
    max_page_size=4