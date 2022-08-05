from django.db import models
from django.core.files.storage import FileSystemStorage
# Create your models here.
class Photo(models.Model):
    #name = models.CharField(max_length=50)
    Photo_Image = models.ImageField(upload_to='images/')
    #Photo_Image1 = models.FileField(upload_to='images/')#n


    def save(self, *args, **kwargs):
        new_name = 'Newnameimg.png'
        self.Photo_Image.name = new_name
        #self.Photo_Image1.name = new_name#n
        super(Photo, self).save(*args, **kwargs)

    #def delete(self, *args, **kwargs):
    #    self.Photo_Img.storage.delete(self.Photo_Img.name)
    #    super(Photo,self).delete(*args, **kwargs)
    #obj=Photo.objects.get(pk=1)
    #obj.Photo_Img.delete()


    #photo = Photo.objects.get(pk=pk)
    # if `save`=True, changes are saved to the db else only the file is deleted
