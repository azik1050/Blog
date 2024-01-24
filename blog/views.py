from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView
from .models import Post, PostComment, PostCategory
from .forms import PostCommentForm, PostForm
from django.contrib import messages


class PostList(ListView):
    model = Post
    template_name = 'blog/index_main.html'
    paginate_by = 6
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for post in context['posts']:
            post.comment_count = PostComment.objects.filter(post=post).count()

        return context

    def get_queryset(self):
        return Post.objects.filter(published=True).order_by('-updated_at')


class PostListByCategory(ListView):
    model = Post
    template_name = 'blog/post_by_category.html'
    paginate_by = 6
    context_object_name = 'posts'

    def get_queryset(self):
        category = get_object_or_404(PostCategory, slug=self.kwargs.get('slug'))
        return Post.objects.filter(category=category).order_by('-updated_at')


class CreatePost(CreateView):
    model = Post
    form_class = PostForm
    success_url = '/'
    template_name = 'blog/post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Your post has been added!')
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, error in form.errors.items():
            messages.warning(self.request, f'{field} - {error}')
        return super().form_invalid(form)


class PostUpdate(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_create.html'

    def form_valid(self, form):
        messages.success(self.request, 'Your post has been updated!')
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, error in form.errors.items():
            messages.warning(self.request, f'{field} - {error}')
        return super().form_invalid(form)


class UserPostList(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 6
    template_name = 'blog/index_main.html'

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user).order_by('-updated_at')


def index_post(req, slug):
    post = get_object_or_404(Post, slug=slug)
    if req.method == 'POST':
        form = PostCommentForm(req.POST)
        if form.is_valid():
            form.instance.author = req.user
            form.instance.post = post
            form.save()
            return redirect('main_post', slug)
        else:
            messages.info(req, 'JK')
    else:
        form = PostCommentForm()
    context = {
        'post': post,
        'comments': PostComment.objects.filter(post=post),
        'form': form,
        'categories': PostCategory.objects.order_by('-created_at'),
        'posts': Post.objects.filter(category__in=post.category.all()).order_by('-updated_at').exclude(id=post.id).distinct()[:3]
    }
    return render(req, 'blog/index_post.html', context)
