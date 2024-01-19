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
    path("request-amount/<account_number>/",request_account.request_ammount, name="request_amount"),
    path("request-transaction/<account_number>/",request_account.request_transaction, name="request_transaction"),
    path("request-confirm/<account_number>/<transaction_id>/",request_account.request_confirm, name="request_confirm"),
    path("request-processing/<account_number>/<transaction_id>/",request_account.request_processing, name="request_processing"),
    path("request-complete/<account_number>/<transaction_id>/",request_account.request_complete, name="request_complete"),

    # Settlement
    path("confirm-settlement/<account_number>/<transaction_id>/",request_account.confirm_settlement, name="confirm_settlement"),
    path("process-settlement/<account_number>/<transaction_id>/",request_account.process_settlement, name="process_settlement"),
    path("complete-settlement/<account_number>/<transaction_id>/",request_account.complete_settlement, name="complete_settlement"),

]
