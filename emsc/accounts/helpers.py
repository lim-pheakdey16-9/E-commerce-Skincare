# emsc/accounts/templatetags/helpers.py
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def btn_submit():
    return mark_safe('<button class="tf-button w288" type="submit">Save</button>')