from django.urls import path
from . import views

app_name = "todo"

urlpatterns = [
    path('guest/', views.guest, name='guest'),
    path('list/', views.HomeView.as_view(), name='home'),
    path('create/', views.TodoCreateView.as_view(), name ="create"),
    path('success/<int:pk>', views.SuccessTodo, name ='success'),
    path('delete/<int:pk>', views.TodoDeleteView.as_view(), name ='delete'),
    path('list/<slug:slug>', views.TodoListView.as_view(), name ='list'),
    path('detail/<int:pk>', views.TodoDetailView.as_view(), name ='detail'),
    path('update/<int:pk>', views.TodoUpdateView.as_view(), name ='update'),
]