from django.conf.urls import url, patterns, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.conf import settings
from products.views import IndexView, LoginView, LogoutView, CategoryDetailView, ProductView
from products.views import CategoryView, LastProductsView
admin.autodiscover()

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^products/$', CategoryView.as_view(), name='products'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^products/(?P<slug>[\w-]+)/$', CategoryDetailView.as_view(), name='category'),
    url(r'^products/(?P<slug>[\w-]+)/(?P<pslug>[\w-]+)$', ProductView.as_view(), name='product'),
    url(r'^last/$', login_required(LastProductsView.as_view(),login_url='/login/'), name='last'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
