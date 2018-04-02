from openerp.exceptions import ValidationError


@api.constrains('age')

def _check_something(self):

    for record in self:

        if record.age > 20:

            raise ValidationError("Your record is too old: %s" % record.age)

    # all records passed the test, don't return anything