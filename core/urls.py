from django.urls import path

from .import views, transfer, transaction, request_account

urlpatterns = [
    path("", views.index, name="index"),
    
    # Transfers
    path("search/", transfer.search_account, name="search_account"),
    path("transfer-amount/<account_number>/", transfer.transfer_ammount, name="transfer_amount"),
    path("transaction/<account_number>/", transfer.transaction, name="transaction"),
    path("confirm-transfer/<account_number>/<transaction_id>/", transfer.confirm_transfer, name="confirm_transfer"),
    path("complete-transfer/<account_number>/<transaction_id>/",transfer.complete_transfer, name="complete_transfer"),
    path("complete-transaction/<account_number>/<transaction_id>/",transfer.complete_transaction, name="complete_transaction"),

    # Transaction
    path("transactions/", transaction.transaction_list, name="transactions"),
    path("transaction/<transaction_id>/detail/", transaction.transaction_detail, name="transaction_detail"),

    # Request payment
    path("request/", request_account.request_account, name="request_account"),
]
