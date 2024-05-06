import serial

from DBConnection import Db

serialPort = serial.Serial(port="COM5")
import pyttsx3
engine = pyttsx3.init()
serialString = ""                           # Used to hold data coming over UART
mm=""
counter=0
studentlogid=""
while(True):
        serialString = serialPort.read().decode('utf-8')
        mm=mm+serialString
        if len(mm)==12:
            print(mm)
            print("==============")
            # mm=""

            db=Db()
            res= db.selectOne("select id from `safetrack_student` where `Rfidnumber`='"+mm+"'")
            if res is not None:

                s=res['id']

                qry="SELECT * FROM `safetrack_checkincheckout` WHERE `Student_id`='"+str(s)+"' AND `Date`=CURDATE()"
                res1= db.select(qry)
                if len(res1)==0:
                    qry="INSERT INTO safetrack_checkincheckout(DATE,TIME,STATUS,Student_id) VALUES (CURDATE(),CURTIME(),'checkin','"+str(s)+"')"
                    db.insert(qry)
                # else:
                #     # res1= res1[0]
                #

                if len(res1)==1 and res1[0]['Status']=="Checkout":
                    qry = "INSERT INTO safetrack_checkincheckout(DATE,TIME,STATUS,Student_id) VALUES (CURDATE(),CURTIME(),'checkin','" + str(
                        s) + "')"
                    db.insert(qry)

                else:

                    if len(res1) == 1:
                        qry = "UPDATE `safetrack_checkincheckout` SET Time= curtime(), `Status`='Checkout' WHERE `id`='" + str(
                            res1[0]['id']) + "'"
                        db.update(qry)

                if len(res1)==2:

                    if res1[0]['Status']=="checkin":
                        qry = "UPDATE `safetrack_checkincheckout` SET Time= curtime(), `Status`='Checkout' WHERE `id`='" + str(
                            res1[0]['id']) + "'"
                        db.update(qry)
                    else:

                        qry = "UPDATE `safetrack_checkincheckout` SET Time= curtime(), `Status`='Checkout' WHERE `id`='" + str(
                            res1[1]['id']) + "'"
                        db.update(qry)










            mm=""