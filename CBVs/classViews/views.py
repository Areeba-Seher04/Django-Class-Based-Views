from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from classViews.models import Author
from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView

#https://docs.djangoproject.com/en/2.2/ref/class-based-views/generic-display/
class AuthorList(ListView):
	''' A QUERYSET is necessary for ListView(otherwise error occured)
	** Queryset can be defined using 3 ways. (from 3 choose 1 which is appropiate for you)
			1. model = model name (result : queryset of all objects in a model in default order) same as modelname.objects.all()
			2. queryset = define a query here (here you can extract data from model as you want)
			3. override get_queryset() function (def get_querset(self):queryset = your query then return queryset)
	'''
	'''
	first check in parent method if template name is not define there (template_name = None),
	then it will use default template name which is app_name/modelname(_template_suffix).html
	** by default:    template_name = None
					  template_name_suffix = '_list'
	'''
	queryset = Author.objects.all()  #returns list of objects
	''' 
	CONTEXT_OBJECT_NAME : used in template ,context = {'context_object_name' : queryset}
	 ways
	 	1. context_object_name = the name which you want
	 	2. if context_object_name not defined then by default it is model_list , object_list
	 	'''

	''' CONTEXT
	get_context_data : a method that save the context of your view.
	 			You can override it to add more data which you want to show on web page
	 			by default:
	 				context = {
                'paginator': None,
                'page_obj': None,
                'is_paginated': False,
                'object_list': queryset
            }
	'''
	ordering = ['last_name'] #A string or list of strings (same as order_by()) , used in get_queryset method for ordering
	context_object_name = 'author'  #2 name , author , object_list
	template_name = 'classViews/author_list.html'
	#overriding get_context_data from django.views.generic.list to add new context in existing context dictionary
	def get_context_data(self,**kwargs):
		#get default context from django.views.generic.list
		context = super(AuthorList,self).get_context_data(**kwargs) #returns a dictionary of context
		#update it just like a dictionary
		# context['my_updated'] = Author.objects.get(first_name = 'Areeba')
		# context['error'] = 'ooopssssssssss ERRORRRRRRRRRR :('
		new_context_objects = {'my_updated':Author.objects.get(first_name = 'Areeba'),'error':'ERROR'}
		context.update(new_context_objects)
		return context 

	
	def post(self, request, *args, **kwargs):
		author = self.get_queryset()   #calling the queryset method
		print("authors",author)
		return render(request,'classViews/author_list.html',{'author':author})




class AuthorDetail(DetailView):
	''' URL
			**define a url dispatcher in urls.py , it will save pk or slug in  kwargs, kwargs = {'our dispatcherr':2} (pk or slug defined in library)
	QUERYSET:
			**returns a QUERYSET: either define a model , queryset or override get_queryset() or define a queryset in url (AuthorDetail.as_view(queryset=Author.objects.all())) (best: define a model only) 
			**then QUERYSET is filtered by pk stored in kwargs
			**then get an object from filtered queryset
	CONTEXT_OBJECT_NAME:
			** by default: model_name in small letters and object
			** define your own context_object_name , also access by object
	'''
	model = Author
	context_object_name = 'author_detail'

	'''
	CONTEXT : a dictionary
		** by default {}
		** if objects and context_name is defined: (objects: get() result from queryset) then
				context = {'object':objects,'our_defined context name':objects}
	'''
	# to add new context we can override get_context_data from django.views.generic.detail
	def get_context_data(self,**kwargs):  #addition of kwarg necessary because it is used by get method also to add new item by calling get_context_data
		context = super(AuthorDetail,self).get_context_data(**kwargs)  #returns a dictionary of context
		new_context_objects = {'error':'Errorrrrr Whyyyyyy :('}
		context.update(new_context_objects)
		print("myyyy",self.kwargs.get('pk'))  #print pk catch by url
		return context
	

class MyView(View):   #only 4 methods ,(setup,dispatch,http_method_not_allowed,option)
	def get(self,request,*args,**kwargs):
		return HttpResponse('Get method')
	def post(self,request,*args,**kwargs):
		return HttpResponse('post method')

class MyTemplateView(TemplateView):  #methods :setup,dispatch,http_method_not_allowed,get_context_data
	'''Renders a given template, with the context containing parameters captured in the URL'''
	template_name = 'classViews/MyTemplateView.html'
	#extra_context = 
	#override get_context_data
	def get_context_data(self,**kwargs):
		context = super(MyTemplateView,self).get_context_data(**kwargs) #initially context dict is only containing {'view',self} self is the info of class obj and id
		new_context_objects = {'my_context_object':"I am a template of My Template View inherited from TemplateView" , 'request':self.request}
		context.update(new_context_objects)
		return context

	def post(self,request,*args,**kwargs):
		#copied from get method.
		def get_context_data(self,**kwargs):
			context = super(MyTemplateView,self).get_context_data(**kwargs) #initially context dict is only containing {'view',self} self is the info of class obj and id
			new_context_objects = {'my_context_object':"I am a template of My Template View inherited from TemplateView" , 'request':self.request}
			context.update(new_context_objects)
			return context
		context = self.get_context_data(**kwargs)
		return self.render_to_response(context)
		#****************************OR********************************
		# return render(request, self.template_name, {'request':self.request})




