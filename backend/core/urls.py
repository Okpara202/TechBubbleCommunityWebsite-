from django.urls import path
from .views import *

urlpatterns = [
    path('announcement/create', AnnouncementCreate.as_view(), name='create-announcement'),
    path('team/create', TeamCreate.as_view(), name='create-team'),
    path('expertise/create', ExpertiseCreate.as_view(), name='create-expertise'),
    path('message/create', MessageCreate.as_view(), name='create-expertise'),
    path('announcements/', AnnouncementList.as_view(), name='announcement'),
    path('expertise/', ExpertiseList.as_view(), name='expertise'),
    path('team/', TeamList.as_view(), name='announcement'),
    path('message/', MessageList.as_view(), name='announcement'),
    path('announcements/<int:pk>', AnnouncementDetail.as_view(), name='announcement-detail'),
    path('expertise/<int:pk>', ExpertiseDetail.as_view(), name='expertise-detail'),
]
