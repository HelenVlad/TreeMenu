from django import template
from ...models import MenuItem
from typing import Dict, Union
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag()
def draw_menu(id_item: int) -> str:
    """
    Выводит меню с заданным идентификатором.

    :param id_item: Идентификатор пункта меню, который должен быть выделен курсивом.
    :type id_item: int
    :return: HTML-код для отображения меню.
    :rtype: str
    """
    flag = 0
    all_items_parent = MenuItem.objects.filter(higher_level__isnull=True)
    html_code = "<ul>"

    for elem in all_items_parent:
        html_code += '<li>'
        if elem.id == id_item:
            html_code += f"<a href='{elem.url}'><em>{elem.name_item}</em></a>"
            flag = 1
            id_item = None
        else:
            html_code += f"<div><a href='{elem.url}'>{elem.name_item}</a></div>"

        result = get_lower(elem, flag, id_item)
        flag = result["flag"]
        html_code += result["temp"]

        html_code += '</li>'

    html_code += "</ul>"
    return mark_safe(html_code)


def get_lower(obj: MenuItem, flag: int, id_obj: Union[int, None] = None, indent: int = 20) -> Dict[str, int]:
    """
    Получает нижний уровень меню для заданного пункта.

    :param obj: Объект пункта меню.
    :type obj: MenuItem
    :param flag: Флаг, указывающий на текущее состояние обработки.
    :type flag: int
    :param id_obj: Идентификатор пункта меню для выделения.
    :type id_obj: int
    :param indent: Отступ для вложенных пунктов меню.
    :type indent: int
    :return: HTML-код для отображения нижнего уровня меню и флаг
    :rtype: dict
    """
    temp = ""
    for subelement in obj.lower_level.all():
        if ((id_obj is None) or (subelement.id != id_obj)) and flag == 0:
            temp += f"""
            <p style=\"margin-left: {indent}px;\">
                <a href='{subelement.url}'>{subelement.name_item}</a>
            </p>
            """
            temp += get_lower(subelement, flag, id_obj, indent + 20)["temp"]

        if flag == 1:
            temp += f"""
            <p style=\"margin-left: {indent}px;\">
                <a href='{subelement.url}'>{subelement.name_item}</a>
            </p>
            """

        if subelement.id == id_obj:
            flag = True
            temp += f"""
            <p style=\"margin-left: {indent}px;\">
                <a href='{subelement.url}'> 
                <em>{subelement.name_item}</em>
                </a>
            </p>
            """
            temp += get_lower(subelement, flag, indent=indent + 20)["temp"]

        if flag not in [0, 1, 2]:
            print("Error")

    flag = 2 if flag == 1 else flag
    return {"temp": temp, "flag": flag}
