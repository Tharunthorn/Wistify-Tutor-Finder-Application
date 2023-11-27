from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Article, ArticleSeries
from .decorators import user_is_superuser
from .forms import SeriesCreateForm, ArticleCreateForm, SeriesUpdateForm, ArticleUpdateForm, CommentForm


# Create your views here.


def homepage(request):
    matching_series = ArticleSeries.objects.all()

    return render(
        request=request,
        template_name='main/home.html',
        context={
            "objects": matching_series,
            "type": "series",
            "user": request.user
        })

def explore(request):
    matching_series = ArticleSeries.objects.all()

    subject_choices = [
        ('math', 'Math'),
        ('physics', 'Physics'),
        ('biology', 'Biology'),
        ('chemistry', 'Chemistry'),
        ('history', 'History'),
        ('computer_science', 'Computer Science'),
        ('literature', 'Literature'),
        ('geography', 'Geography'),
        ('economics', 'Economics'),
        ('psychology', 'Psychology'),
        ('political_science', 'Political Science'),
        ('engineering', 'Engineering'),
        ('art', 'Art'),
        ('music', 'Music'),
        ('languages', 'Languages'),
        ('physical_education', 'Physical Education'),
        ('environmental_science', 'Environmental Science'),
        ('sociology', 'Sociology'),
        ('philosophy', 'Philosophy'),
        ('astronomy', 'Astronomy'),
    ]

    return render(
        request=request,
        template_name='main/explore.html',
        context={
            "objects": matching_series,
            "type": "series",
            'subject_choices': subject_choices
        })


def series(request, series: str):
    matching_series = Article.objects.filter(series__slug=series).all()

    return render(
        request=request,
        template_name='main/home.html',
        context={
            "objects": matching_series,
            "type": "article"
        })

def article(request, series, article):
    matching_article = Article.objects.filter(series__slug=series, article_slug=article).first()

    if request.method == "POST":
        # Only process the comment form if the user is logged in
        if request.user.is_authenticated:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.article = matching_article
                comment.user = request.user  # Set the user for the comment
                comment.save()
                return redirect(request.path)  # Redirect back to the article page
        else:
            # Handle the case where a non-logged-in user tried to submit a comment
            messages.error(request, 'You must be logged in to leave a comment.')

    comment_form = CommentForm(user=request.user)
    user = request.user

    return render(request=request, template_name='main/article.html', context={
        "object": matching_article,
        "comment_form": comment_form,
        "user": user
    })

def new_series(request):
    if request.method == 'POST':
        form = SeriesCreateForm(request.POST, request.FILES, request=request)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = SeriesCreateForm(request=request)

    return render(
        request=request,
        template_name='main/new_record.html',
        context={
            "object": "Series",
            "form": form
        }
    )

def new_post(request):
    if request.method == "POST":
        form = ArticleCreateForm(request.user, request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(f"{form.cleaned_data['series'].slug}/{form.cleaned_data.get('article_slug')}")
    else:
        form = ArticleCreateForm(request.user)

    return render(
        request=request,
        template_name='main/new_record.html',
        context={
            "object": "Article",
            "form": form
        }
    )




def series_update(request, series):
    matching_series = ArticleSeries.objects.filter(slug=series).first()

    if request.method == "POST":
        form = SeriesUpdateForm(request.POST, request.FILES, instance=matching_series)
        if form.is_valid():
            form.save()
            return redirect('homepage')

    else:
        form = SeriesUpdateForm(instance=matching_series)

        return render(
            request=request,
            template_name='main/new_record.html',
            context={
                "object": "Series",
                "form": form
            }
        )

def series_delete(request, series):
    matching_series = ArticleSeries.objects.filter(slug=series).first()

    if request.method == "POST":
        matching_series.delete()
        return redirect('/')
    else:
        return render(
            request=request,
            template_name='main/confirm_delete.html',
            context={
                "object": matching_series,
                "type": "Series"
                }
            )

def article_update(request, series, article):
    matching_article = Article.objects.filter(series__slug=series, article_slug=article).first()

    if request.method == "POST":
        form = ArticleUpdateForm(request.POST, request.FILES, instance=matching_article)
        if form.is_valid():
            form.save()
            return redirect(f'/{matching_article.slug}')

    else:
        form = ArticleUpdateForm(instance=matching_article)

        return render(
            request=request,
            template_name='main/new_record.html',
            context={
                "object": "Article",
                "form": form
            }
        )

def article_delete(request, series, article):
    matching_article = Article.objects.filter(series__slug=series, article_slug=article).first()

    if request.method == "POST":
        matching_article.delete()
        return redirect('/')
    else:
        return render(
            request=request,
            template_name='main/confirm_delete.html',
            context={
                "object": matching_article,
                "type": "article"
                }
            )