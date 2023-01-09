from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_members, name='get_members'),
    path('<int:member_id>', views.get_member, name='get_member'),
    path('add', views.add_member, name='add_member'),
    path('update', views.update_member, name='update_member'),
    path('delete/<int:member_id>', views.delete_member, name='delete_member'),
]
