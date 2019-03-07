from django.contrib import admin
from .models import Post, Article

# 방식1
# admin.site.register(Post)

# 방식2
# class PostAdmin(admin.ModelAdmin):
#     list_display = ['user','title','content', 'content_size5', 'created_at','updated_at']

#     # 여기서 컬럼을 추가하기도 한다 (컬럼 추가 가능)
#     def content_size5(self, Post):
#         return '{}'.format(Post.content[:5])
#     content_size5.short_description = '일부 내용'

#     def content_len(self, Post):
#         return '{}글자'.format(len(Post.content))
#     content_len.short_description = '글자수'

# admin.site.register(Post, PostAdmin)

# 방식3 장식자 
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user','title','content', 'content_size5', 'created_at','updated_at']
    list_display_link = ['user','title']
    fields = ['title','content']
    list_filter = ['title']
    search_fields = ['title', 'content']
    

    # 여기서 컬럼을 추가하기도 한다 (컬럼 추가 가능)
    def content_size5(self, Post):
        return '{}'.format(Post.content[:5])
    content_size5.short_description = '일부 내용'

    def content_len(self, Post):
        return '{}글자'.format(len(Post.content))
    content_len.short_description = '글자수'

def action1(self, request, queryset):
    queryset.update(status='p')    
action1.short_description = '모두p로 변경하기'

def action2(self, request, queryset):
    queryset.update(status='d')
action2.short_description = '모두d로 변경하기'

def action3(self, request, queryset):
    queryset.update(title = '타이틀 변경') 
action3.short_description = '선택된 title 변경하기'

def action4(self, request, queryset):
    queryset.update(body = '날씨야 좋아져라')
action4.short_description = '선택된 body 변경'

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","status"]
    ordering = ['title']
    actions = [action1, action2]

