import requests


def send_otp(otp):
    print('otp password')
    print(otp.password)

    body = {'receptor': otp.phone, 'token': otp.password, 'template': 'verify'}
    sms_res = requests.get(
        'https://api.kavenegar.com/v1/467066542F7547496B7A2F34516745504D7173656E4934762F6F6243726B565A476F556B764D597A6F736F3D/verify/lookup.json',
        params=body)
