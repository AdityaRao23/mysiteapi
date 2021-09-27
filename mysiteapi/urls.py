from django.urls import include, path
from rest_framework import routers
from myapp import views
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'Heroes', views.HeroViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('heroes/', include('myapp.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]