from django.db import models

# Create your models here.

# Comments added FOR REVIEW ... WILL BE REMOVED

# Books:
# 	1. id
# 	2. title
# 	3. year
# 	4. edition - CharField or IntegerField or Decimal ?
# 	5. language -
# 	6. ISBN
# 	7. type (eBook/printed)

# Author:
# 	1. id
# 	2. firstName
# 	3. middleName
# 	4. lastName

# Book Author Mapping
# 	1. bookId
# 	2. authorId

# Publisher
# 	1. id
# 	2. name

# Publisher Book Mapping
# 	1. publisherId
# 	2. bookId

# Copy
# 	1. id
# 	2. book id
# 	3. status
# 	4. lease-link

# Location
# 	1. id
# 	2. main division (shelf/rack)
# 	3. sub division (row)
# 	4. sub-sub division (column)

# Copy Location Link
# 	1. copy id
# 	2. location id

# UserRoleMapping
# 	1. user id
# 	2. role id

# Categories
# 	1. id
# 	2. name
# 	3. description

# CategoryConfiguration
# 	1. category id
# 	2. book count
# 	3. lease days
# 	4. fine rate
# 	5. ebook access (true/false)

# UserCategoryMapping
# 	1. user id
# 	2. category id

# Role
# 	1. id
# 	2. name
# 	3. description

# Lend
# 	1. id
# 	2. user id
# 	3. copy id
# 	4. date of issue
# 	5. date of return

# FineCollection
# 	1. lend id
# 	2. amount
# 	3. payment mode

# Tenant Independent:


class BookType(models.Model):
    type = models.CharField(max_length=50)


class Book(models.Model):
    title = models.CharField(max_length=500)
    year = models.IntegerField()
    edition = models.CharField(max_length=10)
    language = models.CharField(max_length=50)
    isbn = models.CharField(max_length=50)
    type = models.ForeignKey(BookType, on_delete=models.CASCADE)


class Author(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50)


class BookAuthorMapping(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)


class Publisher(models.Model):
    name = models.CharField(max_length=500)


class PublisherBookMapping(models.Model):
    publisher_id = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)


class Copy(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    lease_link = models.ForeignKey('Lease', on_delete=models.CASCADE)


class Lease(models.Model):
    copy_id = models.ForeignKey(Copy, on_delete=models.CASCADE)
    user_id = models.ForeignKey('core.UserData', on_delete=models.CASCADE)
    date_of_issue = models.DateField()
    date_of_return = models.DateField()


class Location(models.Model):
    main_division = models.CharField(max_length=50)
    sub_division = models.CharField(max_length=50)
    sub_sub_division = models.CharField(max_length=50)


class CopyLocationLink(models.Model):
    copy_id = models.ForeignKey(Copy, on_delete=models.CASCADE)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)


class Role(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)


class UserRoleMapping(models.Model):
    user_id = models.ForeignKey('core.UserData', on_delete=models.CASCADE)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)


class CategoryConfiguration(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    book_count = models.IntegerField()
    lease_days = models.DecimalField(max_digits=4, decimal_places=1)
    fine_rate = models.DecimalField(max_digits=4, decimal_places=1)
    ebook_access = models.BooleanField()


class UserCategoryMapping(models.Model):
    user_id = models.ForeignKey('core.UserData', on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)


class FineCollection(models.Model):
    lease_id = models.ForeignKey(Lease, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=4, decimal_places=1)
    payment_mode = models.CharField(max_length=20)
