from django.db import models

# Create your models here.
class Menu(models.Model):
    meal_name=models.CharField(default="",blank=False,max_length=200)
    describe=models.TextField(default="",blank=False,max_length=1000)
    price = models.FloatField()
    category = models.CharField(max_length=30,)
    image=models.ImageField(upload_to='menu_images/')
    state=models.IntegerField(default=1)

    

    class Meta:
        db_table= "Menu"

    def __str__(self):
        return self.meal_name
    

