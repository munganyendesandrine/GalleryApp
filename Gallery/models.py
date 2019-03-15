from django.db import models


class Category(models.Model):
    name = models.CharField(max_length =30)        

    def save_image(self):
        self.save() 

    def __str__(self):
        return self.name  

    @classmethod
    def search_by_name(cls,search_term):
        gallery = cls.objects.filter(name__icontains=search_term)
        return gallery    
   
class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name
    

# Create your models here.
class Image(models.Model):
    image_name = models.CharField(max_length =30)
    image_description = models.CharField(max_length =30)
    image_location = models.ForeignKey(Location)
    image_category = models.ForeignKey(Category)
    image = models.ImageField(upload_to = 'galleryToday/')
    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()    


    def delete_image(self):
        self.delete()

    class Meta:
        ordering = ['image_name']    
        
    @classmethod
    def get_image(cls,id):
        try:
            image=Image.objects.get(id=id)
            return image
        except DoesNotExist:
            return Image.objects.get(id=1)  
    
    # @classmethod
    # def get_comments(cls,id):
    #   comments=Comment.query.filter_by(blog_id=id).all()
    #   return comments

    # def save_comment(self):
    #     db.session.add(self)
    #     db.session.commit()

    # def fetch_comment():
    #     comment= Comment.query.all()
    #     return comment   
        




     


