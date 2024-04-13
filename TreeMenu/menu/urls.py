from django.urls import path, re_path
from .views import draw_menu, handle_invalid_id

urlpatterns = [
    path('', draw_menu, kwargs={'id': 0}, name='draw_menu_base'),
    path('<int:id>/', draw_menu, name='draw_menu'),
    re_path(r'^(?P<id>[^/]+)/$', handle_invalid_id, name='handle_invalid_id'),
]
