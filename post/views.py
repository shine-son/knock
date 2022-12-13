from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from .models import Post
from .serializers import GenericPostSerializer
class GenericPostModelViewSet(ModelViewSet):
    
    queryset = Post.objects.all()
    serializer_class = GenericPostSerializer
    
    @action(detail=False, methods=['GET'])
    def public(self, request):
        '''
        is_public 필드값이 True인 글들만 리스트 합니다.
        '''
        qs = self.queryset.filter(is_public=True)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        '''
        해당 유저정보를 form, json을 통하지 않고 request 통해 저장
        '''
        serializer.save(author=self.request.user)
