from django import forms
from .models import Comment
class commentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields=['description']
		# name = forms.CharField(required=False, max_length=100, help_text='100 characters max.')
		# email = forms.EmailField(required=True)
		# comment = forms.CharField(required=True, widget=forms.Textarea)

		# #fields = ('field',)
