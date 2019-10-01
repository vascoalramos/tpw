from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=30)
    cp = models.CharField(max_length=10)
    local = models.CharField(max_length=35)
    country = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.street}, {self.local}, {self.cp} [{self.country}]"


class Person(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    nationality = models.CharField(max_length=30)
    gender = models.CharField(max_length=15)
    photo = models.ImageField(upload_to="images/")
    desired_job = models.CharField(max_length=100)
    business_sector = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Phone(models.Model):
    country_prefix = models.CharField(max_length=5)
    number = models.CharField(max_length=20)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.country_prefix} {self.number}"


class Fax(models.Model):
    country_prefix = models.CharField(max_length=5)
    number = models.CharField(max_length=20)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.country_prefix} {self.number}"


class Email(models.Model):
    email_type = models.CharField(max_length=20)
    value = models.EmailField()
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.email_type} | {self.value}"


class Employer(models.Model):
    name = models.CharField(max_length=40)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    website = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class WorkExperience(models.Model):
    occupation = models.CharField(max_length=40)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    stat_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.occupation


class Activity(models.Model):
    designation = models.CharField(max_length=10)
    time = models.CharField(max_length=15)
    work_exp = models.ForeignKey(WorkExperience, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.designation} | {self.time}"
