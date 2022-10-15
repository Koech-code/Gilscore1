from distutils.command.upload import upload
from email.policy import default
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from accounts.models import User


CLUB_CHOICES = (
    ("", ""),
    ("Manchester", "Manchester"),
    ("Arsenal", "Arsenal"),
    ("Liverpool", "Liverpool"),
    ("Chelsea", "Chelsea"),
)

class ChampionLeague(models.Model):
    icon = models.ImageField(blank=True, null=True, upload_to='images/club')
    def __str__(self):
        return f'{self.icon.url}'


class EuropaLeague(models.Model):
    icon = models.ImageField(blank=True, null=True, upload_to='images/club')
    def __str__(self):
        return f'{self.icon.url}'

class AfconLeague(models.Model):
    icon = models.ImageField(blank=True, null=True, upload_to='images/club')
    def __str__(self):
        return f'{self.icon.url}'


class Baseball(models.Model):
    icon = models.ImageField(blank=True, null=True, upload_to='images/club')
    def __str__(self):
        return f'{self.icon.url}'


class Bundesliga(models.Model):
    icon = models.ImageField(blank=True, null=True, upload_to='images/club')
    def __str__(self):
        return f'{self.icon.url}'


class Formula1(models.Model):
    icon = models.ImageField(blank=True, null=True, upload_to='images/club')
    def __str__(self):
        return f'{self.icon.url}'


class Laliga(models.Model):
    icon = models.ImageField(blank=True, null=True, upload_to='images/club')
    def __str__(self):
        return f'{self.icon.url}'

class NBA(models.Model):
    icon = models.ImageField(blank=True, null=True, upload_to='images/club')
    def __str__(self):
        return f'{self.icon.url}'


class NFL(models.Model):
    icon = models.ImageField(blank=True, null=True, upload_to='images/club')
    def __str__(self):
        return f'{self.icon.url}'

class Worldcup(models.Model):
    icon = models.ImageField(blank=True, null=True, upload_to='images/club')
    def __str__(self):
        return f'{self.icon.url}'        


class FollowerRelation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profilepic/', blank=True, null=True)
    club = models.CharField(choices=CLUB_CHOICES, default='', max_length=50)
    club_icon = models.ImageField(upload_to='icons/', blank=True, default='')
    location = models.CharField(max_length=220, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    followers = models.ManyToManyField(User, related_name='following', blank=True)
    """
    project_obj = Profile.objects.first()
    project_obj.followers.all() -> All users following this profile
    user.following.all() -> All user profiles I follow
    """
    def user_did_save(sender, instance, created, *args, **kwargs):
        if created:
            Profile.objects.get_or_create(user=instance)

    post_save.connect(user_did_save, sender=User)


# after the user logs in -> verify profile