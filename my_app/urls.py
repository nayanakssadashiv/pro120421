from django.urls import path
from my_app import views
app_name="my_app"
urlpatterns = [
    path("print1/",views.print1,name="print1"),
    path("print2/<name>/<age>/<phone_num>/",views.print2,name="print2"),
]

