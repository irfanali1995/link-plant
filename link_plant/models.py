from django.db import models

# Each Class is table in DB

#profiles  -> Links 

class Profile(models.Model):
    BG_CHOICES =(
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('yellow', 'Yellow'),
    )
    # name of profile, slug, bg_color 
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    bg_color = models.CharField(max_length=50, choices=BG_CHOICES) 
    

    # To make easy and readabile in admin we change dunder method to return name values
    def __str__(self):
        return self.name
    
class Link(models.Model):
    # text, url, profile
    text = models.CharField(max_length=100)
    url = models.URLField((""), max_length=200)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="links")

    def __str__(self):
        return f"{self.text} | {self.url}"