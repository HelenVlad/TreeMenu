from django import template
from ...models import MenuItem
from typing import Dict, Union
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag()
def draw_menu(id_item: int) -> str:
    """
    Отрисовывает меню

    :param id_item: Идентификатор пункта меню, который должен быть выделен курсивом.
    :type id_item: int
    :return: HTML-код для отображения меню.
    :rtype: str
    """
    all_items_parent = MenuItem.objects.filter(higher_level__isnull=True)
    if not all_items_parent.exists():
        return "Страница в разработке."

    flag = 0  # id для выделения еще не найден
    html_code = "<ul>"

    for elem in all_items_parent:
        html_code += '<li>'
        if elem.id == id_item:
            html_code += f"<a href='{elem.url}'><em>{elem.name_item}</em></a>"
            flag = 1
            id_item = None
            html_code += to_bottom(elem, flag=1)["temp"]

        elif flag == 1:
            html_code += f"<div><a href='{elem.url}'>{elem.name_item}</a></div>"

        elif flag == 0:
            html_code += f"<div><a href='{elem.url}'>{elem.name_item}</a></div>"
            result = to_bottom(elem, id_obj=id_item, flag=0)
            flag = result["flag"]
            html_code += result["temp"]

        html_code += '</li>'

    html_code += "</ul>"
    return mark_safe(html_code)


def to_bottom(obj: MenuItem, indent: int = 2, id_obj: Union[int, None] = None, flag: Union[int, None] = None) -> Dict[
    str, int]:
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
    local_flag = flag
    for subelement in obj.lower_level.all():
        design = f"<a href='{subelement.url}'>{subelement.name_item}</a>"
        if local_flag == 0:

            if id_obj:
                if subelement.id == id_obj:
                    design = f"<a href='{subelement.url}'><em>{subelement.name_item}</em></a>"
                    local_flag = 1
                    id_obj = None

            result = to_bottom(subelement, indent + 2, id_obj=id_obj, flag=local_flag)
            temp += f"""
               <ul style=\"margin-left: {indent}px;\">
                   <li>
                       {design}
                   </li>
                   {result["temp"]}
               </ul>
               """
            local_flag = result["flag"] if local_flag != 1 else local_flag

        elif local_flag == 1:
            temp += f"""
               <ul style=\"margin-left: {indent}px;\">
                   <li>
                       {design}
                   </li>
               </ul>
               """

        if local_flag not in [0, 1]:
            temp += "Error"

    return {"temp": temp, "flag": local_flag}
