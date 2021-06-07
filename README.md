# Cowin otp tracker

Auto book covin tag and auto get otp as well. Got tired of the cowin site and ended up having to setup a webserver to ping otp to and do my own stuff

If you need auto otp handling

- Install Tasker and RESTask
- get [task from tasker](https://taskernet.com/shares/?user=AS35m8kGOKLfQOdq0LBwXRFVKzso57%2FDIJnjWlsrzFOAEWwK3vyQYcFuhSrzEANBzXBAIiqANg%3D%3D&id=Task%3ASend+CoWIN+Otp)
- connect it to the [event from tasker](https://taskernet.com/shares/?user=AS35m8kGOKLfQOdq0LBwXRFVKzso57%2FDIJnjWlsrzFOAEWwK3vyQYcFuhSrzEANBzXBAIiqANg%3D%3D&id=Profile%3AReceived+Sms)
- change mobile number in restask to your own number

- in covin_wrapper.py - change PIN to the pincodes you need (hospitals to look for, only add the pins you would like to book)
- in vaccine-booking-details.json - change pincodes and your own codes. Alternatively, delete the file and run covin.py to generate the file again.
- run covin_wrapper.py it should keep searching for pins, if it finds one, it should beep and start to book the slot

