from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path("about/", views.about, name="AboutUs"),
    path("addQ/", views.addQ, name="AddQuestion"),
    path("deleteQ/<int:myid>/", views.delete, name="DeleteQuestion"),
    path("updateQ/<int:myid>/", views.update, name="UpdateQuestion"),
    path("generateQ", views.generate, name="GenearteQuestion"),
    path("create", views.create, name="CreateQuestion"),
    path("login", views.login, name="login"),
    path("signup", views.handleSignup, name="handleSignup"),
    #path("updateQ/<str:pk>/", views.createupdate, name="Update"),

]
