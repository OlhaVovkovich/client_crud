from django.urls import path
from .views import ClientList, ClientCreate, ClientUpdate, ClientDelete

urlpatterns = [

    path('', ClientList.as_view(), name='client-list'),
    path('create/', ClientCreate.as_view(), name='client-create'),
    path('<int:pk>/update/', ClientUpdate.as_view(), name='client-update'),
    path('<int:pk>/delete/', ClientDelete.as_view(), name='client-delete'),

]

