from django.db import models


class Link(models.Model):
    name = models.CharField(max_length=250)
    link = models.CharField(max_length=250)
    status = models.CharField(max_length=25, default='New')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'


class Info(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    type = models.CharField(max_length=250, null=True, blank=True)
    domesticity = models.CharField(max_length=250, null=True, blank=True)
    registered_agent = models.CharField(max_length=250, null=True, blank=True)
    date_formed = models.CharField(max_length=20, null=True, blank=True)
    duration = models.CharField(max_length=250, null=True, blank=True)
    renewal_month = models.CharField(max_length=50, null=True, blank=True)
    report_due = models.CharField(max_length=20, null=True, blank=True)
    chapter = models.CharField(max_length=250, null=True, blank=True)
    home_state = models.CharField(max_length=250, null=True, blank=True)
    status = models.CharField(max_length=250, null=True, blank=True)
    link = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Info'
        verbose_name_plural = 'Info'


class Keys_w(models.Model):
    name = models.CharField(max_length=250)
    status = models.CharField(max_length=25, default='New')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Key'
        verbose_name_plural = 'Keys'
