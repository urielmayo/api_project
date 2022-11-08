import imp
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Dealer(models.Model):
    """Model definition for Dealer."""

    name = models.CharField(max_length=100)

    class Meta:
        """Meta definition for Dealer."""

        verbose_name = 'Dealer'
        verbose_name_plural = 'Dealers'

    def __str__(self):
        """Unicode representation of Dealer."""
        return self.name

class Lead(models.Model):
    """Model definition for Lead."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Lead."""

        verbose_name = 'Lead'
        verbose_name_plural = 'Leads'

    def __str__(self):
        """Unicode representation of Lead."""
        return self.dealer


class Post(models.Model):
    """Model definition for Post."""

    title = models.CharField(max_length=50)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Post."""

        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        """Unicode representation of Post."""
        return self.title

class Color(models.Model):
    """Model definition for Color."""

    name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100)
    class Meta:
        """Meta definition for Color."""

        verbose_name = 'Color'
        verbose_name_plural = 'Colors'

    def __str__(self):
        """Unicode representation of Color."""
        return self.name

class Vehicle(models.Model):
    """Model definition for Vehicle."""

    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True)
    dealer = models.ForeignKey(Dealer, related_name='vehicles', on_delete=models.CASCADE)
    posts = models.ManyToManyField(Post)
    in_stock = models.BooleanField()
    class Meta:
        """Meta definition for Vehicle."""

        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'

    def __str__(self):
        """Unicode representation of Vehicle."""
        return self.name

class AccesoryCategory(models.Model):
    """Model definition for AccesoryCategory."""

    name = models.CharField(max_length=30)
    class Meta:
        """Meta definition for AccesoryCategory."""

        verbose_name = 'Accesory Category'
        verbose_name_plural = 'Accesory Categories'

    def __str__(self):
        """Unicode representation of AccesoryCategory."""
        return self.name

class AccesoryModel(models.Model):
    """Model definition for AccesoryModel."""

    # TODO: Define fields here
    name = models.CharField(max_length=50)
    class Meta:
        """Meta definition for AccesoryModel."""

        verbose_name = 'Accesory Model'
        verbose_name_plural = 'Accesory Models'

    def __str__(self):
        """Unicode representation of AccesoryModel."""
        return self.name


class Accesory(models.Model):
    """Model definition for Accesory."""

    name = models.CharField(max_length=50)
    model = models.ForeignKey(AccesoryModel, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(AccesoryCategory, on_delete=models.SET_NULL, null=True)
    dealer = models.ForeignKey(Dealer, related_name='accesories', on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True)
    price = models.PositiveIntegerField()
    in_stock = models.BooleanField()
    year_of_compatibility = models.PositiveSmallIntegerField()

    class Meta:
        """Meta definition for Accesory."""

        verbose_name = 'Accesory'
        verbose_name_plural = 'Accesories'

    def __str__(self):
        """Unicode representation of Accesory."""
        return self.name
