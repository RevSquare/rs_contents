from django.core import serializers
from django.views.generic.base import View


def preview_object(func):
    def wrap(cls, *args):
        if cls.preview:
            deserialize_list = serializers.deserialize("json", cls.preview)
            deserialize = deserialize_list.next()
            return deserialize.object
        return func(cls, *args)
    return wrap


class PreviewMix(View):
    preview = None

    def get(self, request, *args, **kwargs):
        if 'preview' in request.GET:
            pk = self.kwargs.get(self.pk_url_kwarg, None)
            data = request.session['preview_data_json_%s_%s' % (self.model.__name__.lower(), pk)]
            if data:
                self.preview = data
        return super(PreviewMix, self).get(request, *args, **kwargs)
