from django.shortcuts import render
from django.views import View
import pyrebase
import json

config={
    "apiKey": "AIzaSyDDuNEqgG_VH0deVFt7Iq4HTYTxQAcSuNE",
    "authDomain": "automatic-garde.firebaseapp.com",
    "databaseURL": "https://automatic-garde-default-rtdb.firebaseio.com",
    "projectId": "automatic-garde",
    "storageBucket": "automatic-garde.appspot.com",
    "messagingSenderId": "198862866102",
    "appId": "1:198862866102:web:ac776223c9b4aba5fc4817",
    "measurementId": "G-MM17GXGDPV"
}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()
def index(request):

    channel_name = database.child('Data').child('Name').get().val()
    channel_sub = database.child('Data').child('Sub').get().val()

    return render(request, 'index2.html', {
        "channel_name": channel_name,
        "channel_sub": channel_sub
        })
# def listen_to_firebase_changes(request):
#     # Kết nối đến Firebase Realtime Database
#     database = firebase.database()

#     def stream_handler(message):
#         # Xử lý sự kiện thay đổi trên Firebase
#         print("Thay đổi trên Firebase:", message["event"])  # Theo dõi sự kiện thay đổi

#         # Thực hiện các thao tác cần thiết để cập nhật giao diện Django

#     # Lắng nghe sự thay đổi trên Firebase
#     database.child("your_data_path").stream(stream_handler)

#     return render(request, "your_template.html")
# def update_firebase_data(request):

#     # Đọc giá trị hiện tại từ Firebase
#     current_value = database.child("Data").child("light").get().val()

#     # Kiểm tra giá trị hiện tại và thực hiện thay đổi
#     if current_value == 1:
#         # Nếu đèn đã bật, thì tắt đèn (đặt giá trị là 0)
#         new_value = 0
#     else:
#         # Nếu đèn đã tắt hoặc không xác định, thì bật đèn (đặt giá trị là 1)
#         new_value = 1

#     # Cập nhật giá trị mới lên Firebase
#     database. database.child("Data").child("light").set(new_value)

#     Data = {

#     }

#     # Trả về trang web hoặc thông báo thành công
#     return render(request, "index.html",)


# def control_lights(request):
#     # Kết nối đến Firebase Realtime Database
#     database = firebase.database()

#     # Đọc trạng thái đèn từ Firebase
#     light_status = database.child('Data/light').get().val()
#     spray_status = database.child('Data/spray').get().val()

#     # Xử lý yêu cầu bật/tắt đèn từ người dùng
#     if request.method == 'POST':
#         action = request.POST.get('action', '')
#         if action == 'on':
#             database.child('Data/light').set(1)
#         elif action == 'off':
#             database.child('Data/light').set(0)
    

#     # Lắng nghe sự thay đổi trên Firebase và cập nhật giao diện tự động
#     def stream_handler(message):
#         data = json.loads(json.dumps(message))
#         light_status = data['data']

#     stream = database.child('Data/light').stream(stream_handler)

#     return render(request, 'index2.html', {'light_status': light_status})

# def control_sprays(request):
#     # Kết nối đến Firebase Realtime Database
#     database = firebase.database()

#     # Đọc trạng thái đèn từ Firebase
#     light_status = database.child('Data/spray').get().val()

#     # Xử lý yêu cầu bật/tắt đèn từ người dùng
#     if request.method == 'POST':
#         action = request.POST.get('action', '')
#         if action == 'on':
#             database.child('Data/spray').set(1)
#         elif action == 'off':
#             database.child('Data/spray').set(0)

#     # Lắng nghe sự thay đổi trên Firebase và cập nhật giao diện tự động
#     def stream_handler(message):
#         data = json.loads(json.dumps(message))
#         light_status = data['data']

#     stream = database.child('Data/spray').stream(stream_handler)

#     return render(request, 'index2.html', {'spray_status': light_status})


def control_lights_and_watering(request):
    # Đọc trạng thái đèn và tưới cây từ Firebase
    light_status = database.child('Data/light').get().val()
    watering_status = database.child('Data/watering').get().val()

    if request.method == 'POST':
        action = request.POST.get('action', '')

        if action == 'light_on':
            database.child('Data/light').set(1)
        elif action == 'light_off':
            database.child('Data/light').set(0)
        elif action == 'watering_start':
            database.child('Data/watering').set(1)
        elif action == 'watering_stop':
            database.child('Data/watering').set(0)

    # Lắng nghe sự thay đổi trên Firebase và cập nhật giao diện tự động
    def stream_handler(message):
        data = json.loads(json.dumps(message))
        if data['path'] == '/Data/light':
            light_status = data['data']
        elif data['path'] == '/Data/watering':
            watering_status = data['data']

    stream = database.child('Data').stream(stream_handler)

    return render(request, 'index2.html', {'light_status': light_status, 'watering_status': watering_status})