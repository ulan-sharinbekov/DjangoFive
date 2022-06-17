from django.shortcuts import render, redirect
from .models import Category, Article

from .forms import CreateArticle
# Create your views here.

def get_list_categories(request):
    categories = Category.objects.all()
    print(categories)
    return render(request, 'comment-list.html', {"categories": categories})

def get_list_articles(request):
    articles = Article.objects.all()
    return render(request, 'article-list.html', {"articles": articles})

def get_article(request, pk):
    try:
        article = Article.objects.get(id=pk)
        article.view = article.view + 1
        print(article.author_id)
        article.save()
        return render(request, 'article.html', {"article": article})
    except:
        print("error")

    # return render(request, 'article-list.html', {"articles": articles})

def create_article(request):
    if request.method == "POST":
        form = CreateArticle(request.POST)
        if form.is_valid():
            try:
                # form = Article.objects.create(form.cleaned_data)
                form.save()
                return redirect('add_article')
            except:
                print(form)
                form.add_error(None, "Ошибка добавления")
    else:
        form = CreateArticle()

    return render(request, 'create-article.html', {"form": form})
