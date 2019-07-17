from django.urls import path
from .views import SomeView

urlpatterns = [
    path('secured-endpoint', SomeView.as_view(), name="secured-endpoint"),
]
