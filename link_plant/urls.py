from django.urls import path
from .views import LinkListView, LinkCreate, LinkUpdate, DeleteView, profile_view

urlpatterns = [
    path('', LinkListView.as_view(), name="link-list"),
    path('link/create/', LinkCreate.as_view(), name="link-create"),
    path('link/<int:pk>/update/', LinkUpdate.as_view(), name="link-update"),
    path('link/<int:pk>/delete/', DeleteView.as_view(), name="link-delete"),
    path('<slug:profile_slug>/', profile_view, name="profile"),
]
