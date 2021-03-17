# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 11:18:13 2021

@author: wcoughlan1
"""

import time
dir(time)

import random
dir(random)

print("When prompted hit the enter key")

x = random.normalvariate(0, 5)
time.sleep(x)

time_1 = time.time()
input("Quick hit the Enter key!")


time_2 = time.time()

time_elapsed = time_2 - time_1
formatted_time_elapsed = "{:.2f}".format(time_elapsed)


result = "That was fast. It took you {} seconds to press Enter".format(formatted_time_elapsed)
print(result)



      