from django.urls import path
from invoice.views import InvoiceView, InvoiceItem
from invoice.payment_views import PaymentReq, PaymentVerify

urlpatterns = [
    path("invoice", InvoiceView.as_view(), name="invoice"),
    path('invoice-item/<int:id>', InvoiceItem.as_view(), name='invoice-item'),
    path("payment-request/<int:id>/",PaymentReq.as_view(),name="payment-request"),
    path("payment-verify/<int:id>/",PaymentVerify.as_view(),name="payment-verify"),
]
