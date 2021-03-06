---
title: "w"
date: 2022-04-04T02:25:13+04:30
draft: false
---



<div dir='rtl'>

### فهرست

> - [مقدمه](#مقدمه)
> - [نمایش کاربرهای وارد شده در سیستم](#نمایش-کاربرهای-وارد-شده-در-سیستم)
> - [نمایش اطلاعات به صورت خلاصه](#نمایش-اطلاعات-به-صورت-خلاصه)
> - [نمایش بدون هدر](#نمایش-بدون-هدر)
> - [مخفی کردن فیلد from](#مخفی-کردن-فیلد-from)
> - [نمایش اطلاعات مربوط به یک کاربر خاص](#نمایش-اطلاعات-مربوط-به-یک-کاربر-خاص)
> - [Author or Authors](#author-or-authors)
</div>



---
<div dir='rtl'>

### مقدمه
برای اینکه متوجه شوید که چه یوزرهایی در سیستم لاگین هستند، میتوانید از دستور w استفاده کنید. زمانی که از این دستور استفاده میکنید، تمامی افرادی که در سیستم حضور دارند به شما نمایش داده خواهد شد.

</div>


---
<div dir='rtl'>

### نمایش کاربرهای وارد شده در سیستم 

</div>

<div dir = "rtl">
شما میتوانید با استفاده از دستور w تمامی کاربرهایی که در سیستم وارد شده اند را به همراه اطلاعاتی نظیر uptime ,systemtime , login time و .... را مشاهده کنید.
load average به زبان ساده بیانگر وضعیت لود سرور یا کامپیوتر میباشد . اعدادی که در load average مشاهده میکنید باید پایین تر از تعداد هسته های سی پی یو کامپیوتر یا سرور شما باشد، در غیر اینصورت بیانگر وضعیت بد سرور یا کامپیوتر شماست. هرچه عدد load average بالاتر باشد به این معنی است که فشار روی سرور و کامپیوتر شما بالاست. اما در load average سه عدد مشاهده میکنیم که هرکدام معنای خاصی دارند، عدد اول از سمت چپ بیانگر وضعیت لود در یک دقیقه ، عدد وسط بیانگر وصعیت لود در پنج دقیقه و عدد سوم بیانگر وضعیت لود در پانزده دقیقه است.
عدد نوشته شده در جلوی up بیانگر زمان بالا بودن سیستم است، که در مثال زیر مشاهده میکنید که سیستم من ۸ ساعت و ۴۳ دقیقه از زمان روشن شدنش میگذرد.
system time هم اولین نوشته در اولین خط خروجی است.
این عدد زمان حال سیستم را نشان میدهد که در مثال زیر ساعت 02:32:22 است.
اما توضیحات گفته شده مربوط به هدر بود، اطلاعات ارائه شده ابزار در خروجی به شرح زیر میباشد.
</div>

<div dir = "rtl">
User: کاربر یا کاربرانی که به سیستم لاگین کرده اند
</div>
<div dir = "rtl">
Tty: نحوه ورود کاربر به سیستم
</div>
<div dir = "rtl">
From: موقعیت ورود کاربر به سیستم
</div>
<div dir = "rtl">
Login@: زمان ورود کاربر به سیستم
</div>
<div dir = "rtl">
Idle: مدت غیرفعال بودن کاربر در سیستم
</div>
<div dir = "rtl">
JCPU: کل زمان مصرف CPU از زمان ورود توسط کاربر
</div>
<div dir = "rtl">
PCPU: زمان مصرف CPU برای فرآیند در حال اجرا
</div>
<div dir = "rtl">
What: فرآیند حال حاضر کاربر
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
