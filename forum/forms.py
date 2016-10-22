from django import forms

from .models import Post


class PostForm(forms.ModelForm):

    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)

    def send_post(self):
        # send email using the self.cleaned_data dictionary
        pass