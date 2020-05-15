from django.db import models

class Customer(models.Model):
    allsubject = (('ในเมือง','ในเมือง'),
                  ('นอกเขตเมือง','นอกเขตเมือง'))


    customer_subject = models.CharField(max_length=200, choices=allsubject, default='ในเมือง')
    customer_name = models.CharField(max_length=200)
    customer_id = models.IntegerField(default=0)

    def __str__(self):
        return self.customer_name + ' - ' + self.customer_subject+ ' - ' + str(self.customer_id)
    


