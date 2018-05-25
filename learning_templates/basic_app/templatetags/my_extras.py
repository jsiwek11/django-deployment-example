from django import template

register = template.Library()

@register.filter(name='cut')

def cut(value,arg):
    """

    This cuts out all values of "arg" from the string
    """

    return value.replace(arg,'')

# register the new filter with system - 'cut' is the name
# register.filter('cut',cut)
