# -*- coding: utf-8 -*-


def module_method():
    return "I am a module method"

class AccLib:

     @staticmethod
     def static_method():
         # the static method gets passed nothing
         return "I am a static method"

     @classmethod
     def class_method(cls):
         # the class method gets passed the class (in this case ModCLass)
         return "I am a class method"

     def instance_method(self):
         # An instance method gets passed the instance of ModClass
         return "I am an instance method"


#------------------------------------------------ Correct Time ------------------------------------
    # Used by Account Line 
    # Correct Time 
    # Format:   1876-10-10 00:00:00
    @classmethod
    def correct_time(self, date, delta):
        #print
        #print 'Correct'
        #print date 
        # Print delta 
        if date != False:
            year = int(date.split('-')[0])
            if year >= 1900:
                DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
                DATETIME_FORMAT_sp = "%d/%m/%Y %H:%M"
                date_field1 = datetime.datetime.strptime(date, DATETIME_FORMAT)
                date_corr = date_field1 + datetime.timedelta(hours=delta,minutes=0)
                date_corr_sp = date_corr.strftime(DATETIME_FORMAT_sp)
                return date_corr, date_corr_sp
    # correct_time


