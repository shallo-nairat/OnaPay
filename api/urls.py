from django.urls import path
from .views import AccountListView, AccountDetailView ,  StatementListView, StatementDetailView # Import both views

urlpatterns = [
    path('accounts/', AccountListView.as_view(), name='account-list'),  # For listing and creating accounts
    path('accounts/<int:id>/', AccountDetailView.as_view(), name='account-detail'),  # For retrieving and updating accounts
    path('accounts/<int:account_id>/statements/', StatementListView.as_view(), name='statement-list'),
    path('statements/<int:pk>/', StatementDetailView.as_view(), name='statement-detail'),
]
