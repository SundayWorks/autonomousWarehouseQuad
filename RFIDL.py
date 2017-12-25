from firebase import firebase
firebase = firebase.FirebaseApplication('http://drone-189912.firebaseio.com/RFID',None)
result= firebase.post('/RFID',{'user_id':'wilma','text':'hello'})

