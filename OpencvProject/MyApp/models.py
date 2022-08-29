from django.db import models

# Create your models here.




class Criminals(models.Model):
    #id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=200)
    
    residence = models.CharField(max_length=50)
    country = models.CharField(max_length=50, default="Tanzania")
    education = models.CharField(max_length=150, blank=True, null=True)
    occupation = models.CharField(max_length=150, blank=True, null=True)
    marital_status = models.CharField(max_length=50, blank=True, null=True)

    Gender_Choices = (
            ('', 'Choose Gender'),
            ('Male', 'Male'),
            ('Female', 'Female'),
        )
    gender = models.CharField(choices=Gender_Choices,max_length=7)
    
    recorded_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now = True, blank=True, null=True)
    image = models.ImageField(upload_to="crimanls/")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Criminals"
class Records(models.Model):

    #id = models.CharField(max_length=100, primary_key=True)
    criminals = models.ForeignKey(Criminals, on_delete=models.CASCADE)
    #criminal_name = models.CharField(max_length=200,blank=True, null=True)
    case_records = models.TextField()
    recorded_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now = True, blank=True, null=True)
    
    



class Activities(models.Model):
    #id = models.CharField(max_length=100, primary_key=True)
    activity_name = models.CharField(max_length=50)
    link = models.CharField(max_length=200)
    description = models.TextField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to="Activities/")
    recorded_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now = True, blank=True, null=True)

    def __str__(self):
        return self.activity_name
    class Meta:
        verbose_name_plural = "Activities"
