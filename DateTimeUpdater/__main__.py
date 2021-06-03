#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "laudai"
__version__ = "0.2.0"

if __name__ == "__main__":

    from DateTimeUpdater import getTime
    import os
    import time
    import ctypes

    UTC_Timezone_str = getTime.getUTC_Timezone()
    get_NTP_Server_Time_timeStamp_result = getTime.getNTP_Server_Time()
    if get_NTP_Server_Time_timeStamp_result:
        _date = time.strftime("%Y-%m-%d", time.localtime(get_NTP_Server_Time_timeStamp_result))
        _time = time.strftime("%X", time.localtime(get_NTP_Server_Time_timeStamp_result))
        print(f"Your UTC Timezone is {UTC_Timezone_str}\n")

        if os.name == "nt":
            # check admin
            print("Check admin to modified date & time.")
            if ctypes.windll.shell32.IsUserAnAdmin():
                print("You are admin\n")
                print("Update Your Date and Time to {} {}\n".format(_date, _time))
                os.system(f"date {_date} && time {_time}")
            else:
                print("You are not admin\nPls use root/administrator account.")
        else:
            print("Your OS is not windowds.")
    else:
        print("Can't set datetime to system\n")

    WAITTIME_seconds = 2
    # wait time to exit this consle
    for second in range(WAITTIME_seconds, 0, -1):
        print(f"\rscript will exit in {second} seconds.", end="")
        time.sleep(1)
