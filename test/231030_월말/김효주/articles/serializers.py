from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title',)


class CommentSerializer(serializers.ModelSerializer):

    class ArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title','id',)

    article = ArticleSerializer(read_only=True)    

    class Meta:
        model = Comment
        fields = '__all__'
        # read_only_fields = ('article',)


class ArticleSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True, read_only=True)
    comments_count = serializers.IntegerField(source='comments.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'