from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from blog.errors import NoBlogFound
from .models import Blog
from .forms import CommentForm


# Create your views here.

# def home(request):
#     return render(request, 'home.html') #in render first parameter is request,
#     second is our htmlpage(template). here we have created templates folder inside our app


# def home(request):
#     #print(type(request)) #output: "GET /home HTTP/1.1" 200 15
#     #raise IOError #prints 500 error in our terminal. Output: "GET /home HTTP/1.1" 500 72620
#
#     a = {'name': 'Hari', 'roll': '15'}
#     #print(a['address']) #prints: keyerror
#     print(a.get('address')) # prints: none therefore more useful than previous line
#     print(a.get('address', 'california')) #here we are providing default value of address, if there is no address
#     try: #that code that returns exception must be inside try block
#         blogs = Blog.fetch_all()#since fetch_all() is static we don't need to create instance of it for calling it
#         #blogs = Blog().fetch_all() #this is calling fetch_all instance method. first creating object as Blog()
#         return HttpResponse("There are %d blogs" % (len(blogs)))
#
#     #except: this catches all exception
#     except NoBlogFound: #this catches only NoBlogFound exception
#         return HttpResponse("Sorry, No blogs are available currently.")
#
#     # except ValueError: #here we are chaining different catching mechanisms for different error
#     #     return HttpResponse("coding is....")
#
#
#     #IOError: file not found error

def home(request):
    blog_list = Blog.objects.order_by('-pub_date').all()  # here - means descending order
    paginator = Paginator(blog_list,
                          2)  # Show 2 blogs per page. Give Paginator a list of objects, plus the number of items you’d like to have on each page, and it gives you methods for accessing the items for each page:
    print(
        request.GET)  # when we go http://127.0.0.1:8000/home/?page=10 in browser it prints <QueryDict: {'page': ['10']}> in terminal. in browser after ? is query string eg ?q=hari here q = key and hari is value, & denotes another query. in get we send data to server through query string.
    page = request.GET.get('page',
                           '1')  # here .get('page') here page is key(of querystring that we provide ourself or by clicking page button or next that has key as 'page') and .get doesn't throw key error if it doesnt find key. here 1 is default value i.e page 1. note page starts from page 1
    blogs = paginator.get_page(page)  # here get_page() is method of Paginator class
    popular_posts = Blog.objects.order_by('-pub_date')[:5]

    print(
        request.POST)  # this code is takes our submitted form, it prints what we submit in form form browser in terminal
    if request.method == 'POST':  # this code is takes our submitted form
        form = CommentForm(request.POST)  # this code is takes our submitted form
        if form.is_valid():
            comment = form.save(commit=False)  # if we make commit=True it will directly save to database
            comment.blog = Blog.objects.get(pk=request.POST.get('blog_id'))
            comment.save()

            return redirect('/home')

    else:
        form = CommentForm()

    context = {
        'blogs': blogs,  # key: value where key is used in html page and value is in previous line
        'popular_posts': popular_posts,
        'form': form
    }
    # return render(request, 'home.html', context)
    return render(request, 'new_layout.html', context)
