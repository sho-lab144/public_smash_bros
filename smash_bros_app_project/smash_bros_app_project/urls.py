from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('matches/', include('matches.urls')),  # matchesアプリケーションへのルーティングを追加
    path('select2/', include('django_select2.urls')),
]
