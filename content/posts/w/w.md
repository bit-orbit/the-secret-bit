---
title: "w"
date: 2022-04-04T02:25:13+04:30
draft: false
---



<div dir='rtl'>

### فهرست

- [فهرست](#فهرست)
- [مقدمه](#مقدمه)
- [](#)
- [](#-1)
- [](#-2)
- [](#-3)
- [](#-4)
- [](#-5)
- [Author or Authors](#author-or-authors)
</div>



---
<div dir='rtl'>

### مقدمه
برای اینکه بتوانید متوجه شوید که چه افرادی در سیستم وارد شده اند یا حضور دارند میتوانید از دستور w استفاده کنید. زمانی که از این دستور استفاده میکنید، تمامی افرادی که در سیستم حضور دارند به شما نمایش داده خواهد شد.

</div>


---
<div dir='rtl'>

### نمایش کاربرهای وارد شده در سیستم 

شما میتوانید با استفاده از دستور w تمامی کاربرهایی که در سیستم وارد شده اند را به همراه اطلاعاتی نظیر uptime ,systemtime , login time و .... را مشاهده کنید.

</div>
    
    $ w
    
    # OUTPUT
    # 02:32:22 up  8:43,  1 user,  load average: 1.21, 1.55, 1.45
    # USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
    # amirhose tty7     :0               17:53    8:40m 17:11   3.05s xfce4-session

   

---
<div dir='rtl'>

### نمایش اطلاعات به صورت خلاصه
شمامیتوانید با استفاده از سوییچ s- اطلاعات کاربرها را به صورت خلاصه مشاهده کنید.

</div>

    # w -s
    
    # OUTPUT
    # 02:43:17 up  8:54,  1 user,  load average: 0.69, 1.35, 1.43
    # USER     TTY      FROM              IDLE WHAT
    # amirhose tty7     :0                8:51m xfce4-session

   

---
<div dir='rtl'>

### نمایش بدون هدر
اگر میخواهید که اطلاعات بدون هدر ابتدایی برای شما چاپ شود از سوییچ h- استفاده کنید. با استفاده از این سوییچ فقط اطلاعات کاربرها چاپ میشود و خبری از هدر نیست.

</div>
    
    # w -h
    
    # OUTPUT
    # amirhose tty7     :0               17:53    8:54m 18:01   3.09s xfce4-session


---
<div dir='rtl'>

### مخفی کردن فیلد from
برخی از توزیع های لینوکسی هنگام خروجی ابزار فیلد from را مخفی میکنند.اما برخی دیگر از توزیع ها مانند مینت یا اوبونتو فیلد from را مخفی نمیکنند . برای مخفی کردن فیلد from از سوییچ f- استفاده کنید.

</div>

    # w -s

    # OUTPUT
    # 02:43:17 up  8:54,  1 user,  load average: 0.69, 1.35, 1.43
    # USER     TTY      FROM              IDLE WHAT
    # amirhose tty7     :0                8:51m xfce4-session
    
    # w -f
    # 02:43:35 up  8:54,  1 user,  load average: 0.69, 1.35, 1.43
    # USER     TTY                 IDLE WHAT
    # amirhose tty7                8:51m xfce4-session
    # OUTPUT
---
<div dir='rtl'>

### نمایش اطلاعات مربوط به یک کاربر خاص
شما میتوانید بعد از نوشتن دستور w و نام کاربر اطلاعات مربوط به یک کاربر خاص را مشاهده کنید.

</div>
    
    # w amirhosein
    
    # OUTPUT
    # 02:54:48 up  9:06,  1 user,  load average: 0.60, 0.89, 1.14
    # USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
    # amirhose tty7     :0               17:53    9:02m 18:21   3.12s xfce4-s

   

---
### Author or Authors

- *[Amirhosein](https://github.com/amirhoseinsb)* | **<amirhoseinsohrabi.official@gmail.com>**
