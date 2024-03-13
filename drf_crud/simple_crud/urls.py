from django.urls import path, re_path
from . import views
app_name = 'simple_crud'
"""
 Why do we use the app name?
 - django.core.exceptions.ImproperlyConfigured: Specifying a namespace in include() without providing an app_name is not supported. Set 
 the app_name attribute in the included module, or pass a 2-tuple containing the list of patterns and app_name instead.
"""

urlpatterns = [
    path('tutorials', views.tutorial_list, name='tutorials'),
    re_path(r'^tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail, name='tutorial_detail'),
    path('tutorials/published', views.tutorial_list_published, name='tutorials_published')
]