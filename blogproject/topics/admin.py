from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .models import Thread, ThreadCategory, ThreadGame, ThreadComment
from .forms import ThreadCreateForm


class ThreadAdmin(admin.ModelAdmin):
    pass


class ThreadCategoryAdmin(admin.ModelAdmin):
    pass
class ThreadGameAdmin(admin.ModelAdmin):
    pass


class ThreadCommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Thread, ThreadAdmin)
admin.site.register(ThreadCategory, ThreadCategoryAdmin)
admin.site.register(ThreadGame, ThreadGameAdmin)
admin.site.register(ThreadComment, ThreadCommentAdmin)

