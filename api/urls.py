from django.conf.urls import url

from api import views

# router = routers.DefaultRouter ()
# router.register (r'user', views.UserViewSet)
# router.register (r'apar', views.AparViewSet)
# urlpatterns = router.urls

urlpatterns = [
    url (r'^all$', views.AparViewSet.as_view ()),
    url (r'^(?P<id>[\d]+)$', views.AparDetail.as_view ()),
    url (r'^add$', views.add),
    url (r'^inspect/(?P<id>[\d]+)$', views.inspect),
    url (r'^refill/(?P<id>[\d]+)$', views.refill)
]