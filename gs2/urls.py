"""gs2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter
# from products import views

router=DefaultRouter()
router.register('StudentViewSet',views.StudentViewSet,basename="StudentViewSet")
router.register('StudentModelViewSet',views.StudentModelViewSet)
router.register('InstructorModelViewSet',views.InstructorModelViewSet)
router.register('CourseModelViewSet',views.CourseModelViewSet)
router.register('SingerModelViewSet',views.SingerModelViewSet,basename='singer')
router.register('SongModelViewSet',views.SongModelViewSet,basename='song')


urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('StudentAPI/',views.StudentAPI.as_view()),
    path('StudentAPI/<int:pk>',views.StudentAPI.as_view()),
    path('StudentGenericAPI',views.StudentGenericList.as_view()),
    path('StudentGenericAPI/<int:pk>',views.StudentRetrieveUpdateDestroyAPIView.as_view()),

    # path('api/message',views.message),
    # path('create-checkout-session',views.create_checkout_session),
    # path('',views.ProductLandingPage.as_view(),name='landing-page')

    # path('prodcuts',views.message)


]
