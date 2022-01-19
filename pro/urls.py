
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns_api = [
    path('api/', include(('project.urls_api', 'Persons'), namespace='person_api')),
]

urlpatterns_root = [
    path('admin/', admin.site.urls),
    path('api/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns = urlpatterns_root + urlpatterns_api + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Administración nombre del proyecto'
admin.site.index_title = 'nombre del proyecto'
admin.site.site_title = 'Administración'
