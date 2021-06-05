from django.contrib import admin
from Statement.models import Tax, Financial, BloodDonation,DailyDonation, TotalDonation, DonationPhoto, Calender

# Register your models here.

admin.site.register(Tax)
admin.site.register(Financial)
admin.site.register(BloodDonation)
admin.site.register(DailyDonation)
admin.site.register(TotalDonation)
admin.site.register(DonationPhoto)
admin.site.register(Calender)
