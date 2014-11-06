from django.db import models
from django.template.defaultfilters import slugify


class Staff(models.Model):
    # represents someone who works at a property.  May optionally be a staff member at multiple properties, 
    # but this model does not support someone having different roles at different properties
    name            = models.CharField(max_length=40)
    role            = models.CharField(max_length=40) # property manager, leasing agent, office assistant, maintenance
    phone           = models.CharField(max_length=15)
    email           = models.EmailField()
    # implicitly includes property_set.all() from ManyToMany defintion on Property
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('staff_detail', args=[str(self.id)])
        
    def get_update_url(self):
        from django.core.urlresolvers import reverse
        return reverse('staff_update', args=[str(self.id)])
        
    def get_delete_url(self):
        from django.core.urlresolvers import reverse
        return reverse('staff_delete', args=[str(self.id)])
        
    
        
    
class Property(models.Model):
    marketingName   = models.CharField(max_length=120)
    legalName       = models.CharField(max_length=120)
    MSA_Number      = models.IntegerField()
    MSA_Name        = models.CharField(max_length=60)
    webSite         = models.URLField()
    address         = models.TextField()
    email           = models.EmailField()
    office_phone    = models.CharField(max_length=15)
    maint_phone     = models.CharField(max_length=15)
    staff           = models.ManyToManyField(Staff)
    
    def __unicode__(self):
        return self.marketingName

class Building(models.Model):
    name            = models.CharField(max_length=40)
    managedProperty = models.ForeignKey(Property)
    structureDesc   = models.CharField(max_length=100)
    address         = models.TextField()
    def __unicode__(self):
        return self.name

class Unit(models.Model):
    building        = models.ForeignKey(Building)
    address         = models.TextField()
    sqft            = models.IntegerField()
    floorplan       = models.CharField(max_length=60)
    bedrooms        = models.IntegerField()
    bathrooms       = models.IntegerField()
    occupancyStatus = models.CharField(max_length=40)  # occupied, vacant
    economicStatus  = models.CharField(max_length=40)  # residential, commercial, down, model, employee, construction, office,  other 
    leasedStatus    = models.CharField(max_length=40)  # leased, available, approved, reserved, not ready, on notice, leased on notice, leased reserved, other 
    unitRent        = models.DecimalField(max_digits=6, decimal_places=2)
    marketRent      = models.DecimalField(max_digits=6, decimal_places=2)

    def __unicode__(self):
        return '%s %s' % ( self.building.name, self.address )


class Customer(models.Model):
    idType          = models.CharField(max_length=40)
    idToken         = models.CharField(max_length=40)
    legalName       = models.CharField(max_length=40)
    # how many addresses should we keep?  property, billing, notices, forwarding
    mailing_address = models.TextField()
    email           = models.EmailField()
    unit            = models.ForeignKey(Unit)

    def __unicode__(self):
        return self.legalName

class Lease(models.Model):
    dateSigned      = models.DateField(auto_now_add=True)
    fromDate        = models.DateField()
    thruDate        = models.DateField()
    price           = models.DecimalField(max_digits=6, decimal_places=2)
    unit            = models.ForeignKey(Unit)
    customer        = models.ForeignKey(Customer)

    def __unicode__(self):
        return 'Lease: %s' % ( self.dateSigned)


class Ledger(models.Model):
    customer        = models.ForeignKey(Customer)
    description     = models.CharField(max_length=100)
    status          = models.CharField(max_length=50) #

    def __unicode__(self):
        return 'Ledger %s' % (self.description)
    
class Transaction(models.Model):
    ledger          = models.ForeignKey(Ledger)
    description     = models.CharField(max_length=100)
    chargeCode      = models.CharField(max_length=50)
    transactionDate = models.DateField(auto_now_add=True)
    chargeFromDate  = models.DateField()
    chargeThruDate  = models.DateField()
    amount          = models.DecimalField(max_digits=6, decimal_places=2)
    comment         = models.CharField(max_length=100)
    relatedTrans    = models.ForeignKey('self')

    def __unicode__(self):
        return self.description

    