from django.urls import path
from letter.views import LetterView, LetterItem

urlpatterns = [
    path("letter", LetterView.as_view(), name="letter"),
    path('letter-item/<int:id>', LetterItem.as_view(), name='letter-item'),
]
