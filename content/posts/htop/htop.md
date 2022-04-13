---
title: "htop"
date: 2022-04-07T00:02:56+04:30
draft: False
---

<div dir='rtl'>

### فهرست

- [فهرست](#فهرست)
- [مقدمه](#مقدمه)
- [مانیتور کردن پردازش ها](#مانیتور-کردن-پردازش-ها)
- [گرفتن خروجی از ابزار](#گرفتن-خروجی-از-ابزار)
- [کشتن پروسه ها با htop](#کشتن-پروسه-ها-با-htop)
- [جستجو به دنبال پروسه خاص](#جستجو-به-دنبال-پروسه-خاص)
- [نمایش پروسه ها به شکل درختی](#نمایش-پروسه-ها-به-شکل-درختی)
- [Author or Authors](#author-or-authors)
</div>

---
<div dir='rtl'>

### مقدمه
ابزار htop برای مدیریت پردازش های در حال اجرا به کار میرود، اگر میخواهید که پردازش های خود را ببینید آن ها را حذف کنید یا آن ها را مانیتور کنید از ابزار htop استفاده کنید. لازم به ذکر است بدانید که این ابزار در برخی از توزیع های لینوکسی به شکل پیشفرض نصب نیست و باید آن را با استفاده از پکیج منیجر نصب کنید.
</div>

---

<div dir='rtl'>

### مانیتور کردن پردازش ها

برای مانیتور کردن پردازش ها کافیست از دستور htop در خط فرمان استفاده کنید.
<p align = "center">
    <img src = "htop.png">
</p>
</div>

    # monitoring process with htop
    $ htop

    # OUTPUT
    #                                                                                    
    #  1  [                                                 0.0%]   Tasks: 141, 653 thr; 1 running
    #  2  [|||||||||||||||||||||||||||||||||||||||||||||||100.0%]   Load average: 1.01 0.81 0.94 
    #  Mem[||||||||||||||||||||||||||||||||||||||||||2.17G/2.92G]   Uptime: 01:36:53  
    #  Swp[||||                                       117M/1.86G]                     
    #    PID USER      PRI  NI  VIRT   RES   SHR S CPU% MEM%   TIME+  Command        
    #   9523 amirhosei  20   0 14124  4484  3156 R 109.  0.1  0:00.22 htop           
    #      1 root       20   0  164M  9584  6064 S  0.0  0.3  0:05.48 /sbin/init splash
    #    302 root       19  -1 72952 13184 11812 S  0.0  0.4  0:01.65 /lib/systemd/systemd-journald
    #    333 root       20   0 23664  4864  2724 S  0.0  0.2  0:02.70 /lib/systemd/systemd-udevd
    #    475 systemd-r  20   0 23888  8584  5216 S  0.0  0.3  0:00.40 /lib/systemd/systemd-resolved
    #    715 root       20   0  239M  9064  8148 S  0.0  0.3  0:00.20 /usr/lib/accountsservice/accounts-daemon
    #    792 root       20   0  239M  9064  8148 S  0.0  0.3  0:00.04 /usr/lib/accountsservice/accounts-daemon
    #    703 root       20   0  239M  9064  8148 S  0.0  0.3  0:00.35 /usr/lib/accountsservice/accounts-daemon
    #    704 root       20   0  2540   764   700 S  0.0  0.0  0:01.45 /usr/sbin/acpid 
    #    707 avahi      20   0  8520  3108  2816 S  0.0  0.1  0:00.20 avahi-daemon: running [P5PL2-E.local]
    #    708 root       20   0 12284  2848  2640 S  0.0  0.1  0:00.01 /usr/sbin/cron -f
    #    709 root       20   0 31416  7724  6212 S  0.0  0.3  0:00.04 /usr/sbin/cupsd -l
    #    710 messagebu  20   0  8840  5224  3552 S  0.0  0.2  0:02.54 /usr/bin/dbus-daemon --system --address=systemd: --nofork --n
    #    782 root       20   0  333M 15032 12144 S  0.0  0.5  0:00.09 /usr/sbin/NetworkManager --no-daemon
    #    794 root       20   0  333M 15032 12144 S  0.0  0.5  0:00.27 /usr/sbin/NetworkManager --no-daemon
    #    711 root       20   0  333M 15032 12144 S  0.0  0.5  0:06.41 /usr/sbin/NetworkManager --no-daemon
    #    755 root       20   0 81924  3496  3148 S  0.0  0.1  0:00.00 /usr/sbin/irqbalance --foreground
    #    721 root       20   0 81924  3496  3148 S  0.0  0.1  0:00.57 /usr/sbin/irqbalance --foreground
    #    726 root       20   0 42192 11780  8688 S  0.0  0.4  0:00.32 /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-t
    #    753 root       20   0  233M 11044  8176 S  0.0  0.4  0:00.00 /usr/lib/policykit-1/polkitd --no-debug
    #    793 root       20   0  233M 11044  8176 S  0.0  0.4  0:00.51 /usr/lib/policykit-1/polkitd --no-debug
    #    728 root       20   0  233M 11044  8176 S  0.0  0.4  0:01.93 /usr/lib/policykit-1/polkitd --no-debug
    #    779 syslog     20   0  219M  3776  2896 S  0.0  0.1  0:00.08 /usr/sbin/rsyslogd -n -iNONE
    #    780 syslog     20   0  219M  3776  2896 S  0.0  0.1  0:00.00 /usr/sbin/rsyslogd -n -iNONE
    #    781 syslog     20   0  219M  3776  2896 S  0.0  0.1  0:00.08 /usr/sbin/rsyslogd -n -iNONE
    #    730 syslog     20   0  219M  3776  2896 S  0.0  0.1  0:00.20 /usr/sbin/rsyslogd -n -iNONE
    #    737 root       20   0 16744  5644  4692 S  0.0  0.2  0:00.83 /lib/systemd/systemd-logind
    #    773 root       20   0  386M 12052  9268 S  0.0  0.4  0:00.00 /usr/lib/udisks2/udisksd
    #    795 root       20   0  386M 12052  9268 S  0.0  0.4  0:00.01 /usr/lib/udisks2/udisksd
    #    860 root       20   0  386M 12052  9268 S  0.0  0.4  0:00.00 /usr/lib/udisks2/udisksd
    #    893 root       20   0  386M 12052  9268 S  0.0  0.4  0:00.00 /usr/lib/udisks2/udisksd
    #    740 root       20   0  386M 12052  9268 S  0.0  0.4  0:03.45 /usr/lib/udisks2/udisksd
    #    741 root       20   0 13676  2488  1908 S  0.0  0.1  0:00.04 /sbin/wpa_supplicant -u -s -O /run/wpa_supplicant
    # 1Help  F2Setup F3SearchF4FilterF5Tree  F6SortByF7Nice -F8Nice +F9Kill  F10Quit 


---
<div dir='rtl'>

### گرفتن خروجی از ابزار
برای ذخیره کرده خروجی کافیست از ابزار echo و aha استفاده کنید.ابزار echo که به صورت پیشفرض در تمامی توزیع ها موجود هست، اما ابزار aha را باید جداگانه نصب کنید. که روش نصب هم در توزیع های مختلف به شما توزیح داده خواهد شد. اما لازم است بدانید که خروجی در نهایت html خواهد بود و باید ان را در یک فایل html ذخیره کنید. سپس برای نمایش خروجی مرورگر کروم یا فایر فاکس را باز کنید و با استفاده از کلید های ترکیبی ctrl + o وارد محل ذخیره فایل شوید . بعد از پیداکردن فایل دوبار روی فایل کلیک کنید تا خروجی را مشاهده کنید.
<p align = "center">
    <img src = "saveoutput.png">
</p>
</div>

    # step 1 
    # install the aha tool

    # install in debian
    $ apt install aha

    # install in fedora 
    $ yum install aha

    # install in arch
    $ pacman -S aha

    # step 2
    # Get output 

    $ echo q | htop | aha --black --line-fix > htop.html




---
<div dir='rtl'>

### کشتن پروسه ها با htop
برای کشتن پروسه ها ابتدا پروسه مورد نظر را انتخاب کرده و کلید F9 کیبورد را فشار دهید. حالا برای شما لیستی از سیگنال ها نمایش داده میشود، سیگنال شماره ۹ را انتخاب کنید. بدین ترتیب پروسه اجرا شده کشته میشود و از بین میرود.
<p align = "center">
    <img src = "kill.png">
</p>
</div>

    # step 1
    # select the process

    # step 2
    # select the F9 key

    # step 3 
    # select the 9 SIGKILL


---
<div dir='rtl'>

### جستجو به دنبال پروسه خاص

با استفاده از کلید F3 کیبورد میتوانید به دنبال پروسه های خاص بگردید، بعد از انتخاب کلید F3 نام پروسه مد نظر خود را تایپ کنید، در صورتی که پروسه ی مد نظر شما وجود داشته باشد به شما نمایش داده میشود و در غیر اینصورت چیزی به شما نمایش داده نخواهد شد.

</div>
    
    # step 1 
    # select the F3 Key

    # step 2
    # Type the process name


---
<div dir='rtl'>

### نمایش پروسه ها به شکل درختی
برای نمایش پروسه ها به شکل درختی از کلید F5 کیبورد استفاده کنید. در این حالت پروسه اجرا شده به همراه پروسه هایی که توسط آن پروسه اجرا شده است به شما نمایش داده خواهد شد.
<p align = "center">
    <img src = "treeView.png">
</p>
</div>
    
    
    # View Process tree
    $ select the F5 key


---

### Author or Authors

- *[Amirhosein](https://github.com/amirhoseinsb)* | **<amirhoseinsohrabi.official@gmail.com>**
