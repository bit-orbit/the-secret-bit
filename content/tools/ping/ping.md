---
title: "Ping"
date: 2022-05-08T00:18:52+04:30
draft: true
tags: [
    "ping",
    "network",
    "check-network-connectivity",
    "command-line-utility",
]
---


<div dir='rtl'>

# فهرست

> - [مقدمه](#مقدمه)
> - [استفاده مرسوم](#استفاده-مرسوم)
> - [ساختار خروجی](#ساختار-خروجی)
> - [سوییچ ها](#سوییج-ها)
> - [محدود کردن تعداد پینگ](#محدود-کردن-تعداد-پینگ)
> - [تغییر فاصله زمانی بین هر پینگ](#تغییر-فاصله-زمانی-بین-هر-پینگ)
> - [تغییر سایز پکت](#تغییر-سایز-پکت)
> - [فلود کردن شبکه](#فلود-کردن-شبکه)
> - [پینگ زدن برای مدت زمان معلوم](#پینگ-زدن-برای-مدت-زمان-معلوم)
> - [نمایش مختصر نتیجه](#نمایش-مختصر-نتیجه)
> - [نمایش تایم استمپ در خروجی](#نمایش-تایم-استمپ-در-خروجی)
> - [کابرد مختصر و فشرده سوییچ ها](#کاربرد-مختصر-و-فشرده-سوییچ-ها)
> - [Author or Authors](#author-or-authors)
</div>


<div dir='rtl'>

# مقدمه

اگر جزو افرادی هستید که با شبکه و اینترنت سر و کار دارید احتمالا واژه پینگ و یا دستور پینگ به گوشتون خورده

دستور پینگ به مقصدی که بهش داده شده یه پکت از نوع 
ICMP
میفرسته و اگر ارتباط بر قرار بود جواب دریافت میکند.
ابزار ping به صورت پیشفرض در هر ثانیه یک پکت ICMP به مقصد تایین شده ارسال می‌‌کند،
هر پکت که ارسال می‌شود، این ابزار جمع زمان ارسال و دریافت جواب را باز می‌گرداند.
</div>

> ICMP: Internet Control Message Protocol

<div dir='rtl'>

# استفاده مرسوم
- تست اتصال سیستم به اینترنت (به اینترنت وصلم ام؟)
- چک انلاین بودن یک دستگاه از راه دور
- تحلیل و کشف مشکلات شبکه (گم شدن پکت ها و ...)
</div>

```
ping [option] [hostname] or [IP address]
```

```
$ ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=110 time=51.2 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=110 time=51.1 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=110 time=49.1 ms
64 bytes from 8.8.8.8: icmp_seq=4 ttl=110 time=55.3 ms
64 bytes from 8.8.8.8: icmp_seq=5 ttl=110 time=49.1 ms
64 bytes from 8.8.8.8: icmp_seq=6 ttl=110 time=49.7 ms
64 bytes from 8.8.8.8: icmp_seq=7 ttl=110 time=49.6 ms
^C
--- 8.8.8.8 ping statistics ---
7 packets transmitted, 7 received, 0% packet loss, time 6009ms
rtt min/avg/max/mdev = 47.351/49.138/50.270/1.056 ms
```

<div dir='rtl'>

در دستور بالا هر یک ثانیه یک پکت از نوع
ICMP
به 8.8.8.8
(Google DNS server)
ارسال میشود و خروجی زیر نشون دهنده اتصال ما به اینترنت و در دسترس بودن
DNS
گوگل هست.
</div>

---
<div dir='rtl'>

## ساختار خروجی
- مقصد (جایی که بهش پینگ میزنیم)
با 
`from 8.8.8.8`
نمایش داده میشود.  
- ترتیب و شمارش هر پکت با 
`icmp_seq=n`
نشون داده میشود. بعد از ارسال هر پکت این عدد هم اقزایش پیدا میکند.
- (TTL/Time To Live) 
به معنی مدت زمانی که یک بسته ی اطلاعاتی میتواند در شبکه باقی بماند و با 
`ttl=[1/255]`
نمایش داده میشود،‌ مقدار آن میتواند از 1 تا 255 باشه.  
- مقدار زمانی که به طول می انجامد تا یک پکت به مقصد رسیده و برگردد، با 
`time=51`
نشان داده میشود.
زمان نوشته شده بر حسب میلی ثانیه است.  
- تعداد کل پکت های ارسال شده به این شکل
`7 packets transmitted`
نمایش داده میشود.
- تعداد پکت ها دریافت شده به این شکل
`7 received`
نمایش داده میشود.
- پکت های گم شده و از دست رفته به این شکل
`0% packet loss`
نمایش داده میشود.
- `min/avg/max/mdev = 47.351/49.138/50.270/1.056 ms`  
به ترتیب از سمت چپ، `حداقل/میانگین/حداکثر/کل زمان صرف شده` را نمایش میدهد.  
برای مثال، حداقل زمانی که برای زدن یک پینگ صرف میشود در این نمومه
47.351
میلی ثانیه. 
</div>


<div dir='rtl'>

#  سوییج ها
</div>

<div dir='rtl'>

## محدود کردن تعداد پینگ
برای ارسال تعداد مشخص پکت به تعداد مشخص از سوییچ 
`c-`
استفاده میکنیم.
</div>


```
ping -c 2 google.com
PING google.com (142.250.180.46) 56(84) bytes of data.
64 bytes from mct01s14-in-f14.1e100.net (142.250.180.46): icmp_seq=1 ttl=109 time=46.1 ms
64 bytes from mct01s14-in-f14.1e100.net (142.250.180.46): icmp_seq=2 ttl=109 time=56.5 ms

--- google.com ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1002ms
rtt min/avg/max/mdev = 46.104/51.325/56.547/5.221 ms
```
---
<div dir='rtl'>

## تغییر فاصله زمانی بین هر پینگ
فاصله زمانی ببین ارسال هر پینگ است به صورت پیش فرض یک ثانیه است.
برای تغییر این فاصله زمانی از سوییچ 
`i-`
استفاده میکنیم.  

- برای تغییر فاصله زمانی به کمتر از 2 میلی میلی ثانیه نیاز به دسترسی روت است.
</div>

```
# ping -i 0.001 -c4 127.0.0.1
PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.025 ms
64 bytes from 127.0.0.1: icmp_seq=2 ttl=64 time=0.004 ms
64 bytes from 127.0.0.1: icmp_seq=3 ttl=64 time=0.003 ms
64 bytes from 127.0.0.1: icmp_seq=4 ttl=64 time=0.003 ms

--- 127.0.0.1 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3ms
rtt min/avg/max/mdev = 0.003/0.008/0.025/0.009 ms
```
<div dir='rtl'>

---
## تغییر سایز پکت
برای تغییر سایز پکت از سوییچ
‍`s-`
استفاده میکنیم.
</div>

```
$ ping -s 1000 -c 2 google.com
PING google.com (142.250.180.46) 1000(1028) bytes of data.
76 bytes from mct01s14-in-f14.1e100.net (142.250.180.46): icmp_seq=1 ttl=109 (truncated)
76 bytes from mct01s14-in-f14.1e100.net (142.250.180.46): icmp_seq=2 ttl=109 (truncated)

--- google.com ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1002ms
rtt min/avg/max/mdev = 56.441/58.586/60.731/2.145 ms
```
---
<div dir='rtl'>

## فلود کردن شبکه
برای فلود کردن از سوییچ
`f-`
استفاده میکنیم.  
- اغلب برای تست کارایی شبکه زیر لود سنگین و شلوغی به کار گرفته میشود.
- نیاز به دسترسی روت برای استفاده از این سوییچ هست.
</div>

```
# ping -f 192.168.1.1
PING 192.168.1.1 (192.168.1.1) 56(84) bytes of data.
.^C
--- 192.168.1.1 ping statistics ---
8149 packets transmitted, 8148 received, 0.0122714% packet loss, time 12429ms
rtt min/avg/max/mdev = 0.574/1.480/36.498/1.952 ms, pipe 3, ipg/ewma 1.525/2.463 ms
```
---
<div dir='rtl'>

## پینگ زدن برای مدت زمان معلوم
برای تعیین مدت زمان معلوم برای پینگ زدن از سوییچ
`w-`
استفاده میکنیم.  
برای مثال میخواهیم که بعد از 5 ثانیه پینگ زدن دستور متوقف بشود.
</div>

```
$ ping -w 5 google.com
PING google.com (142.250.185.46) 56(84) bytes of data.
64 bytes from mct01s19-in-f14.1e100.net (142.250.185.46): icmp_seq=1 ttl=49 time=52.4 ms
64 bytes from mct01s19-in-f14.1e100.net (142.250.185.46): icmp_seq=2 ttl=49 time=49.5 ms
64 bytes from mct01s19-in-f14.1e100.net (142.250.185.46): icmp_seq=3 ttl=49 time=56.0 ms
64 bytes from mct01s19-in-f14.1e100.net (142.250.185.46): icmp_seq=4 ttl=49 time=71.3 ms
64 bytes from mct01s19-in-f14.1e100.net (142.250.185.46): icmp_seq=5 ttl=49 time=54.1 ms

--- google.com ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4005ms
rtt min/avg/max/mdev = 49.519/56.661/71.275/7.613 ms
```

---
<div dir='rtl'>

## نمایش مختصر نتیجه
برای نمایش تنها،‌ نتیجه دستور از سوییچ
`q-`
استفاده میکنیم.
</div>
‍‍

```
ping -c 10 -q google.com
PING google.com (142.250.201.142) 56(84) bytes of data.

--- google.com ping statistics ---
10 packets transmitted, 10 received, 0% packet loss, time 9015ms
rtt min/avg/max/mdev = 47.053/50.301/55.083/2.054 ms
```
---
<div dir='rtl'>

## نمایش تایم استمپ در خروجی
برای نمایش تایم استمپ بعد از هر خط از دستور
`D-`
استفاده میکنیم.
</div>

```
$ ping -D -c2  google.com
PING google.com (142.250.201.142) 56(84) bytes of data.
[1651609773.320828] 64 bytes from mct01s21-in-f14.1e100.net (142.250.201.142): icmp_seq=1 ttl=104 time=49.9 ms
[1651609774.325814] 64 bytes from mct01s21-in-f14.1e100.net (142.250.201.142): icmp_seq=2 ttl=104 time=55.2 ms

--- google.com ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1001ms
rtt min/avg/max/mdev = 49.899/52.559/55.219/2.660 ms
```
---
## کاربرد مختصر و فشرده سوییچ ها
| سوییج         |          کارکرد     |
|---------------|------------------|
|       -a      | برای هر پینگ موفق بیپ |
|   -c --count  | محدود کردن تعداد پینگ |
|       -f      | فلود کردن شبکه| 
| -i --interval | قرار دادن وقفه مشخص بین هر پینگ   |
|  -l --preload | عدد را به عنوان پارامتر میگیرد و به تعداد آن، پکت پشت سر هم ارسال میکند بدون انتظار برای جواب  |
|       -A      | آداپتیو هست، و به اندازه تایم ارسال پکت قبلبی وققه ایجاد میکند برای پینگ بعدی |
|       -n      | نمایش ای پی به جای هاست نیم    |
|               |                            |

---
## Author or Authors

- *[Ahoora](https://github.com/ah00ra)* | **<ahoorchi@gmail.com>**
