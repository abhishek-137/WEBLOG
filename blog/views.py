from django.shortcuts import get_object_or_404, render
from .models import Post,Author,Tag

about={
    "Auth_name":"Abhishek's Blog",

    "Introduction":"Hi, I am Abhishek and I love to blog about tech and the world!",
   
    "Description": """
    I love programming, I love to help others and I enjoy exploring new
    technologies in general!

        My goal is to keep on growing as a developer - and if I could help you do
    the same, I'd be very happy!
    """
}


posts=Post.objects.all()

def starting_page(request):
    latest_posts=posts.order_by("-post_date")
    latest_posts=posts[:3]
    
    return render(request, "blog/index.html",{"posts":latest_posts,"about":about})

def all_posts(request):
    return render(request, "blog/all_posts.html",{"posts":posts})

def post_detail(request, slug): 
    
    identified_post=get_object_or_404(Post,slug=slug)
    return render(request, "blog/post-detail.html", {"post": identified_post,"tags" :identified_post.tags.all()
    })
    