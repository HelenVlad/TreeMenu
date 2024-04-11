from django.urls import path

from .views import draw_menu

urlpatterns = [
    path('<int:id>/', draw_menu, name='draw_menu'),
]
