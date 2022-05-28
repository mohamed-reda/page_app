# pages/urls.py
from django.urls import path
# from .views import homePageView
# from django.urls import path, include  # new
# 
# urlpatterns = [
#     path('', homePageView, name='home'),
# 
#     path('', include('pages.urls')),  # new
# ]

from django.urls import path
from .views import HomePageView, AboutPageView  # new

urlpatterns = [
    # the main page is
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),  # new

]
# Our URLpattern has three parts:
# • a Python regular expression for the empty string ''
# • a reference to the view called homePageView
# • an optional named URL pattern37 called 'home'
