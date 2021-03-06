from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rango.models import Category, ContactUs, Page, Review, User,UserProfile
from rango.forms import CategoryForm, ContactUsForm, PageForm, UserForm, UserProfileForm, ReviewForm
from datetime import datetime
from django.db.models import Count


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]

    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['pages'] = page_list
    context_dict['extra'] = 'From the model solution on GitHub'
    
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']

    return render(request, 'rango/about.html', context=context_dict)

def the_fast_and_the_furious(request):
    
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']

    return render(request, 'rango/the_fast_and_the_furious.html', context=context_dict)

def the_expendables(request):
    
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']

    return render(request, 'rango/the_expendables.html', context=context_dict)

def deadpool(request):
    
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']

    return render(request, 'rango/deadpool.html', context=context_dict)

def hangover(request):
    
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']

    return render(request, 'rango/hangover.html', context=context_dict)

def home_alone(request):
    
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']

    return render(request, 'rango/home_alone.html', context=context_dict)

def minions(request):
    
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']

    return render(request, 'rango/minions.html', context=context_dict)

def coco(request):
    
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']

    return render(request, 'rango/coco.html', context=context_dict)

def titanic(request):
    
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']

    return render(request, 'rango/titanic.html', context=context_dict)

def black_panther(request):
    
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']

    return render(request, 'rango/black_panther.html', context=context_dict)

def transformers(request):
    
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']

    return render(request, 'rango/transformers.html', context=context_dict)

def back_to_the_future(request):
    
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']

    return render(request, 'rango/back_to_the_future.html', context=context_dict)

def statistics(request):

    user_count = User.objects.count()
    film_count = Page.objects.count()
    list1=[]
    list2=[]
    categories = Page.objects.filter().order_by('category').values('category__name').annotate(count=Count('category__name'))
    for i in categories:
        list1.append(str(i.get('category__name')))
        list2.append(i.get('count'))
   

    context_dict = {'user_count' : user_count,
                    'film_count' : film_count,
                    'list1' :list1 ,
                    'list2' : list2,
                    }
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']

    return render(request, 'rango/statistics.html', context=context_dict)

def contact_us(request):
    form = ContactUsForm()

    if request.method == 'POST':
        form = ContactUsForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse('rango:index'))
        else:
            print(form.errors)
    
    return render(request, 'rango/contact_us.html', {'form': form})


def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['pages'] = None
        context_dict['category'] = None
    
    return render(request, 'rango/category.html', context=context_dict)

@login_required
def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse('rango:index'))
        else:
            print(form.errors)
    
    return render(request, 'rango/add_category.html', {'form': form})

@login_required
def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except:
        category = None
    
    # You cannot add a page to a Category that does not exist... DM
    if category is None:
        return redirect(reverse('rango:index'))

    form = PageForm()

    if request.method == 'POST':
        form = PageForm(request.POST)

        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()

                return redirect(reverse('rango:show_category', kwargs={'category_name_slug': category_name_slug}))
        else:
            print(form.errors)  # This could be better done; for the purposes of TwD, this is fine. DM.
    
    context_dict = {'form': form, 'category': category}
    return render(request, 'rango/add_page.html', context=context_dict)

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    
    return render(request, 'rango/register.html', context={'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('rango:index'))
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'rango/login.html')

@login_required
def restricted(request):
    return render(request, 'rango/restricted.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('rango:index'))

def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')

    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_visit'] = last_visit_cookie
    
    request.session['visits'] = visits

@login_required
def user_profile(request):
    registered = False
    current_user =  request.user
    current_user_id = request.user.id
    current_user_username = current_user.username
    user = User.objects.get(username = current_user_username)
    try:
        userprofile = UserProfile.objects.get(user = user)
    except:
        UserProfile.objects.create(user=user, phone = '')
        userprofile = UserProfile.objects.get(user = user)
    user_form = UserForm(request.POST or None, instance = user)

    profile_form = UserProfileForm(request.POST or None, instance=userprofile)


    if user_form.is_valid() and profile_form.is_valid():
        current_user =  request.user
        #current_user.delete()
        
        user = user_form.save()
        user.set_password(user.password)
        user.save()

        profile = profile_form.save(commit=False)
        profile.user = user

        if 'picture' in request.FILES:
            profile.picture = request.FILES['picture']
            
        profile.save()
        registered = True
        return redirect('rango:index')
    else:
        print(user_form.errors, profile_form.errors)
    
    
    return render(request, 'rango/profile.html', context={'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def delete_user(request):
    current_user =  request.user
    current_user.delete()
    return redirect('rango:index')

def all_contactus(request):
    contactuslist = ContactUs.objects.all()
    current_user = request.user
    current_user_id = current_user.id

    return render(request,'rango/contact_us_list.html',
    {'contactuslist' : contactuslist , 'current_user':current_user_id} )



def add_review(request):
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse('rango:index'))
        else:
            print(form.errors)
    
    return render(request, 'rango/add_review.html', {'form': form})



def all_reviews(request):
    
    review_list = Review.objects.all()
  

    return render(request,'rango/review_list.html',
    {'review_list' : review_list  } )
