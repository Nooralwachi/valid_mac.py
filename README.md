# valid_mac.py


Input: a file with the following content

Server MAC_Address Last_modified

s01 3D:A0:EA:A3:a7:91 07/31/2020

s02 CF:FD:D4:1C:C3:74 07/31/2020

s03 B7:75:A7:1D:4B:D2 07/31/2020

s04 57:6E:EF:FB:FF;8C 07/31/2020

s05 39:8FC0:47:7B:C1 07/31/2020

s06 2D:F6:OC:9E:4F:C2 07/31/2020

s07 EC:DD:B5:AE:E2:DA 07/31/2020

s08 21:129:CE:BE:CA:55 07/31/2020

s09 6E:3A:D0:DB:CA:97:99 07/31/2020

s10 03:5E:52:98:4B 07/31/2020
 
Output: valid servers and mac addresses

s02 CF:FD:D4:1C:C3:74

s03 B7:75:A7:1D:4B:D2

s07 EC:DD:B5:AE:E2:DA
 
Note:

1) For letters, we only allow uppercase 

2) It's ok to have leading zeros

3) For separator, we only allow colon
