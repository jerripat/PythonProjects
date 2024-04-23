from django.shortcuts import render
from datetime import date
all_posts = [
    {
        "slug" : "my-first-post",
        "image": "me.jpeg",
        "author": "G Patterson",
        "date": date(2021, 1, 1),
        "title": "My First Post",
        "excerpt": "This is my first post. I am excited to share it with you all.",
        "content": """ Lorem ipsum dolor sit amet, consectetur adipisicing elit.
            Cum, distinctio hic incidunt mollitia officia quia tempora
            temporibus tenetur voluptate? Animi asperiores delectus deserunt
            dolorem doloremque ducimus eos neque quaerat quibusdam."""
    },
{
        "slug" : "my-second-post",
        "image": "spidy2.jpeg",
        "author": "G Patterson",
        "date": date(2021, 2, 1),
        "title": "My Second Post",
        "excerpt": "This is my second post. I am excited to share it with you all.",
        "content": """ Lorem ipsum dolor sit amet, consectetur adipisicing elit.
            Cum, distinctio hic incidunt mollitia officia quia tempora
            temporibus tenetur voluptate? Animi asperiores delectus deserunt
            dolorem doloremque ducimus eos neque quaerat quibusdam."""
    },
{
        "slug" : "my-third-post",
        "image": "computerNetworkg.jpeg",
        "author": "G Patterson",
        "date": date(2021, 3, 1),
        "title": "My Third Post",
        "excerpt": "This is my third post. I am excited to share it with you all.",
        "content": """ Lorem ipsum dolor sit amet, consectetur adipisicing elit.
            Cum, distinctio hic incidunt mollitia officia quia tempora
            temporibus tenetur voluptate? Animi asperiores delectus deserunt
            dolorem doloremque ducimus eos neque quaerat quibusdam."""
    }
]
def get_date(post):
    return post['date']
def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_post = sorted_posts[-3:]
    return render(request, 'blog/index.html', {'posts': latest_post})

def posts(request):
    return render(request, 'blog/all-posts.html',
                  { "all_posts": all_posts })

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html',{ "post": identified_post })