from django.urls import path
from .views import DashboardHomeView, NewslettersDashboardHomeView, NewslettersCreateView, NewslettersDetailView, NewslettersUpdateView

app_name = "dashboard"

urlpatterns = [
    path('',DashboardHomeView.as_view(), name = "home"),
    path('list/',NewslettersDashboardHomeView.as_view(), name = "list"),
    path('create/',NewslettersCreateView.as_view(), name = "create"),
    path('detail/<int:pk>',NewslettersDetailView.as_view(), name = "detail"),
    path('update/<int:pk>',NewslettersUpdateView.as_view(), name = "update"),
    path('delete/<int:pk>',NewslettersUpdateView.as_view(), name = "delete"),
]
