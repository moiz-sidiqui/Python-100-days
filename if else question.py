# Gretting the user according to the time

import time
timpestamp = time.strftime('%H:%M:%S')
print(timpestamp)

# getting hours
hours =  int(time.strftime('%H'))

if hours < 12: print('Good Morning')
elif hours >= 12 and hours <=20: print('Good evening')
else: print('Goodnight')



