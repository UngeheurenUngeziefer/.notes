from django.db import models

# Create your models here.
# Topic model
class Topic(models.Model):
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.text

class Entry(models.Model):
	"""Информация, изученная пользователем по теме"""
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		"""Возвращает строковое представление модели."""
		if len(self.text) < 50:
			return self.text
		else:
			return self.text[:50] + "..."