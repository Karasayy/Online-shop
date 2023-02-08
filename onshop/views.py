from django.shortcuts import render
from django.shortcuts import redirect
from .models import Product
from .forms import ProductForm
from .models import Rubric
from .forms import CommentsForm
from .models import Comments

from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.core.exceptions import ImproperlyConfigured
from django.db.models import Q
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin
from onshop.forms import UserRegistrationForm
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializers
from django.views.generic.edit import FormMixin


@api_view(['GET'])
def home(request):
    product = Product.objects.all()
    serializer = ProductSerializers(product, many=True)
    return Response(serializer.data)



def Main(request):
    return render(request, 'onshop/main.html')

def Contact(request):
    return render(request, 'onshop/contact.html')

def Shopping_cart(request):
    return render(request, 'onshop/shopping_cart.html')

def Checkout(request):
    return render(request, 'onshop/checkout.html')

def ProductList(request):
    items = Product.objects.all()
    rubrics = Rubric.objects.all()
    context = {
        'items':items,
        'rubrics':rubrics
    }
    return render(request, 'onshop/product_list.html', context)

class ProductDetail(DetailView, FormMixin):
    model = Product
    template_name = 'onshop/product_detail.html'
    form_class = CommentsForm
    context_object_name = 'item'
    success_url = reverse_lazy('product-list')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.product = self.get_object()
        self.object.save()
        return super().form_valid(form)


def rubric(request, rubric_id):
    product = Product.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {
        'product' : product,
        'rubrics': rubrics,
        'current_rubric': current_rubric
    }
    return render(request, 'onshop/rubric.html', context)


def post_create(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/products/')

    context = {'form': form}
    return render(request, 'post_create.html', context)


def post_update(request, pk):
    item = Product.objects.get(id=pk)
    form = ProductForm(instance=item)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/products/')

    context = {'form': form}
    return render(request, 'post_create.html', context)


def post_delete(request, pk):
    item = Product.objects.get(id=pk)
    item.delete()
    return redirect('/products/')


class Register(CreateView):
	template_name = 'registration/register.html'
	form_class = UserRegistrationForm
	success_url = reverse_lazy('register-success')

	def get_success_url(self):
		if not self.success_url:
			raise ImproperlyConfigured("NO url to redirect")
		return str(self.success_url)

	def form_valid(self, form):
		form.save()
		return HttpResponseRedirect(self.success_url)


#END REGISTRATION LABEL
@login_required(login_url=reverse_lazy('login'))
def product_req(request):
	submitted = False 
	if request.method == 'POST':
		form = ProductForm(request.POST, request.FILES)
		if form.is_valid():
			product = form.save(commit=False)
			try:
				product.username = request.user
			except Exception:
				pass
			product.save()
			return HttpResponseRedirect('/product?submitted=True')
	else:
		form = ProductForm()
		if 'submitted' in request.GET:
			submitted = True
	context = {
		'form' : form,
		'page_list' : Product.objects.all(),
		'submitted' : submitted
	}
	return render(request, '/main', context)


class SearchResultsView(ListView):
    model = Product
    template_name = 'onshop/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        return object_list


def CommentList(request):
    comment = Comments.objects.all()
    context = {
        'comment':comment
    }
    return f"{request},{context}"