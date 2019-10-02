from django.urls import path
from .views import *
from django.views.generic.base import RedirectView

urlpatterns = [
	path('authors/', AuthorList.as_view(), name='authors'),
	path('authors/<int:pk>',AuthorDetail.as_view(), name='author-detail'),
	path('myview/', MyView.as_view(), name='my-view'),
	path('mytemplateview/', MyTemplateView.as_view(), name='my-template-view'),
	path('go-to-django/', RedirectView.as_view(url='https://djangoproject.com'), name='go-to-django'),
]