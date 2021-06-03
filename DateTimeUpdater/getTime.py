#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ntplib
import subprocess
import platform
import socket
from typing import Union
from time import gmtime, strftime

NTPServer = ["tick.stdtime.gov.tw", "time.stdtime.gov.tw", "pool.ntp.org", "time.windows.com"]


def _ping(host, parm, times, waittime_seconds) -> bool:
    """
    return False if ping timeout
    """

    HOST = host
    param = parm
    TIMES = times
    WAITTIME_seconds = waittime_seconds
    command = ["ping", param, TIMES, HOST]

    # use subprocess instead of os.sysstem to avoids shell injection
    # https://en.wikipedia.org/wiki/Code_injection#Shell_injection
    try:
        proc = subprocess.Popen(command, stdout=subprocess.PIPE)
        proc.wait(timeout=WAITTIME_seconds)

    except subprocess.TimeoutExpired:
        return False

    else:
        return True


def getNTP_Server_Time() -> Union[None, str]:
    """
    try and get NTP Server time , to show message when recognized.
    """

    # break for loop when get NTP time
    for ntpserver in NTPServer:
        try:
            c = ntplib.NTPClient()
            response = c.request(ntpserver)

        # get error if get addr information error
        except socket.gaierror as e:
            print(f"Maybe the NTPServer '{ntpserver}'is incorrect, timeout or shutdown.\n")
            if ntpserver == NTPServer[-1]:
                print(f"Error message is:\n{e}\n")
                messagebox = """------------------------------------
| Can't creat any socket connect.   |
| Maybe your Internet is disconnect.|
------------------------------------
                """
                print(f"{messagebox}")

                HOST = "8.8.8.8"
                param = "-n" if platform.system().lower() == "windows" else "-c"
                TIMES = "1"
                WAITTIME_seconds = 1
                ping_result = "success" if _ping(HOST, param, TIMES, WAITTIME_seconds) else "failed"
                print("ping test:")
                print(f"ping HOST: {HOST} {TIMES} times in {WAITTIME_seconds} seconds get {ping_result}\n")

        # get error if connectionerror or timeout
        except (ConnectionError, TimeoutError) as e:
            print(f"Maybe the NTPServer '{ntpserver}'is incorrect, timeout or shutdown.\n")
            # 如果NTP Serever全都不行，有可能是網路沒有連接
            if ntpserver == NTPServer[-1]:
                print(f"Error message is:\n{e}\n")
                messagebox = """------------------------------------
| Can't get any NTP Server Respone. |
| Maybe all NTP Server timeout.|
------------------------------------
                """
                print(f"{messagebox}")
        else:
            timeStamp = response.tx_time
            # 如果可以成功取得NTP時間，則離開迴圈，不再抓其他NTP時間
            return timeStamp
    return None


def getUTC_Timezone() -> str:
    """
    get User UTC TimeZone
    """
    TimeZone_str = strftime("%z", gmtime())
    return TimeZone_str
