from django import forms
from .models import Post, Comment, Category


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = ('title', 'body')
        exclude = ('user', 'slug', 'updated', 'created')


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user', 'slug', 'updated', 'created')


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={'class':'form-control'})
        }
        error_messages = {
            'body': {
                'required': 'این فیلد اجباری است',
            }
        }
        help_texts = {
            'body': 'max 400 char'
        }


class AddReplyForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title',)


class EditCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title',)