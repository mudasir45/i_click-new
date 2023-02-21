from django.contrib import admin
from .models import ProjectDetails
from .models import ReviewersDetails
from .models import SupervisorDetails
from .models import Reviews

admin.site.register(ProjectDetails)
admin.site.register(ReviewersDetails)
admin.site.register(SupervisorDetails)
admin.site.register(Reviews)

