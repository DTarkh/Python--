

import time
import threading

def serving(customer):
    print(f"started serving {customer}")
    time.sleep(5)
    print("served")


start_time=time.time()
## serving("david")
# serving("john")
# serving("anna")
# serving("mari")
# serving("gio")



customers = ["david", "john", "anna", "mari", "gio"]


threads = []

for customer in customers:
    thread = threading.Thread(target=serving, args=(customer,))
    threads.append(thread)
    thread.start()



for thread in threads:
    thread.join()

end_time=time.time()
time_took=end_time-start_time
print(time_took, )

