from django.db import models
from django.shortcuts import reverse


from datetime import datetime
import datetime
# Create your models here.


def gen_slug(dt):
    a = dt.timestamp() * 1000000
    b = str(int(a))
    c = b[5:][::-1]
    d = hex(int(c))[2:][::-1]
    return d


def gen_time(s):
    t1 = s[19:]
    l = len(t1)-1
    t2 = t1[:l]
    t3 = t2.split(', ')
    if len(t3)==2:
        return datetime.timedelta(int(t3[0]), int(t3[1]), 0)
    if len(t3)==1:
        print(datetime.timedelta(int(t3[0]), 0, 0))
        return datetime.timedelta(int(t3[0]), 0, 0)


class Paste(models.Model):
    t1min = repr(datetime.timedelta(0, 60, 0))
    t10min = repr(datetime.timedelta(0, 600, 0))
    t1hour = repr(datetime.timedelta(0, 3600, 0))
    t1day = repr(datetime.timedelta(1, 0, 0))
    t1week = repr(datetime.timedelta(7, 0, 0))
    t1month = repr(datetime.timedelta(30, 0, 0))
    t1year = repr(datetime.timedelta(365, 0, 0))
    tinf = repr(datetime.timedelta(0))
    times = [
        (tinf, 'inf'),
        (t1min, '1 min'),
        (t10min, '10 min'),
        (t1hour, '1 hour'),
        (t1day, '1 day'),
        (t1week, '1 week'),
        (t1month, '1 month'),
        (t1year, '1 year'),
    ]

    public = 'public'
    unlisted = 'unlisted'
    private = 'private'
    access_choices = [
        (public, 'public'),
        (unlisted, 'unlisted'),
        (private, 'private'),
    ]

    slug = models.SlugField(max_length=8, unique=True)
    title = models.CharField(max_length=150, db_index=True, blank=True)
    body = models.TextField(db_index=True)
    author = models.CharField(max_length=150, db_index=True)
    life_time = models.CharField(max_length=100, choices=times, default=datetime.timedelta(0))
    create_time = models.DateTimeField(auto_now_add=True)
    die_time = models.DateTimeField(null=True)
    access = models.CharField(max_length=50, choices=access_choices, default='public')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('paste_detail_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('paste_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(datetime.datetime.now())
            # if request.user.is_authenticated:
            #     pass
            # else:
            print(dir(kwargs))
            print()
            print(dir(args))
            print()
            print(dir(self))
            print()
            self.author = 'guest'
            if not self.title:
                self.title = 'untitled'
            if self.life_time!='datetime.timedelta(0)':
                self.die_time = datetime.datetime.now() + gen_time(self.life_time)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-create_time']
