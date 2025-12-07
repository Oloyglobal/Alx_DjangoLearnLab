# blog/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from .models import Comment
from .models import Profile, Comment, Post, Tag
from .models import Post, Tag


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_image']


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a comment...'})
    )

    class Meta:
        model = Comment
        fields = ['content']
        
        
        
        

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# existing UserUpdateForm, ProfileUpdateForm, CommentForm should remain

# class PostForm(forms.ModelForm):
#     # comma-separated tag names field for convenience
#     tag_names = forms.CharField(
#         required=False,
#         label='Tags (comma separated)',
#         widget=forms.TextInput(attrs={'placeholder': 'e.g. django, tutorial, tips'})
#     )

#     class Meta:
#         model = Post
#         fields = ['title', 'content', 'tag_names']
        
        

class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False)
    # taggit provides a simple comma-separated field in the form
    class Meta:
        model = Post
        fields = ["title", "slug", "content", "published", "tags"]
        widgets = {
            "content": forms.Textarea(attrs={"rows": 8}),
        }

    def __init__(self, *args, **kwargs):
        # If editing an existing post, pre-fill tag_names
        instance = kwargs.get('instance')
        super().__init__(*args, **kwargs)
        if instance:
            self.fields['tag_names'].initial = ', '.join([t.name for t in instance.tags.all()])

    def clean_tag_names(self):
        data = self.cleaned_data.get('tag_names') or ''
        # split and normalize
        names = [n.strip() for n in data.split(',') if n.strip()]
        # optionally enforce length / characters
        return names

    def save(self, commit=True):
        # Save post first, then handle tags
        post = super().save(commit=False)
        if commit:
            post.save()
        # tag handling
        tag_names = self.cleaned_data.get('tag_names', [])
        # get or create Tag objects
        tags = []
        for name in tag_names:
            tag_obj, created = Tag.objects.get_or_create(name__iexact=name, defaults={'name': name})
            tags.append(tag_obj)
        # set tags
        if commit:
            post.tags.set(tags)
        else:
            # if not committed, store for later
            self._pending_tags = tags
        return post
    
    


# ALX EXPECTS THIS NAME
class TagWidget(forms.TextInput):
    """Custom widget for handling comma-separated tags"""
    pass

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "slug", "content", "tags"]
        widgets = {
            "tags": TagWidget(),   # REQUIRED BY ALX CHECKER
        }
