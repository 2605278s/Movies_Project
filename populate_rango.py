import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page



def populate():
    action_films = [
        {'title':'The Fast and the Furious',
         'url': 'http://127.0.0.1:8000/rango/the_fast_and_the_furious/',
         'views': 76,
        },
        {'title':'The Expendables',
        'url': 'http://127.0.0.1:8000/rango/the_expendables/',
         'views': 60,}
        ]
    comedy_films = [
        {'title':'Deadpool',
        'url': 'https://www.youtube.com/watch?v=ONHBaC-pfsk',
         'views': 118,
        },
        {'title':'Hangover',
        'url': 'https://www.youtube.com/watch?v=tcdUhdOlz9M',
         'views': 91,}, 

        {'title':'Home Alone',
        'url': 'https://www.youtube.com/watch?v=jEDaVHmw7r4',
         'views': 5000,} ]
    
    sciencefiction_films = [
        {'title':'Transformers',
        'url': 'https://www.youtube.com/watch?v=dxQxgAfNzyE',
        'views': 27,},

        {'title': 'Back to the Future',
        'url': 'https://www.youtube.com/watch?v=qvsgGtivCgs',
         'views': 60,} ]

    animation_films = [
        {'title':'Minions',
        'url': 'https://www.youtube.com/watch?v=eisKxhjBnZ0',
         'views': 2000,},
         {'title':'Coco',
         'url': 'https://www.youtube.com/watch?v=Rvr68u6k5sI',
         'views': 3500,}
    ]

    drama_films = [
        {'title':'Titanic',
        'url': 'https://www.youtube.com/watch?v=jUm88F3MEbQ',
         'views': 20200,
        },
        {'title':'Black Panther',
        'url': 'https://www.youtube.com/watch?v=xjDjIWPwcPU',
         'views': 200,}
    ]
    
    cats = {'Action': {'pages': action_films, 'views': 128, 'likes': 64},
            'Comedy': {'pages': comedy_films, 'views': 64, 'likes': 32},
            'Science Fiction': {'pages': sciencefiction_films, 'views': 32, 'likes': 16},
            'Animation': {'pages': animation_films, 'views': 64, 'likes': 32},
            'Drama': {'pages': drama_films, 'views': 64, 'likes': 32},}

    for cat, cat_data in cats.items():
        c = add_cat(cat, views=cat_data['views'], likes=cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], views=p['views'])
    
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c

# Start execution here!
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
    