# import the opencv library
import cv2
import face_recognition

from Safetrack.DBConnection import  Db
db=Db()


qry="SELECT * FROM `safetrack_Student`"
res=db.select(qry)

knownimage=[]
knownids=[]
knownsems=[]


for i in res:
    s=i['Photo']
    s=s.replace("/","\\")
    pth="C:\\Users\\HP\\PycharmProjects\\untitled"+ s


    picture_of_me = face_recognition.load_image_file(pth)
    print(pth)
    my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]
    print(my_face_encoding)
    knownimage.append(my_face_encoding)
    knownids.append(i['id'])
    # knownsems.append(str(i['sem']))







# define a video capture object
vid = cv2.VideoCapture(0)




while(True):

    ret, frame = vid.read()
    from _datetime import datetime
    a=datetime.now().strftime('%Y%m%d%H%M%S%f')+'.jpg'
    cv2.imwrite(r"C:\Users\HP\PycharmProjects\untitled\media\detectedface\\"+a,frame)
    cv2.imwrite("a.jpg",frame)

    picture_of_others = face_recognition.load_image_file("a.jpg")
    print(pth)
    others_face_encoding = face_recognition.face_encodings(picture_of_others)


    totface=len(others_face_encoding)

    from datetime import datetime

    curh = float(str(datetime.now().time().hour) + "." + str(datetime.now().time().minute))

    print(curh, "hgfhhgfgfghfghfgh")

    for i in range(0,totface):
        res=face_recognition.compare_faces(knownimage,others_face_encoding[i],tolerance=0.5)
        print(res)

        l=0

        for j in res:
            if j==True:

                # qry="SELECT * FROM `Safetrack_facedetection` WHERE  `Student_id`='"+str(knownids[l])+"'"
                # res=db.selectOne(qry)
                #
                # if res is None:
                qry="INSERT INTO `Safetrack_facedetection` (`Student_id`,`Date`,`Photo`,`Time`) VALUES ('"+str(knownids[l])+"',CURDATE(),'/media/detectedface/"+a+"',curtime())"
                db.insert(qry)
            l=l+1
