from django.forms import ModelForm

from .models import Post
from .models import PostAttachment

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('body', 'is_private')


class AttachmentForm(ModelForm):
    class Meta:
        model = PostAttachment
        fields = ('image',)