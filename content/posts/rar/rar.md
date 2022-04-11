---
title: "rar"
date: 2022-03-23T00:29:04+04:30
draft: false
---




<div dir='rtl'>

### فهرست

> - [مقدمه](#مقدمه)
> - [فشرده کردن فایل](#فشرده-کردن-فایل)
> - [تعمیر فایل های فشرده](#تعمیر-فایل-های-فشرده)
> - [اضافه کردن فایل های جدید به فایل فشرده شده](#اضافه-کردن-فایل-های-جدید-به-فایل-فشرده-شده)
> - [ست کردن پسورد برای فایل فشرده](#ست-کردن-پسورد-برای-فایل-فشرده)
> - [استخراج فایل](#استخراج-فایل)
> - [Author or Authors](#author-or-authors)
</div>



---
<div dir='rtl'>

### مقدمه
یکی از ابزارهایی که با آن می‌توان فایلی را با فرمت rar فشرده و یا آرشیو کرد ابزار *rar* است.
با سوییچ های مختلف این ابزار به جز فشرده سازی می‌توان
فایل های
rar
را استخراج کرد.

> سوییچ های
> rar
> نیاز به پیشوند های - و - - ندارند

</div>



---
<div dir='rtl'>

### فشرده کردن فایل

سوییچ
a
برای فشرده سازی فایل استفاده می‌شود. اولین ارگومان این سوییچ نام فایل شما بعد از فشرده سازی است،
ارگومان هایی بعدی مسیر فایل هایی است که نیاز دارید فشرده شوند.

</div>
    
    $ rar a amir.rar amir.txt ali.txt
    
    # OUTPUT
    # Trial version             Type 'rar -?' for help
 
    # Evaluation copy. Please register.
    # 
    # Creating archive amir.rar
    # 
    # Adding    amir.txt                                                    OK 
    # Adding    ali.txt                                                     OK 
    # Done


---
<div dir='rtl'>

### تعمیر فایل های فشرده
با استفاده از سوییچ r میتوانید فایل فشرده خود را تعمیر کنید.
این سوییچ زمانی کاربرد دارد که فایل فشرده شما به مشکل خورده یا در هیچ حالتی نمیتوانید فایل را از حالت فشرده خارج کنید.
</div>

    $ rar r test.rar



---
<div dir='rtl'>

### اضافه کردن فایل های جدید به فایل فشرده شده

زمانی که شما فایلی هایی را فشرده کرده‌اید و بعد از گذشت زمان، مجدد نیاز دارید تا به فایل
فشرده قبلی چند فایل دیگر هم اضافه کنید
می‌توانید با استفاده از سوییچ
u
فایل فشرده قبلی را اپدیت کنید.

ارگومان اول این سوییچ مسیر فایل فشرده است، و ارگومان دوم مسیر فایل هایی است که باید به
فایل فشرده اضافه شوند.

</div>

    $ rar u test.rar fileadd.txt


---
<div dir='rtl'>

### ست کردن پسورد برای فایل فشرده
با استفاده از سوییچ p- میتوانید برای فایل های فشرده خود پسورد ست کنید.

</div>

    $ rar -p a amir.rar
    # Enter password (will not be echoed):
  
    # Reenter password:
    # *****
    # RAR 5.50   Copyright (c) 1993-2017 Alexander Roshal   11 Aug 2017
    # Shareware version         Type RAR -? for help
    # 
    # Evaluation copy. Please register.
    # 
    # Updating archive amir.rar


---
<div dir='rtl'>

### استخراج فایل 

برای استخراج فایل دو سوییچ e و x استفاده می‌شوند.
- سوییچ
x
مسیر کامل هر فایل را می‌سازد.

- سوییچ
e
هیچ پوشه‌ای برای فایل ها نمی‌سازد و تمامی فایل ها را دورن پوشه فعلی استخراج می‌کند.

</div>

    $ rar x amir.rar
    # RAR 5.50   Copyright (c) 1993-2017 Alexander Roshal   11 Aug 2017
    # Shareware version         Type RAR -? for help
    # 
    # Extracting from amir.rar
    # 
    # Creating    amir                                                   OK
    # Extracting  amir/index.php                                         OK
    # Extracting  amir/index.html                                        OK
    # Extracting  amir/xyz.txt                                           OK
    # Extracting  amir/abc.txt                                           OK

    # All OK



---
### بیشتر بدانید
لازم به ذکر است بدانید که ابزار [unrar](http://localhost:1313/the-secret-bit/posts/unrar/unrar/) هم برای استخراج فایل های فشرده کاربرد دارد.

---
### Author or Authors

- *[Amirhosein](https://github.com/amirhoseinsb)* | **<amirhoseinsohrabi.official@gmail.com>**
- *[Arya](https://github.com/shabane)* | **<m.mohamadshabane@gmail.com>**
