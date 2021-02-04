from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)
from django_currentuser.db.models import CurrentUserField
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import AutoSlugField 
from django.urls import reverse
from smart_selects.db_fields import ChainedForeignKey
from ckeditor.fields import RichTextField
from mptt.models import MPTTModel, TreeForeignKey


from django.conf import settings




class Thread(models.Model):
  title = models.CharField(max_length=100)
  author = CurrentUserField()
  category = models.ForeignKey('ThreadCategory', on_delete=models.SET_NULL, null=True)
  game = models.ForeignKey('ThreadGame', on_delete=models.SET_NULL, null=True)
  message = RichTextField()
  image = models.ImageField(upload_to='image/%Y/%m/%d/', blank=True, null=True)

  flagged = models.BooleanField(default=False)
  reason = models.TextField(blank=True, null=True)
  locked = models.BooleanField(blank=True, default=False)
  isStickied = models.BooleanField(default=False)

  views = models.IntegerField(blank=True, default=0)

  createdAt = models.DateTimeField(default=timezone.now)
  updatedAt = models.DateTimeField(auto_now=True)


  slug = AutoSlugField(populate_from=['id', 'title'], null=True, blank=True)


  def __str__(self):
    return self.title

  def save(self,  *args, **kwargs):
    super(Thread, self).save( *args, **kwargs)

  def get_absolute_url(self):
    return reverse('threads:threadDetail', args=[str(self.game),str(self.category),str(self.slug)])

    
  
  class Meta:
    db_table = 'threads'
    managed = True
    verbose_name = 'Thread'
    verbose_name_plural = 'Threads'

class ThreadCategory(models.Model):
  name = models.CharField(max_length=100)
  game = models.ForeignKey('ThreadGame', blank=True, null=True, related_name='category', on_delete=models.SET_NULL)
  image = models.ImageField(default='category-default.jpg',
                              upload_to='topics/category/img/%Y/%m/%d/')
  slug = models.SlugField(blank=True, null=True)
  
  createdAt = models.DateTimeField(default=timezone.now)
  updatedAt = models.DateTimeField(auto_now=True)


  def save(self, *args, **kwargs):
    if not self.slug and self.name :
      self.slug = slugify(self.name)
    super(ThreadCategory, self).save(*args, **kwargs)

  class Meta:
    verbose_name = 'Thread Category'
    verbose_name_plural = 'Thread Categories'

  def __str__(self):
    return self.name

class ThreadGame(models.Model):
  name = models.CharField(max_length=100)
  image = models.ImageField(default='category-default.jpg',
                              upload_to='topics/category/img/%Y/%m/%d/')
  slug = models.SlugField(blank=True, null=True)
  
  createdAt = models.DateTimeField(default=timezone.now)
  updatedAt = models.DateTimeField(auto_now=True)


  def save(self, *args, **kwargs):
    if not self.slug and self.name :
      self.slug = slugify(self.name)
    super(ThreadGame, self).save(*args, **kwargs)

  class Meta:
    verbose_name = 'Thread Game'
    verbose_name_plural = 'Thread Games'

  def __str__(self):
    return self.name


class ThreadComment(models.Model):
    
    author = CurrentUserField()
    comment = models.TextField(null=False, blank=False)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE,
                                related_name='comments')
    
    createdAt = models.DateTimeField(default=timezone.now)
    updatedAt = models.DateTimeField(auto_now=True)
    
    flagged = models.BooleanField(default=False)
    reason = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('-createdAt',)

    def __str__(self):
        return f"Comentário de {self.author.email} em {self.thread.title}"





