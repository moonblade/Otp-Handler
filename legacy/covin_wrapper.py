from hashlib import sha256
import sys,os,time
import requests,json

import datetime
import requests

WARNING_BEEP_DURATION = (1000, 1500)
PINS = ["111111111"]
mobile = "111111111"


try:
    import winsound

except ImportError:
    import os

    if sys.platform == "darwin":

        def beep(freq, duration):
            # brew install SoX --> install SOund eXchange universal sound sample translator on mac
            os.system(
                f"play -n synth {duration/1000} sin {freq} >/dev/null 2>&1")
    else:

        def beep(freq, duration):
            # apt-get install beep  --> install beep package on linux distros before running
            os.system('beep -f %s -l %s' % (freq, duration))

else:
    def beep(freq, duration):
        winsound.Beep(freq, duration)


main_url = "https://cdn-api.co-vin.in/api/v2/appointment/schedule"
beneficiaries_url = "https://cdn-api.co-vin.in/api/v2/appointment/beneficiaries"
otp_url = "https://cdn-api.co-vin.in/api/v2/auth/public/generateOTP"
val_otp_url = "https://cdn-api.co-vin.in/api/v2/auth/public/confirmOTP"
statusOK = 200
cal_url_pin = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}"
cal_url_dist = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={0}&date={1}"
# cal_url_cent = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByCenter?center_id={0}&date={1}"
flag = False
def checkAvailability():
        base = datetime.datetime.today()
        # date_list = [base + datetime.timedelta(days=x) for x in range(2)]
        date_list = [base + datetime.timedelta(days=x) for x in range(10)]
        date_str = [x.strftime("%d-%m-%Y") for x in date_list]
        pin_code = PINS
        age = 40
        # print (date_str)
        district_id = 305
        center_id = 603445

        statusOK = 200
        for d in date_str:
            for p in pin_code:
                URL = cal_url_pin.format(p, d)
                # URL = cal_url_cent.format(center_id,d)
                #  URL = cal_url_dist.format(district_id,d)
                response = requests.get(url = URL, headers = {'Host': 'cdn-api.co-vin.in','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51'})
                # print(URL)
                if response.status_code == statusOK:
                    print(json.dumps(response.json(), indent = 1))
                    flag = False
                    if response.json()["centers"]:
                        print("Available on: {}".format(d))
                        for center in response.json()["centers"]:
                            for session in center["sessions"]:
                                if session["min_age_limit"] <= age and session["available_capacity_dose1"]>0:
                                    print("\t", center["name"])
                                    print("\t", center["block_name"])
                                    print("\t Price: ", center["fee_type"])
                                    print("\t Available Capacity: ", session["available_capacity_dose1"])
                                    print("HHHHHEEEERRRREEEEEEEEEEEE")
                                    beep(WARNING_BEEP_DURATION[0],WARNING_BEEP_DURATION[1])
                                    if(session["vaccine"] != ''):
                                            print("\t Vaccine: ", session["vaccine"])
                                    os.system("python3 covin.py --mobile="+mobile+" --auto")
                                    print("\n\n")
                    else:
                            print("No centers")
                else:
                    print(response.status_code)
                    # sleep(1)
                    flag = True
                    time.sleep(50)
                    return;

while(1):
        checkAvailability()
        time.sleep(5)
        if(flag):
                flag = False

