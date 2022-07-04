from django.urls import path

from .views import CreateClassView

urlpatterns = [
    path('classes', CreateClassView.as_view(), name='create_class'),
]
