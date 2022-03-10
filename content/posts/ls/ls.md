---
title: "ls"
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
- [ترکیب سوییچ پرطرفدار ابزار](#ترکیب-سوییچ-پرطرفدار-ابزار)
- [Author or Authors](#author-or-authors)
</div>


---
<div dir='rtl'>

### مقدمه
ابزار ls برای لیست کردن دایرکتوری ها و فایلهای موجود در یک دایرکتوری به کار میرود .با استفاده از این ابزار و سوییچ های مفیدش میتوانید به سرعت فایلها و دایرکتوری های خود را پیدا کنید.
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
با استفاده از سوییچ t- در کنار دستور میتوانید فایلهایتان را بر اساس آخرین تغییرات مشاهده کنید. البته لازم به ذکر است بدانید که فایلی که جدید ترین تغییرات را داشته است در ابتدای خروجی نمایش داده میشود. اگر میخواهید که فایلی که جدیدترین تغییرات را داشته است را در انتهای خروجی ببینید از سوییچ ترکیب سوییچ tr- استفاده میکنید.
</div>

    $ ls -t
    # T1est.txt       Os.   txt          'import requests.py'
      Test.txt        number.   txt           tor-browser_en-US
      filejadid.txt   book
      test.txt       'Hacking Tools'
    
    $ ls -tr
    # 

---
<div dir='rtl'>

### نمایش به صورت خط به خط
با استفاده از سوییچ 1- میتوانید نتیجه را به صورت خط به خط مشاهده کنید.
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
با استفاده از سوییچ l- میتوانید تمامی اطلاعات مربوط به فایل ها یا دایرکتوری های موجود را مشاهده کنید. اطلاعاتی نظیر دسترسی ،آخرین ساعت تغییر،اسم و ....
زمانی که از سوییچ l- استفاده میکنید سایز فایل به شکل بایت برای شما نمایش داده میشود . اگر میخواهید که سایز فایل را به شکل خلاصه ببینید از ترکیب سوییچ lh- استفاده کنید.
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

    $ ls -lh
    # drwxr-xr-x 3 amirhosein amirhosein 4.0K Mar  6 19:30  book
      -rw-r--r-- 1 amirhosein amirhosein  181 Mar  9 03:24  filejadid.txt
      drwxr-xr-x 9 amirhosein amirhosein 4.0K Mar  4 02:24 'Hacking       Tools'                                                  
      -rw-r--r-- 1 amirhosein amirhosein  152 Mar  4 01:46 'import requests.py'
      -rw-r--r-- 1 amirhosein amirhosein   21 Mar  8 19:19  number.txt
      -rw-r--r-- 1 amirhosein amirhosein   44 Mar  8 19:20  Os.txt
      -rw-r--r-- 1 amirhosein amirhosein    0 Mar  9 20:34  T1est.txt
      -rw-r--r-- 1 amirhosein amirhosein   32 Mar 10 17:48  test.txt
      -rw-r--r-- 1 amirhosein amirhosein    0 Mar  9 20:34  Test.txt
      drwxr-xr-x 3 amirhosein amirhosein 4.0K Mar  1 21:16  tor-browser_en-US   
---
<div dir='rtl'>

### نمایش فایلهای مخفی
اگر فایلهایی دارید که مخفی هستند میتوانید با سوییچ a- به راحتی فایلهای مخفی را مشاهده کنید.
نکته ای که لازم به ذکر است بدانید این است که فایلهای مخفی سیستم در اول اسم آن ها نقطه به کار رفته است. در مثال زیر فایل های .amirhosein و .amirh.py جزو فایلهای مخفی این دایرکتوری هستند.
یک نکته ای هم که بد نیست بدانید این است که در تمامی دایرکتوری های سیستم دو دایرکتوری تک نقطه و دو نقطه که مخفی هستند با این سوییچ نمایش داده میشوند که کاربرد این ها هنگام استفاده از دستور cd است نمایش داده شدند. اما به هرحال آن ها را با دیگر دایرکتوری ها و فایلها اشتباه نگیرید.
</div>

    $ ls -a
    # .      filejadid.txt         number.txt   test.txt
      ..    'Hacking Tools'        Os.txt       Test.txt
      book  'import requests.py'   T1est.txt    tor-browser_en-US
      .amirhosein   .amirh.py
       
---

<div dir='rtl'>

### ترکیب سوییچ پرطرفدار ابزار
یکی از ترکیب سوییچ های پرطرفدار ابزار ls ترکیب سوییچ ltrh هست.
بد نیست بدانید که ترکیب بالا از ترکیب l- t- r- & h- به دست آمده است.
یعنی چه به شکل جداگانه بنویسید چه به شکل سرهم تفاوتی نخواهد داشت. این مورد سلیقه ای ست.
همچنین میتوانید دستور بالا را به شکل خلاصه شده یعنی ll نیز بنویسید.
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

### Author or Authors

- *[Amirhosein](https://github.com/amirhoseinsb)* | **<amirhoseinsohrabi.official@gmail.com>**

