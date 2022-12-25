from django.contrib import admin
from django.urls import path
from blog.views import frontpage, post_detail
from django.conf import settings
from django.conf.urls.static import static
from blog import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", frontpage),
    path("<slug:slug>/", post_detail, name="post_detail"),
    path("post/new/", views.CreatePostView.as_view(), name="post_new")
    
    ]

urlpatterns += static(settings.MEDIA_URL, docment_root=settings.MEDIA_ROOT)