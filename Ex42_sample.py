from sys import argv
#class parking(object):
#    parking_lot={"101":"","102":"","103":"","104":"","105":"","106":"","107":"","108":"","109":"","110":""}
#    def __int__(self,car_no):
#        self.car_no=car_no

#    def parking_vehicle(self,car_no):
#        for slot_no,vehicle_no in list(parking_lot.items()):
#            if vehicle_no == "":
#                parking_lot[slot_no]=car_no
#            print (parking_log[slot_no])

car_no=input("Enter Car Number >>")
print (car_no)
parking_lot={"101":"","102":"","103":"","104":"","105":""}
for slot,vehicle_no in list(parking_lot.items()):
    if vehicle_no == "":
        parking_lot[slot]=car_no
        print (parking_lot[vehicle_no])
    else:
        print (f"{slot} Vehicle No:: {vehicle_no}")
