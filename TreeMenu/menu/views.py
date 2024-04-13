from django.http import HttpRequest, HttpResponse
from typing import Union
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


def handle_invalid_id(request: HttpRequest, id: Union[int, float, str]) -> HttpResponse:
    """
    Обработчик запросов с недопустимым идентификатором.

    :param request: Запрос от клиента.
    :type request: HttpRequest
    :param id: Идентификатор меню.
    :type id: Union[int, float, str]
    :return: Ответ с сообщением об ошибке.
    :rtype: HttpResponse
    """
    return HttpResponse("Invalid ID")
