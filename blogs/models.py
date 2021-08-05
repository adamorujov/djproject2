from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.utils import timezone
# Create your models here.

class CategoryModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='Kateqoriya')

    class Meta():
        db_table = 'Categories'
        verbose_name = 'Kateqoriya'
        verbose_name_plural = 'Kateqoriyalar'

    def __str__(self):
        return self.name

class BlogModel(models.Model):
    image = models.ImageField(upload_to='blog_images', verbose_name='Bloq başlıq şəkli', default='blog_images/default_blog_img.png')
    title = models.CharField(max_length=250, verbose_name='Bloq başlığı', default="")
    context = RichTextField(verbose_name='Bloq məzmunu', default="")
    pub_date = models.DateTimeField(auto_now_add=True, editable=True)
    views_time = models.PositiveBigIntegerField(default=0, verbose_name='Baxış sayı')
    comment_number = models.PositiveBigIntegerField(default=0, editable=False ,verbose_name='Rəy sayı')
    like_number = models.PositiveBigIntegerField(default=0, verbose_name='Bəyənmə sayı')
    slug = AutoSlugField(populate_from='title', unique=True, default="")
    categories = models.ManyToManyField(CategoryModel, related_name='blogs', verbose_name='Kateqoriyalar')

    class Meta():
        db_table = 'Blogs'
        verbose_name = 'Bloq'
        verbose_name_plural = 'Bloqlar'

    def __str__(self):
        return self.title


class CommentModel(models.Model):
    comment = models.TextField(verbose_name='Rəy')
    writer = models.CharField(max_length=100, verbose_name='Yazan', default="")
    pub_date = models.DateTimeField(auto_now_add=True, editable=True)
    blog = models.ForeignKey(BlogModel, related_name='comments', on_delete=models.CASCADE, verbose_name='Bloq')
    parent = models.ForeignKey('self', related_name='replies', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Əsas rəy')

    class Meta():
        db_table = 'Comments'
        verbose_name = 'Rəy'
        verbose_name_plural = 'Rəylər'

    def __str__(self):
        return self.comment