from django.db import models

class ChaiVarity(models.Model):
    CHAI_CHOICES = [
        ('black', 'Black Tea'),
        ('green', 'Green Tea'),
        ('oolong', 'Oolong Tea'),
        ('white', 'White Tea'),
        ('herbal', 'Herbal Tea'),
    ]
name = models.CharField(max_length=100, unique=True)
image= models.ImageField(upload_to='chai_varity_images/')
description = models.TextField()
date_added = models.DateTimeField(auto_now_add=True)
date_updated = models.DateTimeField(auto_now=True)

def __str__(self):
    return self.name


class ChaiReview(models.model):
    chai = models.ForeignKey(ChaiVarity, on_delete=models.CASCADE, related_name='reviews')
    user = models.CharField(max_length=100)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user} - {self.chai.name} - {self.rating}"
    
class ChaiOrder(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    ChaiVarity = models.ForeignKey(ChaiVarity, on_delete=models.CASCADE, related_name='orders')

    def __str__(self):
        return self.name
    
class ChaiCertification(models.Model):
    chai = models.ForeignKey(ChaiVarity, on_delete=models.CASCADE, related_name='certifications')
    certification_body = models.CharField(max_length=100)
    certification_date = models.DateField()
    expiration_date = models.DateField()

    def __str__(self):
        return f"{self.chai.name} - {self.certification_body}"