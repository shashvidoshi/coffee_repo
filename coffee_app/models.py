from django.db import models

class Inventory(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='coffee_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.price} ({self.quantity})"


class UpdateInventory:
    @staticmethod
    def update(pk, name=None, price=None, quantity=None, image=None):
        try:
            obj = Inventory.objects.get(pk=pk)
            if name is not None:
                obj.name = name
            if price is not None:
                obj.price = price
            if quantity is not None:
                obj.quantity = quantity
            if image is not None:
                obj.image = image
            obj.save()
            return obj
        except Inventory.DoesNotExist:
            return None


class DeleteInventory:
    @staticmethod
    def delete(pk):
        try:
            obj = Inventory.objects.get(pk=pk)
            obj.delete()
            return True
        except Inventory.DoesNotExist:
            return False
