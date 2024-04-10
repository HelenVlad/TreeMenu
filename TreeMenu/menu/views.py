from django.shortcuts import get_object_or_404, render
from django.views import View
from .models import MenuItem


class MenuView(View):
    def get(self, request, id):
        menu_item = get_object_or_404(MenuItem, id=id)
        return render(request, "menu/main_page.html", context={"menu_item": menu_item})
