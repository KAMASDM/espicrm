"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from Master.schema import schema as master_schema
from Enquiry.schema import schema as enquiry_schema
from Application.schema import schema as application_schema
from Assessment.schema import schema as assessment_schema
from DetailEnquiry.schema import schema as detail_enquiry_schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/master/', GraphQLView.as_view(graphiql=True, schema=master_schema), name='graphql-master'),
    path('graphql/enquiry/', GraphQLView.as_view(graphiql=True, schema=enquiry_schema), name='graphql-enquiry'),
    path('graphql/application/', GraphQLView.as_view(graphiql=True, schema=application_schema), name='graphql-application'),
    path('graphql/assessment/', GraphQLView.as_view(graphiql=True, schema=assessment_schema), name='graphql-assessment'),
    path('graphql/detail-enquiry/', GraphQLView.as_view(graphiql=True, schema=detail_enquiry_schema), name='graphql-detail-enquiry'),
]
