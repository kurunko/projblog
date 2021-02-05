# Core Django imports.
from django.db.models.fields import BooleanField
from django.forms import ModelForm, TextInput, EmailInput, Textarea, FileInput,Select
from django import forms
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget



# Blog application imports.
from .models import Thread, ThreadCategory, ThreadComment
from accounts.models import CustomUser


class ThreadCreateForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=ThreadCategory.objects.all(),
                                      empty_label="Select Category",
                                      widget=forms.Select(attrs=
                                                          {
                                                              "class": "form-control selectpicker",
                                                              "type": "text",
                                                              "name": "thread-category",
                                                              "id": "threadCategory",
                                                              "data-live-search": "true"
                                                          }
                                      )
                                    )


    class Meta:

        # Article status constants
        MASCULINO = "MASCULINO"
        FEMININO = "FEMININO"
        OUTROS = "OUTROS"

        # CHOICES
        GENDER_CHOICES = (
            (MASCULINO, 'Masculino'),
            (FEMININO, 'Feminino'),
            (OUTROS, 'Outros'),
        )

        model = Thread
        fields = [
            "title",
            "category", 
            "game", 
            "image", 
            "message", 
        ]
        widgets = {
            'title': TextInput(attrs={
                                     'name': "thread-title",
                                     'class': "form-control",
                                     'placeholder': "Enter Thread Title",
                                     'id': "threadTitle"
                                     }),
            'image': FileInput(attrs={
                                        "class": "form-control clearablefileinput",
                                        "type": "file",
                                        "id": "articleImage",
                                        "name": "thread-image"
                                      }

                               ),

            'body': forms.CharField(widget=CKEditorWidget(config_name="default", attrs={
                       "rows": 5, "cols": 20,
                       'id': 'content',
                       'name': "article_content",
                       'class': "form-control",
                       })),

            'tags': TextInput(attrs={
                                     'name': "tags",
                                     'class': "form-control",
                                     'placeholder': "Example: sports, game, politics",
                                     'id': "tags",
                                     'data-role': "tagsinput"
                                     }),

            'status': Select(choices=GENDER_CHOICES,
                             attrs=
                             {
                                 "class": "form-control selectpicker",
                                 "name": "status", "type": "text",
                                 "id": "articleStatus",
                                 "data-live-search": "true",
                                 "title": "Select Status"
                             }
                             ),
        }

class ThreadModerateForm(forms.ModelForm):

    class Meta:

        model = Thread
        fields = [
            "isStickied",
            "locked", 
            "flagged", 
            "reason", 
        ]
        labels  = {
            "isStickied": "Em Destaque?",
            "locked": "Está Fechado?", 
            "flagged": "É Spam?", 
            "reason":"Motivo", 
        }




class ThreadCommentForm(ModelForm):
    class Meta:
        model = ThreadComment
        fields = ['comment', ]
        widgets = {
            'comment': Textarea(attrs={'name': "contact-form-message",
                                       'rows': "2",
                                       'class': "text-area-messge form-control",
                                       'placeholder': "Insira seu comentário",
                                       'aria - required': "true",
                                       'aria - invalid': "false"
                                       }),
        }



class UserUpdateForm(forms.ModelForm):
    """
        Creates form for user to update their account.
    """
    email = forms.EmailField(widget=
                             forms.EmailInput(attrs={
                                                     'name': "email",
                                                     'id': "email",
                                                     'class': "form-control",
                                                    }
                                              ),
                             )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
        widgets = {

            'first_name': forms.TextInput(attrs={
                'name': "first-name",
                'class': "form-control",
                'id': "first-name"
            }),

            'last_name': forms.TextInput(attrs={
                'name': "last-name",
                'class': "form-control",
                'id': "last-name"
            }),

            'username': forms.TextInput(attrs={
                'name': "username",
                'class': "form-control",
                'id': "username"
            }),
        }

