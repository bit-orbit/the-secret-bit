---
title: "ping"
date: 2022-05-08T00:18:52+04:30
draft: False
tags: [
    "ping",
    "network",
    "check-network-connectivity",
    "command-line-utility",
]
---


<div dir='rtl'>

### فهرست

> - [مقدمه](#مقدمه)
> - [استفاده مرسوم](#استفاده-مرسوم)
> - [ساختار خروجی](#ساختار-خروجی)
> - [سوییچ ها](#سوییج-ها)
> - [محدود کردن تعداد پینگ](#محدود-کردن-تعداد-پینگ)
> - [تغییر فاصله زمانی بین هر پینگ](#تغییر-فاصله-زمانی-بین-هر-پینگ)
> - [تغییر سایز پکت](#تغییر-سایز-پکت)
> - [فلود کردن شبکه](#فلود-کردن-شبکه)
> - [ارسال پکت برای مدت زمان معلوم](#ارسال-پکت-برای-مدت-زمان-مشخص)
> - [نمایش مختصر نتیجه](#نمایش-مختصر-نتیجه)
> - [کابرد مختصر و فشرده سوییچ ها](#کاربرد-مختصر-و-فشرده-سوییچ-ها)
> - [Author or Authors](#author-or-authors)
</div>

---

<div dir='rtl'>

### مقدمه
اگر از دسته افرادی هستید که در زمینه شبکه یا عیب یابی شبکه یا مواردی از این قبیل فعالیت کارکرده باشید، ابزار ping برای شما غریب نخواهد بود.
با استفاده از ابزار ping میتوانید پکتهایی از نوع icmp را به مقصدی خاص ارسال کنید. هنگام استفاده از ping کامپیوتر شما پکتهایی از نوع icmp را به آدرس مقصد ارسال کرده و منتظر پاسخ می‌ماند. زمانی که پاسخ را دریافت کند،
 زمان سپری شده‌ی این رفت و برگشت را به شما نمایش می‌دهد،
 یا در صورت عدم دریافت پاسخ به شما می‌گوید که پاسخی دریافت نکرده است.

</div>

> ICMP: Internet Control Message Protocol
---

<div dir='rtl'>

### بررسی در دسترس بودن یا نبودن یک سرور

برای بررسی در دسترس بودن یا نبودن یک سرور میتوانید از ping و آی پی یا نام دامنه آن سرور یا سایت استفاده کنید.
در حالت زیر ما با استفاده از ping و آی پی 8.8.8.8 بررسی کردیم که آیا سرور 8.8.8.8 در دسترس هست یا خیر، که در خروجی میبینید که پکت ها با موفقیت به سمت سرور ارسال شده و شما اطلاعاتی را راجب به هرپکت مشاهده میکنید.

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


---
<div dir='rtl'>

### توضیحات خروجی ابزار
- مقصد یا جایی که به سمت آن درخواست icmp ارسال کردید
با
`from 8.8.8.8`
نمایش داده می شود.  
- ترتیب و شمارش هر پکت با 
`icmp_seq=n`
نشان داده می شود. بعد از ارسال هر پکت این عدد هم افزایش پیدا می کند.
- (TTL/Time To Live) 
به معنی مدت زمانی است که یک پکت icmp می تواند در شبکه باقی بماند و با 
`ttl=[1/255]`
نمایش داده می شود،‌ مقدار آن می توانید از 1 تا 255 باشد. 

اما درواقع
ttl
برای هدف دیگری استفاده می‌شود. هر بار که پکت شما از یک
hop(هر نودی که پکت از آن عبورداده می‌شود مثل سوییچ یا روتر)
عبور کند، یک مقدار از عدد
ttl
درون پکت کم می‌شود.

- مقدار زمانی که به طول می انجامد تا یک پکت به مقصد رسیده و برگردد، با 
`time=51`
نشان داده می شود.
زمان نوشته شده بر حسب میلی ثانیه است.  
- تعداد کل پکت های ارسال شده به این شکل
`7 packets transmitted`
نمایش داده می شود.
- تعداد پکت ها دریافت شده به این شکل
`7 received`
نمایش داده می شود.
- پکت های گم شده و از دست رفته به این شکل
`0% packet loss`
نمایش داده می شود.
- `min/avg/max/mdev = 47.351/49.138/50.270/1.056 ms`  
به ترتیب از سمت چپ، `حداقل/میانگین/حداکثر/کل زمان صرف شده` را نمایش می دهد.  
برای مثال، حداقل زمانی که برای زدن یک پینگ صرف می شود در این نمونه
47.351
میلی ثانیه. 
</div>

---

<div dir='rtl'>

### محدود کردن تعداد پینگ
برای ارسال تعداد پکت به تعداد مشخص از سوییچ 
`c-`
استفاده می کنیم.
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

### تغییر فاصله زمانی بین هر پینگ
فاصله زمانی ببین ارسال هر پینگ به صورت پیش فرض یک ثانیه است.
برای تغییر این فاصله زمانی از سوییچ 
`i-`
استفاده می کنیم.  

- برای تغییر فاصله زمانی به کمتر از 2 میلی ثانیه نیاز به دسترسی روت است.
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
### تغییر سایز پکت
برای تغییر سایز پکت از سوییچ
‍`s-`
استفاده می کنیم.
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

### فلود کردن شبکه
برای فلود کردن از سوییچ
`f-`
استفاده می کنیم.  
- اغلب برای تست کارایی شبکه زیر لود سنگین و شلوغی به کار گرفته می شود.
- برای استفاده از این سوییچ نیاز به دسترسی روت است.
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

### ارسال پکت در مدت زمان مشخص
با استفاده از سوییچ w- میتوانیم محدوده زمانی مشخصی را برای ارسال پکت های icmp مشخص کنیم. به عنوان مثال در خروجی زیر مشاهده میکنید که بعد از ۵ ثانیه ارسال پکت ارسال درخواست متوقف شود.
یعنی در واقع ارسال پکت های icmp را به مدت زمان مشخصی محدود کردیم.
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

### نمایش مختصر نتیجه
برای نمایش خروجی به شکل خلاصه از سوییچ
`q-`
استفاده می کنیم.
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

### کاربرد مختصر و فشرده سوییچ ها

در جدول زیر شما میتوانید راجع به کاربرد سوییچ های ابزار اطلاعات بیشتری کسب کنید.

</div> 

| سوییج         |          کارکرد      |
|:---------------:|:------------------:|
|       -a        |  برای هر پینگ موفق بیپ می کند |
|   -c --count    | محدود کردن تعداد پینگ           |
|       -f        | فلود کردن شبکه                  | 
| -i --interval   | قرار دادن وقفه مشخص بین هر پینگ   |
|  -l --preload   | عدد را به عنوان پارامتر میگیرد و به تعداد آن، پشت سر هم پکت ارسال می کند بدون انتظار برای گرفتن پاسخ  |
|       -A        | آداپتیو هست، و به اندازه تایم ارسال پکت قبلبی وققه ایجاد می کند برای پینگ بعدی |
|       -n        | نمایش آی پی به جای هاست نیم    |

---
### Author or Authors

- *[Ahoora](https://github.com/ah00ra)* | **<ahoorchi@gmail.com>**
- *[Amir hosein sohrabi](github.com/amirhoseinsb)* | **<amirhoseinsohrabi.official@gmail.com>**
- *[Arya Shabane](github.com/shabane)* | **<m.mohamadshabane@gmail.com>**
