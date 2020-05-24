from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'placeholder' : "제목을 입력하세요.",
            'style' : 'border:0px;'})
        self.fields['content'].widget.attrs.update({
            'style' : 'width:254px; height:335px; font-size:15pt; border:0px; resize:none;',
            'placeholder' : '내용을 입력하세요.',
            
        })
        
    class Meta:
        model = Post
        fields = ('title', 'content')
        title = forms.CharField(max_length=200)
        content = forms.TextInput()
        


        
            

        