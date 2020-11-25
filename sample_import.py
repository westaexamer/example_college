import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "examplecollege.settings")

from examplecollege.school.models import (
    Learner,
    Person,
)

p = Person(first_name="Cal", last_name='Kestis', email_address="cal.kestis@sw.net", phone_number="0117361155")
p.save()
l = Learner(person=p, student_number="LE188443")
l.save()