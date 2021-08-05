from django.urls import path
from blogs.views import HomePageView, BlogDetailView, CategoryPageView

app_name='blogs'
urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('detail/<slug:slug>/', BlogDetailView.as_view(), name='detailpage'),
    path('category/<str:name>/', CategoryPageView.as_view(), name='categorypage'),
]
