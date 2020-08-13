from django.urls import path
from .views import index, person_list, person_list_with_detail_href


urlpatterns = [
    path('', index, name='index'),
    path('person/', person_list, name='person_list'),
    path('person-with-detail-href/', person_list_with_detail_href, name='person_list_with_detail_href'),
]
