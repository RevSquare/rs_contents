from django.core import serializers
from django.contrib import admin
from django.http import HttpResponse
from django.contrib.admin.options import csrf_protect_m
from django.contrib.admin.utils import unquote
from functools import update_wrapper


class AdminPreviewMix(admin.ModelAdmin):
    """
    Admin view for generate preview
    """

    @csrf_protect_m
    def preview_view(self, request, object_id=None, form_url='', extra_context=None):
        model = self.model
        opts = model._meta
        add = object_id is None
        if add:
            return HttpResponse('No preview for new objects')
        obj = self.get_object(request, unquote(object_id))

        ModelForm = self.get_form(request, obj)
        if request.method == 'POST':
            form = ModelForm(request.POST, request.FILES, instance=obj)
            if form.is_valid():
                form_validated = True
                new_object = self.save_form(request, form, change=not add)
                data = serializers.serialize('json', [new_object])
                request.session['preview_data_json_%s_%s' % (obj.__class__.__name__.lower(), obj.id)] = data
                return HttpResponse('success')
            else:
                return HttpResponse(form.errors)

    def get_urls(self):
        from django.conf.urls import patterns, url

        def wrap(view):
           def wrapper(*args, **kwargs):
               return self.admin_site.admin_view(view)(*args, **kwargs)
           return update_wrapper(wrapper, view)
        info = self.model._meta.app_label, self.model._meta.model_name
        urlpatterns = super(AdminPreviewMix, self).get_urls()
        urlpatterns += patterns('',
           url(r'^(.+)/preview$', wrap(self.preview_view), name='%s_%s_preview' % info),
        )
        return urlpatterns
