from django.urls import path
from .views import (
ip_create_view,
ip_detail_view,
dynamic_lookup_view,
ip_delete_view,
ip_listview
)
app_name = 'ips'
urlpatterns = [
    path('ip/',ip_detail_view,name='ipdetail'),
    path('ipcreate/', ip_create_view, name='ipcreate'),
    path('iplist/', ip_listview, name='iplist'),
    path('ipdelete/<int:id>/', ip_delete_view, name='ipdelete'),
    path('ipdyn/<int:my_id>/',dynamic_lookup_view, name='ipdyn'),
]