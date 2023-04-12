from django.urls import path

from . import views

# views.index() -> HttpResponse
# views.QuestionListView.as_view() -> object() -> HttpResponse

urlpatterns = [
    path('', views.ClientListView.as_view()),
    path('<int:client_id>/', views.ClientDetailView.as_view(), name='client_detail'),

]
