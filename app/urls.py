from django.urls import path
from .views import home_view, blog_view, checkout_view, contact_view, cart_view
urlpatterns = [
    path('', home_view),
    path('blog/', blog_view),
    path('checkout/', checkout_view),
    path('contact/', contact_view),
    path('cart/', cart_view)
]
