from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status



# webpackが生成したhtmlをそのままテンプレートとして読み込まれる
def index(request):
    return render(request, 'index.html', {})


class PingViewSet(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        return Response(data={'username': request.user.stu_num}, status=status.HTTP_200_OK)
