# run this from the shell
# import create_users
# after syncdb
# before running other db scripts
from django.contrib.auth.models import User

user = User.objects.create_user('Jim', 'jim@jim.jim', 'JimHardPass9')
user.first_name = 'Jim'
user.second_name = 'Surname'
user.save()

user = User.objects.create_user('Maksim', 'maksim@jim.jim', 'MaksimHardPass9')
user.first_name = 'Maksim'
user.second_name = 'Surname'
user.save()

user = User.objects.create_user('Fred', 'fred@jim.jim', 'FredHardPass9')
user.first_name = 'Fred'
user.second_name = 'Surname'
user.save()

