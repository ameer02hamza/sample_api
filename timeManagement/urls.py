from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('timesheet', views.timeSheetViewSet)
router.register('pilelogs', views.pileLogViewSet)
urlpatterns = []
urlpatterns += router.urls
