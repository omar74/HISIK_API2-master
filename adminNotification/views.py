from django.shortcuts import render

from .models import NotificationAdmin
from .serializer import NotificationAdminSerializer
from rest_framework import generics


class AdminNotificationListView(generics.ListCreateAPIView):
    permission_classes          = []
    authentication_classes      = []
    queryset                    = NotificationAdmin.objects.all()
    serializer_class            = NotificationAdminSerializer

    def create(self, request, *args, **kwargs):
        ''' I wanted to do some stuff with serializer.data here '''
        return super(AdminNotificationListView, self).create(request, *args, **kwargs)


class AdminNotficationDetailedView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes          = []
    authentication_classes      = []
    queryset                    = NotificationAdmin.objects.all()
    serializer_class            = NotificationAdminSerializer
    lookup_field                = 'type'


