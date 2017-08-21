from django.db.models.signals import post_save
#

def save_url_image(sender, instance, **kwargs):
    print '=====post_save======'
    #cerramos la conexion
    post_save.disconnect(save_url_image, sender=sender)
    #recuperamos la url si existe
    if instance.image_upload != None:
        instance.image = instance.image_upload.url
        #guardamos el cambio
        instance.save()
    #re-abrimos la conexxion
    post_save.connect(save_url_image, sender=sender)
