from django.forms import ModelForm
from . models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'message'] #this is from our Comment Model class
        #fields = '__all__' #for this no need to typle all fields ourselves


