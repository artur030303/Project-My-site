from django.urls import path

from baskets import views

app_name = "baskets"

urlpatterns = [
    path(
        "basket_add/<slug:product_slug>/",
        views.BasketAddView.as_view(),
        name="basket_add",
    ),
    path(
        "basket_change/<int:basket_id>/",
        views.BasketChangeView.as_view(),
        name="basket_change",
    ),
    path(
        "basket_remove/<int:basket_id>/",
        views.BasketRemoveView.as_view(),
        name="basket_remove",
    ),
]
