from django.urls import path

from .views import CreateClassView, CreateStudentView

urlpatterns = [
    path('classes', CreateClassView.as_view(), name='create_class'),
    path('students', CreateStudentView.as_view(), name='create_student'),
]
