from django.contrib import admin

from Bloodbank.models import Designation, Donor, OrganizationMember, Booking
from Bloodbank.models import Upazila, Zilla, Applicant, BloodGroup, About
admin.site.register(Applicant)
admin.site.register(Donor)
admin.site.register(Designation)
admin.site.register(OrganizationMember)
admin.site.register(About)
admin.site.register(Zilla)
admin.site.register(Upazila)
admin.site.register(BloodGroup)
admin.site.register(Booking)