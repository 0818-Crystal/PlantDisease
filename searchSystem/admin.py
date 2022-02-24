from django.contrib import admin

# Register your models here.

from .models import Plant_disease
from .models import Plant
from .models import Plant_organs
from .models import Activation
from .models import Comments


admin.site.site_header = '蔬菜病虫害管理后台'  # 设置header
admin.site.site_title = '蔬菜病虫害管理后台'  # 设置title
admin.site.index_title = '蔬菜病虫害管理后台'

admin.site.register(Plant_disease)
admin.site.register(Plant_organs)
admin.site.register(Plant)
admin.site.register(Activation)
admin.site.register(Comments)
