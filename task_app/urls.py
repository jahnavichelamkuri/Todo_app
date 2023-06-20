from django.urls import path
#from .import views
from .views import DataView, Todo
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    #path('', views.index, name="index"),  
    # path('',TaskList.as_view(), name='tasks'), 
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('data/', DataView.as_view(), name='data'),
    path('todo/',Todo.as_view()),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
