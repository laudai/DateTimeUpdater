#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import ntplib
from time import gmtime, strftime

NTPServer = ["tick.stdtime.gov.tw", "time.stdtime.gov.tw",
             "pool.ntp.org", "time.windows.com"]

# PEP 484 -- Type Hints


def getNTP_Server_Time() -> str:
    """
    try and get NTP Server time , to show message when recognized
    """
    for ntpserver in NTPServer:
        try:
            c = ntplib.NTPClient()
            response = c.request(ntpserver)
            # break for loop when get NTP time

        except Exception as e:
            print(e)
            print("Maybe the NTPServer '{}'is incorrect , timeout or shutdown.\n".format(
                ntpserver))
            # 如果NTP Serever全都不行，有可能是網路沒有連接
            if ntpserver == NTPServer[-1]:
                print(
                    "Can't get any NTP Server Respone.\nMaybe your Internet is disconnect.")
                return None
        else:
            timeStamp = response.tx_time
            # 如果可以成功取得NTP時間，則離開迴圈，不再抓其他NTP時間
            break
    return timeStamp


def getUTC_Timezone() -> str:
    """
    get User UTC TimeZone
    """
    TimeZone_str = strftime("%z", gmtime())
    return TimeZone_str
