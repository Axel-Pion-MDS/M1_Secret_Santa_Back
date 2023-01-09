from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_promotions, name='get_promotions'),
    path('<int:promotion_id>', views.get_promotion, name='get_promotion'),
    path('add', views.add_promotion, name='add_promotion'),
    path('update', views.update_promotion, name='update_promotion'),
    path('delete/<int:promotion_id>', views.delete_promotion, name='delete_promotion'),
]
