from django.views.generic import TemplateView, ListView
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import FormView
from products.forms import LoginForm
from products.utils import render_to_json_response
from products.models import Product, Category
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from django.utils import timezone


class IndexView(TemplateView):
    template_name = 'products/index.html'


class CategoryView(ListView):
    template_name = 'products/categories.html'

    def get_queryset(self):
        """Return the last five published questions."""
        return Category.objects.all()


class CategoryDetailView(DetailView):
    template_name = 'products/category.html'
    model = Category

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        categ = get_object_or_404(Category, slug__iexact=self.kwargs['slug'])
        context['products'] = Product.objects.all().filter(category=categ)
        context['slug'] = self.kwargs['slug']
        return context


class ProductView(DetailView):
    template_name = 'products/product.html'
    model = Product

    def get_object(self):
        return get_object_or_404(Product, slug__iexact=self.kwargs['pslug'])


class LastProductsView(ListView):
    template_name = 'products/last.html'
    model = Product

    def get_queryset(self):
        current_time = timezone.now()
        day_ago = current_time - timezone.timedelta(hours=24)
        return Product.objects.filter(created_at__gt=day_ago)


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'registration/login.html'

    def form_valid(self, form):
        context = form.cleaned_data
        user = authenticate(
            username=context['username'], password=context['password'])
        context['login'] = True
        del context['password']
        if user is not None:
            if user.is_active:
                login(self.request, user)
                if not self.request.user.is_authenticated():
                    context = {'errors': 'Invalid user or password!'}
                    context['login'] = False
            else:
                context['login'] = False
                context = {'errors': 'Invalid user or password!'}
        else:
            context['login'] = False
            context = {'errors': 'Invalid user or password!'}
        return render_to_json_response(context, status=200)

    def form_invalid(self, form):
        context = {'errors': str(form.errors)}
        context['login'] = False
        if self.request.is_ajax():
            return render_to_json_response(context, status=200)


class LogoutView(TemplateView):
    template_name = 'registration/logged_out.html'

    def get_context_data(self, **kwargs):
        context = super(LogoutView, self).get_context_data(**kwargs)
        logout(self.request)
        return context
