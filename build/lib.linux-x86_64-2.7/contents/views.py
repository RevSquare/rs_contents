from django.http import Http404
from django.views.generic import DetailView
from .preview.views import PreviewMix, preview_object


class ArticleDetailViewMix(PreviewMix, DetailView):
    """
    Article detail view - for all models based on ContentPages
    """

    template_name = 'contents/article.html'

    def get_queryset(self):
        return self.model.objects.all()

    @preview_object
    def get_object(self, queryset=None):
        obj = super(ArticleDetailViewMix, self).get_object(queryset)
        if obj.is_public or obj.author_id == self.request.user.id:
            return obj
        raise Http404

