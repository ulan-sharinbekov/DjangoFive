import traceback

from django.shortcuts import render, redirect
from .models import Comment
from article.models import Article
from .forms import CreateComment
# Create your views here.


def get_comments_of_article(request, pk):
    try:
        article = Article.objects.get(id=pk)
        comments = article.comment_set.all()

        return render(request, 'comment-list.html', {"comments": comments})
    except:
        pass

def create_comment(request, pk):
    if request.method == "POST":
        form = CreateComment(request.POST)
        if form.is_valid():
            print("VALID")
            try:
                # form = Article.objects.create(form.cleaned_data)
                article = Article.objects.get(id=pk)
                # form.cleaned_data['article_id'] = article
                form.instance.article_id = article
                # print(form.cleaned_data)
                # print(type(form.cleaned_data))
                form.save()
                # return redirect('add_comment')
            except Exception:
                # print(form.cleaned_data)

                traceback.print_exc()
                # print(form)
                form.add_error(None, "Ошибка добавления")
    else:
        form = CreateComment()

    return render(request, 'create-comment.html', {"form": form, "pk": pk})
