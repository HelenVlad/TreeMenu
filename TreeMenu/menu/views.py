from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def draw_menu(request: HttpRequest, id: int) -> HttpResponse:
    """
    Отображает страницу с основным меню.

    :param request: Запрос от клиента.
    :type request: HttpRequest
    :param id: Идентификатор меню.
    :type id: int
    :return: Отображение страницы с основным меню.
    :rtype: HttpResponse
    """
    return render(request, "menu/main_page.html",
                  context={"main_menu": id})
