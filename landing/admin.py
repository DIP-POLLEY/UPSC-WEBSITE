from django.contrib import admin
from .models import Practice1,Practice2,GS1_static,GS1_Current,GS2_static,GS2_Current,GS3_static,GS3_Current,GS4_static,GS4_Current,Essay,Sociology_static,Sociology_current


# Register your models here.
admin.site.register(Practice1)
admin.site.register(Practice2)


admin.site.register(GS1_static)
admin.site.register(GS1_Current)


admin.site.register(GS2_static)
admin.site.register(GS2_Current)


admin.site.register(GS3_static)
admin.site.register(GS3_Current)


admin.site.register(GS4_static)
admin.site.register(GS4_Current)


admin.site.register(Essay)



admin.site.register(Sociology_static)
admin.site.register(Sociology_current)


