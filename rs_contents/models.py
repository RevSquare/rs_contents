import re

from django.db import models
from django_brightcove.fields import BrightcoveField

from filebrowser.fields import FileBrowseField
from cms_base.abstract import CmsContentAbstract


class ContentPageAbstract(CmsContentAbstract):
    """
    Store content pages data.
    Extend :class:`cms_base.abstract.CmsContentAbstract` with
    basic fields for content page (title, subtitle, text and author)
    """

    class Meta:
        abstract = True
        verbose_name = 'Content Page'
        verbose_name_plural = 'Content Pages'

    @models.permalink
    def get_absolute_url(self):
        return ('%s_detail' % self.__class__.__name__.lower(),
                (self.slug, self.pk))


class ContentPageImageAbstract(ContentPageAbstract):

    image = FileBrowseField(extensions=('.jpg', '.png'),
        null=True, blank=True, max_length=255)
    image_titre = models.CharField('Titre', max_length=255,
        null=True, blank=True)

    class Meta:
        abstract = True


class ContentPageImagesAbstract(ContentPageAbstract):

    image_1 = FileBrowseField(extensions=('.jpg', '.png'),
        null=True, blank=True, max_length=255)
    image_1_titre = models.CharField('Titre', max_length=255,
        null=True, blank=True)

    image_2 = FileBrowseField(extensions=('.jpg', '.png'),
        null=True, blank=True, max_length=255)
    image_2_titre = models.CharField('Titre', max_length=255,
        null=True, blank=True)

    image_3 = FileBrowseField(extensions=('.jpg', '.png'),
        null=True, blank=True, max_length=255)
    image_3_titre = models.CharField('Titre', max_length=255,
        null=True, blank=True)

    class Meta:
        abstract = True

    @property
    def images(self):
        """return list of images with titre"""
        images = []
        for i in range(1, 4):
            im = getattr(self, 'image_%d' % i)
            if im:
                images.append({'image': im,
                               'titre': getattr(self, 'image_%d_titre' % i)})
        return images


class ContentPageVideoAbstract(ContentPageImagesAbstract):
    """
    Content Page with video
    """

    brightcove = BrightcoveField(null=True, blank=True)
    brightcove_image = FileBrowseField(extensions=('.jpg', '.png'),
        null=True, blank=True, max_length=255)

    class Meta:
        abstract = True

    @property
    def is_video(self):
        """return True if object has video"""
        return bool(self.brightcove)

    def get_next_previous_queryset(self):
        """
        return queryset used in get_next and get_previous_method
        """
        return self.__class__.objects.get_content()


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
