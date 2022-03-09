---
title: "Ls"
date: 2022-03-09T20:52:30+03:30
draft: false
---

<div dir='rtl'>

### فهرست

- [فهرست](#فهرست)
- [مقدمه](#مقدمه)
- [لیست کردن فایلها و دایرکتوری ها](#لیست-کردن-فایلها-و-دایرکتوری-ها)
- [نمایش بر اساس آخرین تغییرات](#نمایش-بر-اساس-آخرین-تغییرات)
- [نمایش به صورت خط به خط](#نمایش-به-صورت-خط-به-خط)
- [نمایش تمامی اطلاعات مربوط به فایل و دایرکتوری](#نمایش-تمامی-اطلاعات-مربوط-به-فایل-و-دایرکتوری)
- [نمایش فایلهای مخفی](#نمایش-فایلهای-مخفی)
- [نمایش شماره فایلها](#نمایش-شماره-فایلها)
- [ترکیب سوییچ پرطرفدار ابزار](#ترکیب-سوییچ-پرطرفدار-ابزار)
- [Author or Authors:](#author-or-authors)
</div>


---
<div dir='rtl'>

### مقدمه
ابزار ls برای لیست کردن دایرکتوری ها و فایلهای موجود در یک دایرکتوری به کار میرود .با استفاده از این ابزار و سوییچ های مفیدش میتوانید به سرعتی فایلها و دایرکتوری های خود را پیدا کنید.
</div>


---
<div dir='rtl'>

### لیست کردن فایلها و دایرکتوری ها
با استفاده از دستور ls به تنهایی میتوانید تمامی دایرکتوری ها و فایلهای موجود در یک دایرکتوری را لیست کنید.
</div>

    $ ls
    # book                  number.txt   Test.txt
      filejadid.txt         Os.txt              tor-browser_en-US
      Hacking Tools'        T1est.txt
      import requests.py'   test.txt
                                

---
<div dir='rtl'>

### نمایش بر اساس آخرین تغییرات
با استفاده از سوییچ -t در کنار دستور میتوانید فایلهایتان را بر اساس آخرین تغییرات مشاهده کنید.
</div>

    $ ls -t
    # T1est.txt       Os.   txt          'import requests.py'
      Test.txt        number.   txt           tor-browser_en-US
      filejadid.txt   book
      test.txt       'Hacking Tools'
    

---
<div dir='rtl'>

### نمایش به صورت خط به خط
با استفاده از سوییچ -1 میتوانید نتیجه را به صورت خط به خط مشاهده کنید.
</div>

    $ ls -1
    # book
      filejadid.txt
      'Hacking Tools'
      'import requests.py'
      number.txt
      Os.txt
      T1est.txt
      test.txt
      Test.txt
      tor-browser_en-US
      

---
<div dir='rtl'>

### نمایش تمامی اطلاعات مربوط به فایل و دایرکتوری
با استفاده از سوییچ -l میتوانید تمامی اطلاعات مربوط به فایل ها یا دایرکتوری های موجود را مشاهده کنید. اطلاعاتی نظیر دسترسی آخرین ساعت تغییر اسم و ....
برای درک بهتر موضوع به دو دستور زیر دقت کنید.
</div>

    $ ls
    # book                  number.txt   Test.txt
      filejadid.txt         Os.txt              tor-browser_en-US
      Hacking Tools'        T1est.txt
      import requests.py'   test.txt

    $ ls -l
    # drwxr-xr-x 3 amirhosein amirhosein 4096 Mar  6 19:30  book
      -rw-r--r-- 1 amirhosein amirhosein  181 Mar  9 03:24  filejadid.txt
      drwxr-xr-x 9 amirhosein amirhosein 4096 Mar  4 02:24 'Hacking       Tools'                                                      
      -rw-r--r-- 1 amirhosein amirhosein  152 Mar  4 01:46 'import requests.py'
      -rw-r--r-- 1 amirhosein amirhosein   21 Mar  8 19:19  number.txt
      -rw-r--r-- 1 amirhosein amirhosein   44 Mar  8 19:20  Os.txt
      -rw-r--r-- 1 amirhosein amirhosein    0 Mar  9 20:34  T1est.txt
      -rw-r--r-- 1 amirhosein amirhosein  136 Mar  9 03:22  test.txt
      -rw-r--r-- 1 amirhosein amirhosein    0 Mar  9 20:34  Test.txt
      drwxr-xr-x 3 amirhosein amirhosein 4096 Mar  1 21:16  tor-browser_en-US  

---
<div dir='rtl'>

### نمایش فایلهای مخفی
اگر فایلهایی دارید که مخفی هستند میتوانید با سوییچ -a به راحتی فایلهای مخفی را مشاهده کنید.
که در مثال زیر دایرکتوری های تک نقطه و دو نقطه که مخفی بودند نمایش داده شدند.
این دو دایرکتوری زمانی که با دستور cd کار میکنید کار میکنند.
</div>

    $ ls -a
    # .      filejadid.txt         number.txt   test.txt
      ..    'Hacking Tools'        Os.txt       Test.txt
      book  'import requests.py'   T1est.txt    tor-browser_en-US
       
---
<div dir='rtl'>

### نمایش شماره فایلها
گاهی اوقات ممکن است برای نگهداری فایلهای مهم شماره آن فایل را بدانید . برای نمایش شماره فایل از سوییچ -i استفاده کنید.
</div>

    $ ls -i
    # 4338739  book                       4228488  Os.txt
      4195792  filejadid.txt              4196447  T1est.txt
      4328908 'Hacking Tools'             4197160  test.txt
      4213606 'import requests.py'        4197384  Test.txt
      4228373  number.txt                 4329791  tor-browser_en-US
             

---

<div dir='rtl'>

### ترکیب سوییچ پرطرفدار ابزار
یکی از ترکیب سوییچ های پرطرفدار ابزار ls ترکیب سوییچ ltrh هست.
با استفاده از این سوییچ میتوانید اطلاعات کامل راجب فایلها و دایرکتوری های موجود به دست بیاورید. آن ها را به ترتیب ببینید سایز آن ها را به شکل خلاصه ببینید و همچنین آخرین زمان دسترسی را مشاهده کنید.
برای درک بهتر این ترکیب سوییچ به دو دستور زیر توجه کنید.
</div>


    $ ls
    # book                  number  txt   Test.txt
      filejadid.txt         Os.txt              tor-browser_en-US
      Hacking Tools'        T1est.txt
      import requests.py'   test.txt

    $ ls -ltrh
    # drwxr-xr-x 3 amirhosein amirhosein 4.0K Mar  1 21:16  tor-browser_en-US                                                   
      -rw-r--r-- 1 amirhosein amirhosein  152 Mar  4 01:46 'import requests.py'
      drwxr-xr-x 9 amirhosein amirhosein 4.0K Mar  4 02:24 'Hacking       Tools'                                                      
      drwxr-xr-x 3 amirhosein amirhosein 4.0K Mar  6 19:30  book
      -rw-r--r-- 1 amirhosein amirhosein   21 Mar  8 19:19  number.txt
      -rw-r--r-- 1 amirhosein amirhosein   44 Mar  8 19:20  Os.txt
      -rw-r--r-- 1 amirhosein amirhosein  136 Mar  9 03:22  test.txt
      -rw-r--r-- 1 amirhosein amirhosein  181 Mar  9 03:24  filejadid.txt
      -rw-r--r-- 1 amirhosein amirhosein    0 Mar  9 20:34  Test.txt
      -rw-r--r-- 1 amirhosein amirhosein    0 Mar  9 20:34  T1est.txt
      

---

### Author or Authors:

- *[Amirhosein](https://github.com/amirhoseinsb)* | **<amirhoseinsohrabi.official@gmail.com>**

