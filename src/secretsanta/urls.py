from django.urls import path

from . import views

urlpatterns = [
    # Santa
    path('', views.get_santas, name='get_santas'),
    path('<int:santa_id>', views.get_santa, name='get_santa'),
    path('add', views.add_santa, name='add_santa'),
    path('update/<int:santa_id>', views.update_santa, name='update_santa'),
    path('delete/<int:santa_id>', views.delete_santa, name='delete_santa'),
    # Santa members
    path('<int:santa_id>', views.get_santa_members,
         name='get_santa_members'),
    path('<int:santa_id>/member/<int:member_id>', views.get_santa_member,
         name='get_santa_member'),
    path('<int:santa_id>/add', views.add_santa_member,
         name='add_santa_member'),
    path('<int:santa_id>/update/<int:member_id>',
         views.update_santa_member, name='update_santa_member'),
    path('<int:santa_id>/delete/<int:member_id>',
         views.delete_santa_member, name='delete_santa_member'),
]
