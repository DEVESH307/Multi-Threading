import time
import threading

def firstName(name):
    print ("First Name:")
    for i in range(5):
        time.sleep(2)
        print (name[0])
        print (name[0])

def lastName(name):
    print("Last Name:")
    for i in range(5):
        time.sleep(2)
        print (name[1])
        print (name[1])

arr = ['Devesh','Jaiswal']

t = time.time()

t1 = threading.Thread(target = firstName, args = (arr, ))
t2 = threading.Thread(target = lastName, args = (arr, ))

t1.start()
t2.start()

t1.join()
t2.join()

print ("done in : ", time.time()-t)
print ("DONE!!!!!!")

