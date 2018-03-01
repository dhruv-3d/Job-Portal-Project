import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','job_portal_project.settings')

import django
django.setup()
from jportal.models import Graduation, Post_Graduation, PhD

a=[{'title':"Not Pursuing Graduation"},{'title':"B.A."},{'title':"B.Arch"},{'title':"B.Des."},
{'title':"B.El.Ed"},{'title':"B.P.Ed"},{'title':"B.U.M.S"},{'title':"BAMS"},{'title':"BCA"},
{'title':"B.B.A/B.M.S"},{'title':"B.Com"},{'title':"B.Ed"},{'title':"BDS"},{'title':"BFA"},
{'title':"BHM"},{'title':"B.Pharma"},{'title':"B.Sc"},{'title':"B.Tech/B.E."},{'title':"BHMS"},
{'title':"LLB"},{'title':"MBBS"},{'title':"Diploma"},{'title':"BVSC"},{'title':"Other"}]

b=[{'title':"CD"},{'title':"CS"},{'title':"ICWA(CMA)"},{'title':"Integrated PG"},
{'title':"LLM"},{'title':"M.A."},{'title':"M.Arch"},{'title':"M.Ch."},{'title':"M.Com."},
{'title':"M.Des."},{'title':"M.Ed."},{'title':"M.Pharma."},{'title':"MDS"},{'title':"MFA"},
{'title':"M.S./M.Sc.(Science)"},{'title':"M.Tech."},{'title':"MBA/PGDM"},{'title':"MCA"},
{'title':"Medical-MS/MD"},{'title':"PG Diploma"},{'title':"MVSC"},{'title':"DM"},{'title':"MCM"},
{'title':"Other"}]

c=[{'title':"Ph.D/Doctorate"},{'title':"MPHIL"},{'title':"Other"}]

for i in a:
    g = Graduation()
    a = Graduation.objects.get_or_create(title=i['title'])[0]
    a.save()

for i in b:
    pg = Post_Graduation()
    b = Post_Graduation.objects.get_or_create(title=i['title'])[0]
    b.save()

for i in c:
    pg = PhD()
    b = PhD.objects.get_or_create(title=i['title'])[0]
    b.save()


