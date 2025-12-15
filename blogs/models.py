from django.db import models
from django.contrib.auth import get_user_model  # i used this because it can be used for custom user too
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower


# Create your models here.
# creating category model 
class Category(models.Model):
    category_name = models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('category_name'),
                name='unique_category_name_ci'
            )
        ]
        verbose_name = 'categories'

    def __str__(self):
        return self.category_name
    



#models for blog
User = get_user_model()

STATUS_CHOICES = (
    ("Draft",'Draft'),
    ("Published",'Published'),
)
class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d')
    short_description = models.TextField(max_length=500)
    blog_body = models.TextField(max_length=2000)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default="Draft")
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         base_slug = slugify(self.title)
    #         slug = base_slug
    #         counter = 1
    #         # Ensure uniqueness
    #         while Blog.objects.filter(slug=slug).exists():
    #             slug = f"{base_slug}-{counter}"
    #             counter += 1
    #         self.slug = slug
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.title

