from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from PIL import Image


class Status(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=280)
    retweeted_tweet_id = models.CharField(max_length=20)
    date_posted = models.DateTimeField(default=timezone.now)
    mention_to_other_tweet = models.OneToOneField(
        "self", models.SET_NULL, blank=False, null=True
    )

    def __str__(self):
        return self.message[:140]

    def get_absolute_url(self):
        return reverse("tweet-detail", kwargs={"pk": self.pk})


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return "{} Profile".format(self.user.username)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="following"
    )


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_tweet = models.CharField(max_length=20)
