from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Dealer, Vehicle, Post, Accesory, Lead

class DealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealer
        fields = ('id', 'name')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Post.objects.all()
    )

    class Meta:
        model = Vehicle
        fields = '__all__'

    def validate(self, data):
        for post in data['posts']:
            if not Post.objects.filter(pk=post.pk, dealer=data['dealer']):
                raise serializers.ValidationError(
                    "Post {} not with this dealer".format(post.pk)
                )
        return data

class AccesorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Accesory
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password', 'email')

class LeadSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Lead
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        return Lead.objects.create(user=user, **validated_data)