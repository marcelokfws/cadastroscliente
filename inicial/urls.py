from cracha import settings
from django.conf.urls.static import static
from django.urls import path

from inicial import views

urlpatterns = [
    path('add/', views.add, name='add'),

]
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
