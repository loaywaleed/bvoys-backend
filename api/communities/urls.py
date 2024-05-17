from django.urls import path
from . import views


urlpatterns = [
    path('',
         views.CommunityListCreate.as_view(),
         name='community-view-create'),
    path('<int:id>', views.CommunityRetrieveUpdateDestroyAPIView.as_view(), name="community-update-delete")
]