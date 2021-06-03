# DateTimeUpdater

DateTimeUpdater - Update your windows date and time via NTP Server.

## Download

Download the program [here](https://github.com/laudai/DateTimeUpdater/releases)

## How to use

Use the admin account and double click the program to update your windows date & time .

## How to build

1. install pyinstaller `pip install pyinstaller`
2. `$pyinstaller -F -c DateTimeUpdater\__main__.py -n DateTimeUpdater`

---

DateTimeUpdater - 透過網路與 NTP 伺服器取得時間，更新你的 Windows 本地日期與時間

## 下載

點擊[這裡](https://github.com/laudai/DateTimeUpdater/releases)下載

## 如何使用

雙擊程式，並使用管理員權限

## 如何自己打包

1. install pyinstaller `pip install pyinstaller`
2. `pyinstaller -F -c DateTimeUpdater\__main__.py -n DateTimeUpdater`

## 版本

- 0.2.0 : 新增檢查錯誤是由 timeout 或是 網路資訊錯誤，並發出一個 ICMP 封包測試。修正更新時間邏輯錯誤。
- 0.1.0 : 基本版本
