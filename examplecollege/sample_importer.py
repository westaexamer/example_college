import os
import sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'examplecollege.settings'

# Since feeder.py is in Dashboard_app, you need to add the parent directory
# to the python path so that dashex can be imported
# (without this you'll get the 'no module named dashex' error)
sys.path.append('..')

import django
django.setup()

from school.models import Learner, Person
p = Person(first_name="Cal", last_name='Kestis', email_address="cal.kestis@sw.net", phone_number="0117361155")
p.save()
l = Learner(person=p, student_number="LE188443")
l.save()
