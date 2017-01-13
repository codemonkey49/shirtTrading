from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r"profile",views.profile,name="profile"),
    url(r"browse",views.browse,name="browse"),
    url(r"detail/(?P<userName>.*)/",views.detail,name="detail"),
    url(r"messages/",views.messages,name="messages"),
    ]