from django.db import models
from django.contrib.auth.models import User,AbstractUser,Group,Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from .fields import OrderField
from django.template.loader import render_to_string


# Create your models here.
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')], null=True, blank=True)
    
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Ensure this name is unique
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='customuser',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # Ensure this name is unique
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='customuser',
    )


class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug=models.SlugField(max_length=200,unique=True)

    class Meta:
        ordering=['title']

    def __str__(self):
        return self.title
    

class Course(models.Model):
    owner=models.ForeignKey(User,
                            related_name='courses_created',
                            on_delete=models.CASCADE)
    students=models.ManyToManyField(User,related_name='courses_joined',
                                    blank=True)
    subjects=models.ForeignKey(Subject,
                              related_name='courses',
                              on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200,unique=True)
    overview = models.TextField()
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
    
class Modules(models.Model):
    course=models.ForeignKey(Course,
                             related_name='modules',
                             on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    description=models.TextField(blank=True)
    order=OrderField(blank=True,for_fields=['course'])

    class Meta:
        ordering=['order']

    def __str__(self):
        return f'{self.order}.{self.title}'
    

class Content(models.Model):
    module=models.ForeignKey(Modules,
                             related_name='contents',
                             on_delete=models.CASCADE)
    content_type=models.ForeignKey(ContentType,
                                   on_delete=models.CASCADE,
                                   limit_choices_to={'models_in':(
                                       'text',
                                       'video',
                                       'image',
                                       'file'
                                   )})
    order=OrderField(blank=True,for_fields=['module'])
    
                                                     
                                   
    object_id=models.PositiveIntegerField()
    item=GenericForeignKey('content_type','object_id')

    class Meta:
        ordering=['order']


class ItemBase(models.Model):
    owner=models.ForeignKey(User,
                            related_name='%(class)s_related',
                            on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title
    

    def render(self):
        return render_to_string(
            f'courses/content/{self._meta.model_name}.html',
            {'item': self})
    
class Text(ItemBase):
    content=models.TextField()


class File(ItemBase):
    file=models.FileField(upload_to='files')

class Image(ItemBase):
    file=models.FileField(upload_to='images')

class Video(ItemBase):
    url=models.URLField()
    
