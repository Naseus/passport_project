# URL Patterns for the schedule section
from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    path('', views.index, name='index'),
    path('clients', views.ClientListings.as_view(), name = 'clientListings'),
    path('<pk>/updateposting', views.UpdatePostings.as_view(), name='updatePosting'),
    path('<pk>/editprofile', views.UpdateProfile.as_view(), name='editProfile'),
    path('createposting', views.CreatePosting.as_view(), name='createPosting'),
    path('<int:clientId>/postings', views.ClientPostings.as_view(), name='clientPostings'),
    path('editpostings', views.ModeratePostings.as_view(), name='editPostings'),
    path('<pk>/deleteposting', views.DeletePosting.as_view(), name='update'),
    path('<int:postingId>/apply',views.Apply.as_view(), name = 'apply'),
    path('error', views.Error.as_view(), name='error')
]
