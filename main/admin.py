from django.contrib import admin
from .models import *
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user',)
admin.site.register(UserProfile, UserProfileAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ["id", "timestamp", "name"]
admin.site.register(ContactProfile, ContactAdmin)

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "is_active"]
admin.site.register(Testimonial, TestimonialAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "is_active"]
    readonly_fields = ["slug"]
admin.site.register(Blog, BlogAdmin)

class CertificateAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
admin.site.register(Certificate, CertificateAdmin)

class SkillAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "score"]
admin.site.register(Skill, SkillAdmin)

class MediaAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
admin.site.register(Media, MediaAdmin)

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "is_active"]
    readonly_fields = ["slug"]
admin.site.register(Portfolio, PortfolioAdmin)
