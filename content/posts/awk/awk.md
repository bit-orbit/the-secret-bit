---
title: "awk"
date: 2022-03-22T16:57:04+04:30
draft: true
---



<div dir='rtl'>

### فهرست

> - [مقدمه](#مقدمه)
> - [چاپ تمامی محتویات فایل](#چاپ-تمامی-محتویات-فایل)
> - [فیلتر کردن فایل با الگوهای خاص](#فیلتر-کردن-فایل-با-الگوهای-خاص)
> - [جدا سازی خطوط با استفاده از فیلدها](#جدا-سازی-خطوط-با-استفاده-از-فیلدها)
> - [شمارش خطوط](#شمارش-خطوط)
> - [نمایش آخرین فیلد ها در هر خط](#نمایش-آخرین-فیلد-ها-در-هر-خط)
> - [نمایش تعداد خطوط](#نمایش-تعداد-خطوط)
> - [Author or Authors](#author-or-authors)
</div>




---
<div dir='rtl'>

### مقدمه
AWK یک زبان برنامه نویسی با کاربرد خاص برای پردازش و استخراج متن است. در سال ۱۹۷۷ در آزمایشگاه‌های بل نوشته شد.
ابزار awk در واقع یک زبان برنامه نویسی است. awk نویسی به کاربر اجازه میدهد از متغیرها، توابع عددی ، توابع رشته ای و عملگرهای منطقی در برنامه های خود استفاده کند. هرچند از awk بیشتر برای فیلترکردن و پردازش فایلها استفاده میشود، اما در این حال شما میتوانید با این زبان برنامه نویسی برنامه های کوچک و مفیدی برای کارهای روزانه خود بنویسید.. 
</div>



---
<div dir='rtl'>

### چاپ تمامی محتویات فایل
اگر میخواهید که تمامی محتویات یک فایل برای شما چاپ شود از دستور awk و تابع ptint استفاده کنید. در این حالت تمامی محتویات فایل برای شما چاپ میشود.

</div>

    # view file with cat
    $ cat test.txt
    
    # OUTPUT
    # amirhosein sohrabi Linux
    # zahra moradi Windows
    # jadi mirmirani Linux
    # amirmohammad mosavi Kali-linux
      
    # view file with awk
    $ awk '{print}' test.txt  

    # OUTPUT
    # amirhosein sohrabi Linux
    # zahra moradi Windows
    # jadi mirmirani Linux
    # amirmohammad mosavi Kali-linux
      
      
---
<div dir='rtl'>

### فیلتر کردن فایل با الگوهای خاص
اگر میخواهید که با awk فایل را فیلتر کنید کافیست از علامت / قبل از تابع print استفاده کنید. اینگونه خطوطی که با الگوی داده شده شما مطابقت دارند برای شما چاپ خواهند شد.

</div>

    $ cat test.txt
    
    # OUTPUT
    # amirhosein sohrabi Linux
    # zahra moradi Windows
    # jadi mirmirani Linux
    # amirmohammad mosavi Kali-linux
      

    # file filter
    $ awk '/Linux/ {print}' test.txt 

    # OUTPUT
    # amirhosein sohrabi Linux
    # jadi mirmirani Linux


---
<div dir='rtl'>

### جدا سازی خطوط با استفاده از فیلدها
اگر میخواهید که فایل خود را با استفاده از فیلدها فیلتر کنید، از علامت $ در کنار تابع print استفاده کنید. awk فضاهای خالی را به عنوان جداکننده در نظر میگیرد و با استفاده از فضاهای خالی به جدا کردن خطوط میپردازد.

</div>

    
    $ cat test.txt
    
    # OUTPUT
    # amirhosein sohrabi Linux
    # zahra moradi Windows
    # jadi mirmirani Linux
    # amirmohammad mosavi Kali-linux
      
    $ awk '{print $2,$1}' test.txt

    # OUTPUT
    # sohrabi amirhosein
    # moradi zahra
    # mirmirani jadi
    # mosavi amirmohammad
 



---
<div dir='rtl'>

### شمارش خطوط
با استفاده از NR که یک متغیر داخلی است میتوانید خطوط را شمارش کنید. بعد از استفاده از این متغیر شماره خطوط برای شما چاپ خواهد شد.


</div>

    
    $ cat test.txt
    
    # OUTPUT
    # amirhosein sohrabi Linux
    # zahra moradi Windows
    # jadi mirmirani Linux
    # amirmohammad mosavi Kali-linux
      

    # display line number
    $ awk '{print NR,$0}' test.txt

    # OUTPUT
    # 1 amirhosein sohrabi Linux
    # 2 zahra moradi Windows
    # 3 jadi mirmirani Linux
    # 4 amirmohammad mosavi Kali-linux
      


---
<div dir='rtl'>

### نمایش آخرین فیلد ها در هر خط
با استفاده از NF میتوانید آخرین فیلدهای هر خط را مشاهده کنید.

</div>

    
    $ cat test.txt
    
    # OUTPUT
    # amirhosein sohrabi Linux
    # zahra moradi Windows
    # jadi mirmirani Linux
    # amirmohammad mosavi Kali-linux
      

    # display last field
    $ awk '{print $NF}' test.txt

    # OUTPUT
    # Linux
    # Windows
    # Linux
    # Kali-linux
      
      
---
<div dir='rtl'>

### نمایش تعداد خطوط
همانطور که میدانید با استفاده از NR میتوانستیم تعداد خطوط را شمارش کنیم، اما این سری فقط میخواهیم که تعداد خطوط را مشاهده کنیم. برای نمایش تعداد خطوط از دستور END در برنامه کوچک خود استفاده میکنیم. همانطور که میدانید بعد از استفاده از NR شماره تمامی خطوط به ترتیب چاپ میشود و ما برای فهمیدن تعداد خطوط به آخرین خط نگاه میکنیم، پس برای اینکه این مسئله گیج کننده نباشد از دستور END در برنامه کوچک خود استفاده میکنیم تافقط خط آخر برای ما چاپ شود.

</div>

    $ awk '{print NR}' test.txt
    
    # OUTPUT
    # 1
    # 2
    # 3
    # 4
    # 5

    $ awk 'END {print NR}' test.txt
    
    # OUTPUT
    # 5


---

### Author or Authors

- *[Amirhosein](https://github.com/amirhoseinsb)* | **<amirhoseinsohrabi.official@gmail.com>**
