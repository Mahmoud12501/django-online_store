from django.shortcuts import render ,redirect
from django.urls import reverse
from .models import blog
from django.core.paginator import Paginator
from .forms import ReviewForm,BlogForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def all_Blogs(request):

    blog_list=blog.objects.all()
    paginator = Paginator(blog_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    contxt={'blogs':page_obj}
    return render(request,"blog/blog_list.html",contxt)
    
def blog_Detail(request,slug):
    blog_d=blog.objects.get(slug=slug)
    
    if request.method=='POST':
         form= ReviewForm(request.POST)
         if form.is_valid:
             myform=form.save(commit=False)
             myform.blog_r=blog_d
             myform.save()
    else:
        form= ReviewForm()
    contxt={'detail':blog_d,'form':form}
    return render(request,"blog/blog_detail.html",contxt)




@login_required
def Add_Blog(request):

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid:
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('blog:blog'))
    else:
        form = BlogForm()
    return render(request, 'blog/add_blog.html', {"form": form})
