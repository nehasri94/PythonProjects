"""
ASGI config for StudentManagement project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os
from rest_framework import routers
from Stu import views
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'StudentManagement.settings')

application = get_asgi_application()

router = routers.DefaultRouter()
router.register(r'StudentInfo', views.StudentInfoViewSet)
