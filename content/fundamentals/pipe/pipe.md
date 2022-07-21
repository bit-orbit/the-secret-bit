---
title: "pipe"
date: 2022-07-18T15:18:37+04:30
draft: false
---
<div dir='rtl'>

### فهرست
> - [توضیحات](#توضیحات)
> - [مثال عملی](#مثال-عملی)
> - [نویسنده یا نویسندگان](/#نویسنده-یا-نویسندگان)

---

### توضیحات
در گنولینوکس یا سیستم عامل های یونیکس بیس شما میتوانید خروجی یک ابزار را با استفاده از ابزاری به نام پایپ به ابزار دیگر انتقال دهید. به شکل تخصصی تر در گنولینوکس ما سه مفهوم ورودی استاندارد خروجی استاندارد و ارور استاندارد رو داریم. زمانی که شما از علامت پایپ ‌| استفاده میکنید در واقع خروجی استاندارد را به ورودی استاندارد یک ابزار دیگر انتقال دادید. با استفاده از پایپ لاین میتوانید به راحتی خروجی را به یک ورودی استاندارد تحویل دهید، به شکل عمومی نام این کار فیلتر هست. در واقع زمانی که شما چند دستور را با استفاده از پایپ لاین به هم دیگر متصل کنید عملیات فیلتر را انجام دادید. در استفاده های روزانه ما از پایپ استفاده میکنیم. 
به عنوان مثال زمانی که میخواهید خروجی ابزار ls را مرتب سازی کنید از پایپ استفاده میکنید. به این شکل که با استفاده از ls لیستی از دایرکتوریها و فایل ها را با استفاده از پایپ به sort انتقال میدهیم و بدین ترتیب خروجی شما به شکل مرتب شده نمایش داده میشود.

### مثال عملی

#### مرتب سازی فایل با استفاده از انتقال خروجی cat به sort 

<div dir='ltr'>

    $ cat test.txt
    # amirhosein
    # sohrabi
    # gnulinux

    $ cat test.txt | sort
    # amirhosein
    # gnulinux
    # sohrabi

</div>

#### نمایش تعداد لاین های فایل به کمک wc

<div dir='ltr'>

    $ cat amir.txt
    # amirhosein
    # sohrabi
    # gnulinux
    # sohrabi
    # gnulinux


    $ cat amir.txt | wc -l
    # 6 
     

</div>

#### ترکیب چند دستور با هم برای پیدا کردن ابزار خاص

<div dir='ltr'>

    $ ls -l /bin/
    # -rwxr-xr-x 1 root root             96 Mar  8  2021 2to3-2.7
    # -rwxr-xr-x 1 root root             39 Aug  9  2019 7z
    # -rwxr-xr-x 1 root root             40 Aug  9  2019 7za
    # -rwxr-xr-x 1 root root             40 Aug  9  2019 7zr
    # -rwxr-xr-x 1 root root          31248 May 19  2020 aa-enabled
    # -rwxr-xr-x 1 root root          35344 May 19  2020 aa-exec
    # -rwxr-xr-x 1 root root          22912 Apr 14  2021 aconnect
    # -rwxr-xr-x 1 root root          19016 Nov 28  2019 acpi_listen

    $ ls -l /bin/ | grep zip
    # -rwxr-xr-x 1 root root          39144 Sep  5  2019 bunzip2
    # -rwxr-xr-x 1 root root          39144 Sep  5  2019 bzip2
    # -rwxr-xr-x 1 root root          18584 Sep  5  2019 bzip2recover
    # -rwxr-xr-x 1 root root          26776 Aug 16  2019 funzip
    # -rwxr-xr-x 1 root root           3516 Jan  6  2021 gpg-zip
    # -rwxr-xr-x 1 root root           2346 Dec 13  2019 gunzip
    # -rwxr-xr-x 1 root root          97496 Dec 13  2019 gzip
    # lrwxrwxrwx 1 root root              6 Jun 26 01:32 mzip -> mtools
    # -rwxr-xr-x 1 root root           4754 Aug  9  2019 p7zip
    # -rwxr-xr-x 1 root root           5656 Jul 22  2021 preunzip
    # -rwxr-xr-x 1 root root           5656 Jul 22  2021 prezip
    # -rwxr-xr-x 1 root root          14640 Jul 22  2021 prezip-bin
    # -rwxr-xr-x 1 root root         186664 Aug 16  2019 unzip
    # -rwxr-xr-x 1 root root          84248 Aug 16  2019 unzipsfx
    # -rwxr-xr-x 1 root root         216256 Apr 22  2017 zip
    # -rwxr-xr-x 1 root root          93816 Apr 22  2017 zipcloak
    # -rwxr-xr-x 1 root root          50718 Oct 19  2020 zipdetails
    # -rwxr-xr-x 1 root root           2953 Aug 16  2019 zipgrep
    # -rwxr-xr-x 1 root root         186664 Aug 16  2019 zipinfo
    # -rwxr-xr-x 1 root root          89488 Apr 22  2017 zipnote
    # -rwxr-xr-x 1 root root          93584 Apr 22  2017 zipsplit
      

</div>

### نویسنده یا نویسندگان

</div>

- *[Amirhosein](https://github.com/amirhoseinsb)* | **<amirhoseinsohrabi.official@gmail.com>**


