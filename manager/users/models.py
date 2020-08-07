from django.db import models

# Create your models here.
class Users (models.Model):
    rmit_id = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(max_length=100, unique=True)
    about_me = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users'
        # verbose_name = _("Users ")
        # verbose_name_plural = _("Users s")

    # def __str__(self):
    #     return self.name

    # def get_absolute_url(self):
    #     return reverse("Users _detail", kwargs={"pk": self.pk})
