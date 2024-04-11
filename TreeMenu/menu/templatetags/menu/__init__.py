from django import template
from .menu_tags import draw_menu

register = template.Library()

register.tag('draw_menu', draw_menu)
