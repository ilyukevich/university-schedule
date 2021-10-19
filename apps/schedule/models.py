from django.db import models

# Create your models here.


# class Product(models.Model):
#     """Description models of product"""
#
#     category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
#     name = models.CharField(max_length=200, db_index=True)
#     slug = models.SlugField(max_length=200, db_index=True)
#     image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
#     description = models.TextField(blank=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     available = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         ordering = ('name',)
#         index_together = (('id', 'slug'),)
#
#     def __str__(self):
#         return self.name
#
#     def get_absolute_url(self):
#             return reverse('shop:product_detail',
#                            args=[self.id, self.slug])