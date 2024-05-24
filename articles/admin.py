from django.contrib import admin

# Register your models here.
from .models import Article
from .models import Comment


#class CommentInline(admin.StackedInline):
class CommentInline(admin.TabularInline):
    model =  Comment
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
