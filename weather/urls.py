from django.conf.urls import url
from django.contrib import admin
from wxpoint import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'weather.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

#   url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home_page, name='home'),
    url(r'^models/', views.model_page, name="models"),
    url(r'^create_post/$', views.model_page, name="create_post"),
]
