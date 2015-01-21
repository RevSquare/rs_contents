from django import template
from django.conf import settings
from bs4 import BeautifulSoup as bs


register = template.Library()


@register.assignment_tag()
def split_by_p_tag(html):
    """
    Return html splited by <p> tags
    """

    soup = bs(html)
    p_tags = []
    for p_tag in soup.find_all(settings.CONTENT_MAIN_TAGS):
        p_tags.append(unicode(p_tag))
    return p_tags
