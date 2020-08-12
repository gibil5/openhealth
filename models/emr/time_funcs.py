# -*- coding: utf-8 -*-
"""
    TimeFuncs - Openhealth

    Created:                27 Jul 2020
    Last updated:           11 Aug 2020
"""
from datetime import datetime,tzinfo,timedelta

#------------------------------------------------ Time ---------------------------------------------------
class Zone(tzinfo):
    def __init__(self,offset,isdst,name):
        self.offset = offset
        self.isdst = isdst
        self.name = name
    def utcoffset(self, dt):
        return timedelta(hours=self.offset) + self.dst(dt)
    def dst(self, dt):
            return timedelta(hours=1) if self.isdst else timedelta(0)
    def tzname(self,dt):
         return self.name
