from django.urls import path

from . import views

from apuntapp.views import PublisherListView

urlpatterns = [
    #path('PublisherListView/', PublisherListView.as_view())
    path('', views.index, name='index'),
]