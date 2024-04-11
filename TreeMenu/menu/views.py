from django.shortcuts import get_object_or_404, render
# from .models import MenuItem


def draw_menu(request, id):
    return render(request, "menu/main_page.html",
                  context={"main_menu": id})
