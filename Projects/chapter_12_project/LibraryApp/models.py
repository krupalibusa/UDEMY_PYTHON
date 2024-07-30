from django.db import models

# Create your models here.

class Book(models.Model):
    BookID = models.AutoField(primary_key=True)
    BookName = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=13)
    Qty = models.IntegerField()
    category = models.CharField(max_length=255, default='')  # New field added previously
    author_name = models.CharField(max_length=255, default='')  # New field added previously
    bookstatus = models.CharField(max_length=50, default='available')  # New field

class Member(models.Model):
    MID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=15)
    email = models.EmailField()


class Borrow(models.Model):
    BID = models.AutoField(primary_key=True)
    MID = models.ForeignKey(Member, on_delete=models.CASCADE)
    BookID = models.ForeignKey(Book, on_delete=models.CASCADE)
    b_date = models.DateField(null=True, blank=True)  # Allow null values
    r_date = models.DateField(null=True, blank=True)  # Allow null values