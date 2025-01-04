from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        user = self.create_user(email, name, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    is_president = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

class Organization(models.Model):
    name = models.CharField(max_length=75)

    def __str__(self):
        return self.name

class Notice(models.Model):
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=45, choices=[('Recruitment', 'Recruitment'), ('Notice', 'Notice')])
    schedule = models.DateTimeField()
    description = models.TextField()
    location = models.CharField(max_length=100)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # participants = models.ManyToManyField(User, through=)

    def __str__(self):
        return self.title

# class Participant(models.Model):
#     participant = models.ForeignKey(User, on_delete=models.CASCADE)
#     event_joined = models.ForeignKey(Notice, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.participant.name} - {self.event_joined.title}"

#     class Meta:
#         contraints = [
#             models.UniqueConstraint(
#                 fields = ["participant", "event_joined"],
#                 name = "unique_participant_event"
#             )
#         ]
