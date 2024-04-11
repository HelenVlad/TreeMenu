from django import template
from ...models import MenuItem

register = template.Library()


@register.simple_tag()
def draw_menu(id):
    flag = False
    all_items_parent = MenuItem.objects.filter(higher_level__isnull=True)
    html_code = ""

    for elem in all_items_parent:

        if elem.id == id:
            flag = True
            html_code += f"<em>{elem.name_item}</em>"
        else:
            html_code += f"<div>{elem.name_item}</div>"

        result = get_lower(elem, flag)
        flag = result["flag"]
        html_code += result["temp"]

    return html_code


def get_lower(object, flag, id=None, indent=20):
    temp = ""
    for subelement in object.lower_level.all():
        if ((id is None) or (subelement.id != id)) and not flag:
            temp += f"<p style=\"margin-left: {indent}px;\">{subelement.name_item}</p>"
            temp += get_lower(subelement, flag, id, indent + 20)["temp"]

        if subelement.id == id:
            flag = True
            temp += f"<p style=\"margin-left: {indent}px;\"><em>{subelement.name_item}</em></p>"
            temp += get_lower(subelement, flag, indent=indent + 20)["temp"]

    return {"temp": temp, "flag": flag}

