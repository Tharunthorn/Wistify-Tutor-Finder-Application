from django import forms
from .models import Article, ArticleSeries, Comment

class SeriesCreateForm(forms.ModelForm):
    SUBJECT_CHOICES = [
        ('math', 'Math'),
        ('physics', 'Physics'),
        ('biology', 'Biology'),
        ('chemistry', 'Chemistry'),
        ('history', 'History'),
        ('computer_science', 'Computer Science'),
        ('literature', 'Literature'),
        ('geography', 'Geography'),
        ('economics', 'Economics'),
        ('psychology', 'Psychology'),
        ('political_science', 'Political Science'),
        ('engineering', 'Engineering'),
        ('art', 'Art'),
        ('music', 'Music'),
        ('languages', 'Languages'),
        ('physical_education', 'Physical Education'),
        ('environmental_science', 'Environmental Science'),
        ('sociology', 'Sociology'),
        ('philosophy', 'Philosophy'),
        ('astronomy', 'Astronomy'),
    ]

    subjects = forms.MultipleChoiceField(
        choices=SUBJECT_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    class Meta:
        model = ArticleSeries
        fields = [
            "title",
            "subtitle",
            "slug",
            "subjects",
            "image",
        ]

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.request:
            instance.author = self.request.user

        # Convert selected subjects to a space-separated string
        instance.subjects = ' '.join(self.cleaned_data.get('subjects', []))

        if commit:
            instance.save()
        return instance

# forms.py
class ArticleCreateForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.fields['series'].queryset = ArticleSeries.objects.filter(author=user)

    class Meta:
        model = Article
        fields = [
            "title",
            "subtitle",
            "article_slug",
            "content",
            "notes",
            "series",
            "image",
        ]

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.author = self.user
        if commit:
            instance.save()
        return instance


class SeriesUpdateForm(forms.ModelForm):
    class Meta:
        model = ArticleSeries

        fields = [
            "title",
            "subtitle",
            "image",
            "subjects"
        ]

class ArticleUpdateForm(forms.ModelForm):
    class Meta:
        model = Article

        fields = [
            "title",
            "subtitle",
            "content",
            "notes",
            "series",
            "image",
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'rating']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        # Remove the 'user' field for non-authenticated users
        if not (user and user.is_authenticated):
            self.fields.pop('user', None)

        # If the user is authenticated, set the initial value and hide the 'user' field
        elif 'user' in self.fields:
            self.fields['user'].initial = user
            self.fields['user'].widget = forms.HiddenInput()