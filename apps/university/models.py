from django.db import models


class Faculties(models.Model):
    """***"""

    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'faculty'
        verbose_name_plural = 'faculties'

    def __str__(self):
        return self.name


class Departaments(models.Model):
    """***"""

    faculty = models.ForeignKey(Faculties, related_name='faculties', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'departament'
        verbose_name_plural = 'departaments'

    def __str__(self):
        return self.name


class StudyGroups(models.Model):
    """***"""

    departament = models.ForeignKey(Departaments, related_name='departaments', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'studygroup'
        verbose_name_plural = 'studygroups'

    def __str__(self):
        return self.name


class Auditories(models.Model):
    """***"""

    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'auditory'
        verbose_name_plural = 'auditories'

    def __str__(self):
        return self.name


class Disciplines(models.Model):
    """***"""

    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'discipline'
        verbose_name_plural = 'disciplines'

    def __str__(self):
        return self.name
