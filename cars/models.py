from datetime import datetime

from django.db import models


# Create your models here.

class Car(models.Model):
    state_choices = (
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District Of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    )

    year_choice = []
    for year in range(2000, (datetime.now().year + 1)):
        year_choice.append((year, year))

    feature_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    car_name = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    state = models.CharField(choices=state_choices, max_length=200)
    city = models.CharField(max_length=200)
    fuel_type = models.CharField(max_length=50)
    mileage = models.IntegerField()
    transmission = models.CharField(max_length=200)
    body_design = models.CharField(max_length=200)
    car_features = models.CharField(choices=feature_choices, max_length=200)
    price = models.IntegerField()
    model_year = models.IntegerField('year', choices=year_choice)
    description = models.TextField(max_length=1000)
    main_photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    temp_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    temp_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    temp_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    temp_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    passengers = models.IntegerField()
    VIN = models.CharField(max_length=50)
    no_of_previous_owners = models.IntegerField()
    car_interior = models.CharField(max_length=100)
    car_doors = models.CharField(choices=door_choices, max_length=10)
    condition = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    engine = models.CharField(max_length=255)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.car_name

