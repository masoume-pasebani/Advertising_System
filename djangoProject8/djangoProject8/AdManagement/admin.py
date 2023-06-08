from django.contrib import admin

# Register your models here.

from .models import Advertiser
from .models import Ad
from .models import Click
from .models import View
admin.site.register(Advertiser)
admin.site.register(Ad)
admin.site.register(Click)
admin.site.register(View)
