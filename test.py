# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 14:45:43 2016

@author: Jeff
"""
import wavepy
import time
start = time.clock()
X = wavepy.wavepy();

X.Validate(5)
print time.clock() - start, "seconds"