from django import forms
from models import Post

class AddTextPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text',)

class AddPhotoPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddPhotoPostForm,self).__init__(*args, **kwargs)
        self.fields['photo'].required = True

    class Meta:
        model = Post
        fields = ('photo', 'text',)