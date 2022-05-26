from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from whatsonzambia.models import CustomUser
from django.forms import ModelForm
from .models import Post, PostFeature

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'venue', 'town', 'event_date', 'event_time', 'event_day', 'charge', 'content', 'post_image']


class PostFeatureCreateForm(ModelForm):
    class Meta:
        model = PostFeature
        fields = ['ft_title', 'ft_venue', 'ft_town', 'ft_event_date', 'ft_event_time', 'ft_event_day', 'ft_charge', 'ft_content', 'ft_post_image']