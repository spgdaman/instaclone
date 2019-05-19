from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Image(models.Model):
    image=models.ImageField(upload_to='media/')
    image_name=models.CharField(max_length=30)
    image_caption=HTMLField()
    likes=models.IntegerField()
    comments=models.CharField(max_length=120)

    # Foreign key
    profile = models.ForeignKey('Profile')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Image model methods
    @classmethod
    def save_image(cls):
        image_saved=cls.objects.save()
        return image_saved

    @classmethod
    def delete_image(self,image_id):
        image_deleted=cls.objects.filter(id=image_id).delete()
        return image_deleted

    @classmethod
    def update_image(self,image_id,image_name):
        image_updated=cls.objects.filter(id=image_id).update(image_name=image_name)        
        return image_updated

class Profile(models.Model):
    profile_photo=models.ImageField(upload_to='images/')
    bio=HTMLField()

    # Profile model methods
    @classmethod
    def save_profile(cls):
        profile_saved=cls.objects.save()
        return profile_saved

    @classmethod
    def delete_profile(self,profile_id):
        delete_profile=cls.objects.filter(id=profile_id).delete()
        return delete_profile

    @classmethod
    def update_profile(self,profile_id,bio):
        updated_profile=cls.objects.filter(id=profile_id).update(bio=bio)
        return updated_profile
        