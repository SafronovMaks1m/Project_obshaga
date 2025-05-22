from django.urls import path, include
from obshaga import views

app_name = 'obshaga'

urlroom = [
    path('', views.room, name='room'),
    path('api/', views.api_room, name='api_room')
]

urlpatterns = [
    path('', views.base, name='base'),
    path('rooms/', views.rooms, name='rooms'),
    path('room/<int:id>/', include(urlroom)),
    path('top_violators/', views.top_violators, name='top'),
    path('api_violations/', views.api_violations, name='alerts'),
    path('api_violations/mark_read', views.api_violations_mark_read, name='alerts_mark')
]