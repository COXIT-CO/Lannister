from django.urls import path

from .views import (
    BonusRequestHistoryList,
    BonusRequestHistorySingle,
    BonusRequestList,
    BonusRequestSingle,
    ReviewerBonusRequestList,
    ReviewerList,
    ReviewerSingle,
    UserList,
    UserSingle,
    WorkerBonusRequestList,
    WorkerList,
    WorkerSingle,
)

urlpatterns = [
    path("requests/", BonusRequestList.as_view(), name="bonus_request-list"),
    path("requests/<int:pk>", BonusRequestSingle.as_view(), name="bonus_request-single"),
    path("requests/worker/<int:pk>", WorkerBonusRequestList.as_view(), name="worker-bonus_request-list"),
    path("requests/reviewer/<int:pk>", ReviewerBonusRequestList.as_view(), name="reviewer-bonus_request-list"),
    path("requests_history/", BonusRequestHistoryList.as_view(), name="bonus_request_history-list"),
    path("requests_history/<int:pk>", BonusRequestHistorySingle.as_view(), name="bonus_request_history-single"),
    path("users/", UserList.as_view(), name="user-list"),
    path("users/<int:pk>", UserSingle.as_view(), name="user-single"),
    path("reviewers/", ReviewerList.as_view(), name="reviewers-list"),
    path("reviewers/<int:pk>", ReviewerSingle.as_view(), name="reviewer-single"),
    path("workers/", WorkerList.as_view(), name="workers-list"),
    path("workers/<int:pk>", WorkerSingle.as_view(), name="worker-single"),
]
