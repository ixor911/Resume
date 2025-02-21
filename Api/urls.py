from django.urls import path, include
from .views import *

urlpatterns = [
    path('resume/', ResumeView.as_view(), name="resume"),
    path('resume/<int:pk>', ResumeView.as_view(), name="resume"),

    path('details/', DetailsView.as_view(), name="details"),
    path('details/<int:pk>', DetailsView.as_view(), name="details"),

]