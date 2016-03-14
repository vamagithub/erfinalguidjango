from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin


urlpatterns = [
    url(r"^$", TemplateView.as_view(template_name="index.html"), name="home"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls")),

    #myupload
    url(r'^dash/', 'myupload.views.Form', name="dash"),
    url(r'^upload','myupload.views.Upload', name="upload"),

    #mycontact
    url(r"^contact/",'mycontact.views.contact',name="contact"),

    #myapp


    #policies footer

    url(r'^refund/', TemplateView.as_view(template_name='refund.html'), name='refund'),
    url(r"^tandc/", TemplateView.as_view(template_name='tandc.html'), name='tandc'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
