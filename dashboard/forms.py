from django import forms

from blogs.models import Blog, Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    def clean_category_name(self):
        name = self.cleaned_data['category_name']
        if Category.objects.filter(category_name__iexact=name).exists():
            raise forms.ValidationError("Sorry, this category already exists")
        return name
        
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ('author',)

        fields = ('title', 'category', "featured_image", "short_description", "blog_body", "status", "is_featured")
