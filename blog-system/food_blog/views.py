from django.shortcuts import render, get_object_or_404, redirect
from food_blog.models import Post, Category, Comment
from .utils import calculate_reading_time
from .forms import CommentForm

# Create your views here.
def index(request):
    posts = Post.objects.select_related('author').all() # Retrieve all the information including the information of the author from the USER model.
    # Calculate reading time for each post and add it as an attribute
    for post in posts:
        post.reading_time = calculate_reading_time(post.body)

    return render(request, 'index.html', {
        'posts' : posts,
    })

def post(request, slug):
    # Get the post and calculate reading time
    post = get_object_or_404(Post, slug=slug)
    reading_time = calculate_reading_time(post.body)
    
    # Get comments
    comments = post.comments.order_by('-created_at')
    comment_count = comments.count()

    # Handle comment form
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()

    # Render template with all necessary context
    return render(request, 'post.html', {
        'post': post,
        'reading_time': reading_time,
        'comments': comments,
        'comment_count': comment_count,
        'form': form
    })

def category_posts(request, category):
    # Retrieve the category, or return 404 if not found
    category = get_object_or_404(Category, category=category)
    
    # Retrieve posts within the selected category
    posts = Post.objects.filter(category=category)

    for post in posts:
        post.reading_time = calculate_reading_time(post.body)

    return render(request, 'category_posts.html', {
        'category': category,
        'posts': posts,
    })

