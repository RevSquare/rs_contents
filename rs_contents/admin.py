from cms_base.admin import ContentAbstractAdmin


class ContentPageImageAdmin(ContentAbstractAdmin):

    fieldsets = tuple(list(ContentAbstractAdmin.fieldsets) + [
        ('Image', {
            'classes': ('collapse',),
            'fields': (
                ('image', 'image_titre'),)
            }),
        ])


class ContentPageImagesAdmin(ContentAbstractAdmin):

    fieldsets = tuple(list(ContentAbstractAdmin.fieldsets) + [
        ('Images', {
            'classes': ('collapse',),
            'fields': (
                ('image_1', 'image_1_titre'),
                ('image_2', 'image_2_titre'),
                ('image_3', 'image_3_titre'),)
        }),
    ])