from django.urls import path

from competicoes import Views
app_name = 'competicoes'
urlpatterns = [
    path('', Views.dashboard_hackathon, name='dashboard_hackathon'),
    # path('', Views.list_hackathon, name='list_hackathon'),
    path('new', Views.create_hackathon, name='create_hackathon'),
    path('update', Views.update_hackathon, name='update_hackathon'),
    path('get', Views.get_hackathon, name='get_hackathon'),
]
