from django.urls import path
from  .views import home_views, myfirst_views, accounts_view, access_view, skin_hair_view, novelties_view, bags_view, search_results
urlpatterns=[
    path('',home_views, name='home'),
    path('members/', myfirst_views, name='members'),
    path('accounts/',accounts_view, name='accounts'),
    path('access/',access_view, name='access'),
    path('access/skin_hair/',skin_hair_view, name='skin_hair'),
    path('access/novelties/',novelties_view, name='novelties'),
    path('access/bags/',bags_view, name='bags'),
    path('search/', search_results, name='search_results'),
]