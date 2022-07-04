from django.urls import path

from .views import ClassView, CreateClassView, CreateStudentView

urlpatterns = [
    path('classes/<int:class_id>', ClassView.as_view(), name='single_class'),
    path('classes', CreateClassView.as_view(), name='create_class'),
    path('students', CreateStudentView.as_view(), name='create_student'),
]
