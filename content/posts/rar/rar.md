---
title: "rar"
date: 2022-03-23T00:29:04+04:30
draft: false
---




<div dir='rtl'>

### فهرست

- [فهرست](#فهرست)
- [مقدمه](#مقدمه)
- [فشرده کردن فایل](#فشرده-کردن-فایل)
- [تعمیر فایل های فشرده](#تعمیر-فایل-های-فشرده)
- [اضافه کردن فایل های جدید به فایل فشرده شده](#اضافه-کردن-فایل-های-جدید-به-فایل-فشرده-شده)
- [ست کردن پسورد برای فایل فشرده](#ست-کردن-پسورد-برای-فایل-فشرده)
- [استخراج فایل](#استخراج-فایل)
- [Author or Authors](#author-or-authors)
</div>



---
<div dir='rtl'>

### مقدمه
یکی از ابزارهایی که با آن میتوانید فایل ها خود را با فرمت rar فشرده کنید ابزار rar است.
با سوییچ های مختلف این ابزار به جز فشرده سازی میتوانید عملیات غیر فشرده سازی را هم نیز انجام دهید.
</div>



---
<div dir='rtl'>

### فشرده کردن فایل
با استفاده از سوییچ a میتوانید فایل های خود را تبدیل به یک فایل فشرده کنید.

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

با استفاده از سوییچ u میتوانید فایلهای جدیدی را به فایل فشرده شده خود اضافه کنید.

</div>

    $ rar u test.rar fileadd.txt


---
<div dir='rtl'>

### ست کردن پسورد برای فایل فشرده
با استفاده از سوییچ p- میتوانید برای فایل های فشرده خود پسورد ست کنید.

</div>

    $ rar a -p amir.rar
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
با استفاده از سوییچ x میتوانید فایل های خود را از حالت فشرده خارج کنید.

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

### Author or Authors

- *[Amirhosein](https://github.com/amirhoseinsb)* | **<amirhoseinsohrabi.official@gmail.com>**
