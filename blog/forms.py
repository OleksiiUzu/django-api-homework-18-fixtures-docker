from django.forms import ModelForm
from blog import models


class FeedbackForm(ModelForm):
    class Meta:
        model = models.Feedback
        fields = ('title', 'text', 'media')

