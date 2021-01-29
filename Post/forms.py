from django import forms
from .models import Post
from ckeditor.widgets import CKEditorWidget
from .models import *

class PostForm(forms.Form):
	user = forms.CharField(label='User', required=True, max_length=100)
	title = forms.CharField(label='Title', required=True, max_length=100)
	# content = forms.CharField(widget=CKEditorWidget())
	content = forms.CharField(label="Content")
	img = forms.ImageField(label="Image**")

	class Meta():
		model = Post
		fields = ['user', 'title' , 'content', 'img' ]




