from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),  # 👈 ADICIONE ESSA LINHA
    path('admin/', admin.site.urls),
    # outras urls...
]
