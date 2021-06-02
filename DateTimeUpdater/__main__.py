#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "laudai"
__version__ = "0.1.0"

if __name__ == "__main__":

    from DateTimeUpdater import getTime
    import os
    import time
    import ctypes

    UTC_Timezone_str = getTime.getUTC_Timezone()
    NTP_Server_Time_timeStamp_str = getTime.getNTP_Server_Time()
    _date = time.strftime("%Y-%m-%d", time.localtime(NTP_Server_Time_timeStamp_str))
    _time = time.strftime("%X", time.localtime(NTP_Server_Time_timeStamp_str))
    print("Your UTC Timezone is {}\n".format(UTC_Timezone_str))

    try:
        if os.name == "nt":
            # check admin
            if ctypes.windll.shell32.IsUserAnAdmin() == True:
                print("You are admin")
                print("Update Your Date and Time to {} {}\n".format(_date, _time))
                os.system("date {} && time {}".format(_date, _time))
            else:
                print("You are not admin\nPls use root/administrator account.")
        else:
            print("Your OS is not windowds.")
    except:
        pass
    finally:
        # wait the consle
        time.sleep(1)
