from django.shortcuts import render


# webpackが生成したhtmlをそのままテンプレートとして読み込まれる
def index(request):
    return render(request, 'index.html', {})
