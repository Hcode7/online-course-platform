from django import template

register = template.Library()

@register.filter(name='truncate_words')
def truncate_words(value, arg):
    """
    Truncates a string after a certain number of words.
    """
    words = value.split()
    if len(words) > arg:
        words = words[:arg]
        return ' '.join(words) + '...'
    else:
        return value
