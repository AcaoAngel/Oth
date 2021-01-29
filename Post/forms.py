from django import forms
from .models import Post
from ckeditor.widgets import CKEditorWidget
from .models import *

# class PostForm(forms.ModelForm):
class PostForm(forms.Form):
	content = forms.CharField(widget=CKEditorWidget())
	img = forms.ImageField(label="Image**")
	user = forms.CharField(label='User', required=True, max_length=100)
	title = forms.CharField(label='User', required=True, max_length=100)

	class Meta():
		model = Post
		fields = ['title' , 'content', 'img' ]




