from django.shortcuts import render

posts = [
    {
        'author': "C'est moi",
        'title': "Blog Post 1",
        'content': 'First post content',
        'date_posted': 'March 28, 2022'
    },
    {
        'author': "Still me",
        'title': "Blog Post 2",
        'content': 'Second post content',
        'date_posted': 'March 29, 2022'
    },
    {
        'author': "It's a me",
        'title': "Blog Post 3",
        'content': 'Third post content',
        'date_posted': 'March 32, 2022'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request=request, template_name='blog/home.html', context=context)


def about(request):
    return render(request=request, template_name='blog/about.html', context={'title': 'About'})
