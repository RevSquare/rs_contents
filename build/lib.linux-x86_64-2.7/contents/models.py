import re
from contentpages.models import ContentPageImageAbstract


class ContentTypeNameMixIn(object):

    def content_type_name(self):
        return u' '.join(
            re.findall(r'[A-Z][^A-Z]*', self.__class__.__name__))


class ContentAbstract(ContentPageImageAbstract, ContentTypeNameMixIn):
    """
    Base class for all Content models in IBM
    """

    class Meta:
        abstract = True
