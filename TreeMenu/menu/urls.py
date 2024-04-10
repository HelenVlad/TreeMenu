from django.urls import path

from .views import MenuView

urlpatterns = [
    # path("", views.index, name="index"),
    path('<int:id>/', MenuView.as_view(), name='menu'),
]
