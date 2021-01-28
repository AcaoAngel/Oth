from django import forms
from .models import Post
from ckeditor.widgets import CKEditorWidget
from .models import *

class PostForm(forms.ModelForm):
	content = forms.CharField(widget=CKEditorWidget())


	class Meta():
		model = Post
		fields = ['title' , 'content', 'img' ]




