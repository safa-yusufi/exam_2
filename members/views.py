from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import BlogPost
from members.models import Product




def hello(request):
    return HttpResponse("Hello world!")



def blog_post_list(request):
    blog_posts = BlogPost.objects.all()
    template = loader.get_template('blog_post_list.html')
    return render(request, 'blog_post_list.html', {'blog_posts': blog_posts})
    



def get_all_products(request):
  mymembers = Product.objects.all().values()
  template = loader.get_template('products.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))


