from django.db import models
from django.template.defaultfilters import slugify
class Company(models.Model):
    comp_name = models.CharField(max_length=30)
    comp_username = models.CharField(max_length=20)
    comp_password = models.CharField(max_length=16)
    comp_phoneno = models.CharField(max_length=13)
    comp_email = models.EmailField(max_length=100)
    comp_description = models.CharField(max_length=300)
    comp_addressline1 = models.CharField(max_length=100)
    comp_addressline2 = models.CharField(max_length=100)
    comp_zipcode = models.CharField(max_length=20)
    comp_state = models.CharField(max_length=100)
    comp_country = models.CharField(max_length=100)

    def __str__(self):
        return self.comp_name

class Jobfield(models.Model):
    job_comp = models.ForeignKey(Company,on_delete=models.CASCADE)
    job_description = models.CharField(max_length=300)
    job_category = models.CharField(max_length=100)
    job_experience = models.CharField(max_length=20)
    job_location = models.CharField(max_length=50)
    job_salary = models.CharField(max_length=100)
    job_postedon = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return self.job_category


class Jobseeker (models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    contact = models.IntegerField(15)
    address = models.TextField(max_length=800)
    max_Qualification = models.CharField(max_length=150)
    resume = models.ImageField(upload_to='pdf')

'''
class Group(models.Model):
    name =models.CharField(max_length=80, unique=True)
    permission = models.ManyToManyField('Permission', blank=True)
'''

class AddJobTypes(models.Model):
	types = models.CharField(max_length=200)
	slug = models.SlugField(unique=True, blank=True, null=True)

	def __str__(self):  
		return self.types

	class Meta:
		verbose_name = ("Add Job Type")
		verbose_name_plural = ("Add Job Types")

	def save(self, *args, **kwargs):
		self.slug = slugify(self.types)
		super(AddJobTypes, self).save(*args, **kwargs)


class AddJobCategory(models.Model):
	category = models.CharField(max_length=200)
	slug = models.SlugField(unique=True, blank=True, null=True)

	def __str__(self):  
		return self.category

	class Meta:
		verbose_name = ("Add Job Category")
		verbose_name_plural = ("Add Job Categories")

	def save(self, *args, **kwargs):
		self.slug = slugify(self.category)
		super(AddJobCategory, self).save(*args, **kwargs)

class PostAJob(models.Model):
	job_title = models.CharField(max_length=200)
	employee_name = models.CharField(max_length=200)
	location = models.ForeignKey(Location)
	types = models.ForeignKey(AddJobTypes)
	category = models.ForeignKey(AddJobCategory)
	# location = models.CharField(max_length=200)
	description = models.TextField(null=True, blank=True)
	candidate_submit = models.TextField(null=True, blank=True)
	company = models.CharField(max_length=200)
	
	slug = models.SlugField(unique=True,null=True, blank=True)
	logo = models.ImageField(verbose_name=u'Image', upload_to="uploads/logo", null=True, blank=True)
	url = models.URLField(null=True, blank=True)
	twitter = models.URLField(null=True, blank=True)
	email = models.EmailField(null=True, blank=True)
	date = models.DateField(auto_now_add=True) 

	def __str__(self):  
		return self.owner_name

	class Meta:
		verbose_name = ("Add Job Post")
		verbose_name_plural = ("Add Job Posts")

	def save(self, *args, **kwargs):
		self.slug = slugify(self.company)
		super(AddJobPost, self).save(*args, **kwargs)

class AddMailTypes(models.Model):
	types = models.CharField(max_length=200)

	def __str__(self):  
		return self.types

	class Meta:
		verbose_name = ("Add Mail Type")
		verbose_name_plural = ("Add Mail Types")


class AddEmail(models.Model):
	# head_email = models.ForeignKey(HeadEmail, null=True, blank=True)
	email = models.EmailField()
	types = models.ForeignKey(AddMailTypes)

	def __str__(self):  
		return self.email

	class Meta:
		verbose_name = ("Add Email")
		verbose_name_plural = ("Add Emails")


class AddNumberTypes(models.Model):
	types = models.CharField(max_length=200)

	def __str__(self):  
		return self.types

	class Meta:
		verbose_name = ("Add Number Type")
		verbose_name_plural = ("Add Number Types")

class AddNumber(models.Model):
	
	number = models.IntegerField()
	types = models.ForeignKey(AddMailTypes)

	def __str__(self):  
		return str(self.number)

	class Meta:
		verbose_name = ("Add Number")
		verbose_name_plural = ("Add Numbers")
