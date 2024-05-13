from django.urls import path,include
from .views import AssessmentListCreateAPIView, AssessmentDetailUpdateDeleteAPIView

urlpatterns = [
    # URL pattern for listing and creating assessments
    path('assessments/', AssessmentListCreateAPIView.as_view(), name='assessment-list-create'),

    # URL pattern for retrieving, updating, and deleting individual assessments
    path('assessments/<int:pk>/', AssessmentDetailUpdateDeleteAPIView.as_view(), name='assessment-detail-update-delete'),
]
