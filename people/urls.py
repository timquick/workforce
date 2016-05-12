from django.conf.urls import patterns, url, include
from people.views import PeopleList,   ViewPerson,   NewPerson,   EditPerson,   DeletePerson
from people.views import CategoryList, ViewCategory, NewCategory, EditCategory, DeleteCategory

person_urls = patterns('',
    url(r'^$', ViewPerson.as_view(), name='person_detail'),
    url(r'^Update$', EditPerson.as_view(), name='person_update'),
    url(r'^Delete$', DeletePerson.as_view(), name='person_delete'),
)

category_urls = patterns('',
    url(r'^$', ViewCategory.as_view(), name='category_detail'),
    url(r'^Update$', EditCategory.as_view(), name='category_update'),
    url(r'^Delete$', DeleteCategory.as_view(), name='category_delete'),
)

urlpatterns = patterns('',
    url(r'^$', PeopleList.as_view(), name='people_list'),
    url(r'^(?P<slug>[\w-]+).person/', include(person_urls)),
    url(r'^NewPerson$', NewPerson.as_view(), name='person_add'),
    url(r'^Categories$', CategoryList.as_view(), name='category_list'),
    url(r'^(?P<slug>[\w-]+).cat/', include(category_urls)),
    url(r'^NewCategory$', NewCategory.as_view(), name='category_add'),
)