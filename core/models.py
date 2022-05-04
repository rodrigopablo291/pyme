from django.db import models



# Create your models here.

#Tipo Usuario
class TipoUsuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombretipousuario = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    
    def __str__(self):
        return '{} '.format(self.nombretipousuario)
    
    class Meta:
        verbose_name = "TipoUsuario"
        verbose_name_plural = "TipoUsuario"
        
#Usuario
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    idtipousuario = models.ForeignKey(TipoUsuario,to_field='id',on_delete=models.CASCADE)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    
    def __str__(self):
        return '{} '.format(self.username)
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuario"

#Industria Pyme      
class IndustriaPyme(models.Model):
    id = models.AutoField(primary_key=True)
    nombreindustria = models.CharField(max_length=50)
    descripcionindustria = models.CharField(max_length=100)
    
    def __str__(self):
        return '{} '.format(self.nombreindustria)
    
    class Meta:
        verbose_name = "IndustriaPyme"
        verbose_name_plural = "IndustriaPyme"
        
#Pyme
class Pyme(models.Model):
    id = models.AutoField(primary_key=True)
    idusuario = models.ForeignKey(Usuario,to_field='id',on_delete=models.CASCADE)
    idindustriapyme = models.ForeignKey(IndustriaPyme,to_field='id',on_delete=models.CASCADE)
    nombrepyme = models.CharField(max_length=50)
    rutpyme = models.CharField(max_length=30) # LO DEJE CHAR POR SI QUIERE PONER PUNTO Y GUION
    descripcion = models.CharField(max_length=100)
    comuna = models.CharField(max_length=30)
    email =  models.EmailField()
    telefono = models.IntegerField()
    whatsapp = models.CharField(max_length=15) #TAMBIEN CHAR POR SI QUIERE COLOCAR EL +
    telegram = models.CharField(max_length=20)
    
    def __str__(self):
        return '{} '.format(self.nombrepyme)
    
    class Meta:
        verbose_name = "Pyme"
        verbose_name_plural = "Pyme"
        
#Categoria Demanda Oferta
class CategoriaDemandaOferta(models.Model):
    id = models.AutoField(primary_key=True)
    nombrecategoria = models.CharField(max_length=30,null=True,unique=True) # de esta manera al migrar no me pedira ingresar un dato obligatoriamente, pero el unique me lo pide obligatoriamente cuando no es una clave foreanea
    descripcion = models.CharField(max_length=100)
    
    def __str__(self):
            return '{} '.format(self.nombrecategoria)
    
    class Meta:
        verbose_name = "CategoriaDemandaOferta"
        verbose_name_plural = "CategoriaDemandaOferta"
        
# ===================================================================

#Demanda Pyme
class DemandaPyme(models.Model):
    id = models.AutoField(primary_key=True)
    idpymed = models.ForeignKey(Pyme,to_field='id',on_delete=models.CASCADE)
    idcategoriademaandaoferta = models.ForeignKey(CategoriaDemandaOferta,to_field='id',on_delete=models.CASCADE)
    demandapyme = models.ForeignKey(CategoriaDemandaOferta,to_field='nombrecategoria',on_delete=models.CASCADE,related_name='demandaspyme')
    descripcion = models.CharField(max_length=100)
    
    def __str__(self):
            return '{} '.format(self.id)
    
    class Meta:
        verbose_name = "DemandaPyme"
        verbose_name_plural = "DemandaPyme"

#Oferta Pyme

class OfertaPyme(models.Model):
    id = models.AutoField(primary_key=True)
    idpymeo = models.ForeignKey(Pyme,to_field='id',on_delete=models.CASCADE)
    idcategoriademandaoferta = models.ForeignKey(CategoriaDemandaOferta,to_field='id',on_delete=models.CASCADE)
    ofertapyme = models.ForeignKey(CategoriaDemandaOferta,to_field='nombrecategoria',on_delete=models.CASCADE,related_name='ofertaspyme')
    descripcion = models.CharField(max_length=100)