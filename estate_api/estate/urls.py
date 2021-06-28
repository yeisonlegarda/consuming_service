from django.urls import path
from estate import views

app_name = 'estates'


urlpatterns = [
    path('userFilter/',
         views.StatusPropertyViewSet.as_view(),
         name='userfilter')
]
