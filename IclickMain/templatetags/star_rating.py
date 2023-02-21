from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def star_rating(rating):
    full_star = int(rating)
    empty_star = 5 - full_star
    star_html = ""
    for i in range(full_star):
        star_html += '<i class="fa fa-star"></i>'
    for i in range(empty_star):
        star_html += '<i class="fa fa-star-o"></i>'
    return mark_safe(star_html)
