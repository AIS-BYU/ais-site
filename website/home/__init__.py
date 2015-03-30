__author__ = 'cfiloteo'
from django.dispatch import receiver
from django_cas_ng.signals import cas_user_authenticated
from home import models as hmod

###########################################################
###   Signal handler for when users authenticate via CAS

@receiver(cas_user_authenticated)
def cas_authentication_handler(sender, **kwargs):
  user = kwargs['user']
  attributes = kwargs['attributes']

  # fill out the user account with info from BYU
  for fieldname, attrname in [
    ( 'first_name', 'preferredFirstName' ),
    ( 'last_name' , 'preferredSurname' ),
    ( 'email'     , 'emailAddress' ),
    ( 'fullname'  , 'fullName' ),
  ]:
    if attributes.get(attrname):
      setattr(user, fieldname, attributes.get(attrname))
    else:
      setattr(user, fieldname, '')

  # byu status logic
  status_list = []
  for attrname in [
    'activeParttimeEmployee',
    'activeFulltimeEmployee',
    'activeFulltimeInstructor',
    'inactiveFulltimeInstructor',
    'activeParttimeNonBYUEmployee',
    'inactiveParttimeNonBYUEmployee',
    'activeEligibletoRegisterStudent',
    'inactiveFulltimeNonBYUEmployee',
    'inactiveParttimeInstructor',
    'inactiveParttimeEmployee',
    'activeFulltimeNonBYUEmployee',
    'inactiveFulltimeEmployee',
    'activeParttimeInstructor',
    'alumni',
  ]:
    if attributes.get(attrname) == 'true':
      status_list.append(attrname)
  user.byu_status = ','.join(status_list)

  # save the user
  user.save()
