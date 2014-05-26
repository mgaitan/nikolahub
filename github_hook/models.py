from django.db import models
import subprocess


class Hook(models.Model):
    user = models.ForeignKey('auth.User')
    ghuser = models.CharField(max_length=255)
    ghrepo = models.CharField(max_length=255)

    def execute(self):
        subprocess.call([self.path])

    def __unicode__(self):
        return "%s (%s/%s)" % (self.name, self.user, self.repo)

    class Meta:
        db_table = 'github_hook'
