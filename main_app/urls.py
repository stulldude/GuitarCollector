from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('guitars/', views.guitars_index, name='index'),
    path('guitars/<int:gtr_id>/', views.guitars_detail, name='detail'),
    path('guitars/<int:pk>/update/', views.GuitarUpdate.as_view(), name='guitar_update'),
    path('guitars/<int:pk>/delete/', views.GuitarDelete.as_view(), name='guitar_delete'),
    path('guitars/create/', views.GuitarCreate.as_view(), name='guitar_create'),
    path('guitars/<int:gtr_id>/add_mod/', views.add_mod, name='add_mod'),
    path('guitars/<int:gtr_id>/assoc_amp/<int:amp_id>/', views.assoc_amp, name='assoc_amp'),
    path('guitars/<int:gtr_id>/unassoc_amp/<int:amp_id>/', views.unassoc_amp, name='unassoc_amp'),
    path('amps/', views.AmpList.as_view(), name='amp_index'),
    path('amps/<int:pk>/', views.AmpDetail.as_view(), name='amps_detail'),
    path('amps/create/', views.AmpCreate.as_view(), name='amps_create'),
    path('amps/<int:pk>/update/', views.AmpUpdate.as_view(), name='amps_update'),
    path('amps/<int:pk>/delete/', views.AmpDelete.as_view(), name='amps_delete'),
]