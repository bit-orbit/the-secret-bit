---
title: "file"
date: 2022-03-09T21:41:26+03:30
draft: false
---

<div dir='rtl'>

### فهرست

> - [مقدمه](#مقدمه)
> - [نمایش نوع فایل](#نمایش-نوع-فایل)
> - [نمایش نوع چند فایل به صورت همزمان](#نمایش-نوع-چند-فایل-به-صورت-همزمان)
> - [نمایش نوع تمامی فایلهای موجود در دایرکتوری](#نمایش-نوع-تمامی-فایلهای-موجود-در-دایرکتوری)
> - [نمایش محدوده خاصی از فایلها و دایرکتوری ها](#نمایش-محدوده-خاصی-از-فایلها-و-دایرکتوری-ها)
> - [حالت تعاملی ابزار](#حالت-تعاملی-ابزار)
> - [چاپ محتویات بدون فاصله اضافی](#چاپ-محتویات-بدون-فاصله-اضافی)
> - [Author or Authors](#author-or-authors)
</div>



---
<div dir='rtl'>

### مقدمه
از این ابزار برای نمایش نوع فایل ها استفاده میشود. برای مثال زمانی که با فایلی برخورد میکنید که پسوندی ندارد و اصلا نوع فایل مشخص نیست میتواند استفاده از این ابزار کاربردی باشد.
</div>



---
<div dir='rtl'>

### نمایش نوع فایل
برای نمایش نوع فایل از دستور file قبل از نام فایلتان استفاده کنید.به مثال زیر توجه کنید.
</div>

    $ file Os.txt 
    # Os.txt: ASCII text
    
    Or 

    $ file -b Os.txt
    # ASCII text



---
<div dir='rtl'>

### نمایش نوع چند فایل به صورت همزمان
برای نمایش نوع چند فایل به شکل همزمان میتوانید مسیر فایل موجود یا نام فایل موجود را با فاصله جدا کنید. به مثال زیر توجه کنید.
</div>

    $ file Os.txt DEB.jpg
    # Os.txt:  ASCII text
      DEB.jpg: JPEG image data, JFIF standard 1.02, resolution (DPI), density 72x72, segment       length 16, baseline, precision 8, 300x300, components 3



---
<div dir='rtl'>

### نمایش نوع تمامی فایلهای موجود در دایرکتوری
با استفاده از ستاره * میتوانید تمامی فایلهای موجود در دایرکتوری را اسکن کنید. به دستور زیر دقت کنید.

</div>

    $ file /home/amirhosein/Desktop/*
    # /home/amirhosein/Desktop/book:               directory
      /home/amirhosein/Desktop/DEB.jpg:            JPEG image data, JFIF standard 1.02,       resolution (DPI), density 72x72, segment length 16, baseline, precision 8, 300x300,       components 3
      /home/amirhosein/Desktop/filejadid.txt:      ASCII text
      /home/amirhosein/Desktop/Hacking Tools:      directory
      /home/amirhosein/Desktop/import requests.py: ASCII text
      /home/amirhosein/Desktop/number.txt:         ASCII text
      /home/amirhosein/Desktop/Os.txt:             ASCII text
      /home/amirhosein/Desktop/T1est.txt:          empty
      /home/amirhosein/Desktop/test.txt:           ASCII text
      /home/amirhosein/Desktop/Test.txt:           empty
      /home/amirhosein/Desktop/tor-browser_en-US:  directory
        


---
<div dir='rtl'>

### نمایش محدوده خاصی از فایلها و دایرکتوری ها
با استفاده از براکت میتوانید محدوده خاصی از کلمات را تعریف کنید. به دو مثال زیر توجه کنید.
</div>

    $ file /home/amirhosein/Desktop/*
    # /home/amirhosein/Desktop/book:               directory
      /home/amirhosein/Desktop/DEB.jpg:            JPEG image data, JFIF standard 1.02,       resolution (DPI), density 72x72, segment length 16, baseline, precision 8, 300x300,       components 3
      /home/amirhosein/Desktop/filejadid.txt:      ASCII text
      /home/amirhosein/Desktop/Hacking Tools:      directory
      /home/amirhosein/Desktop/import requests.py: ASCII text
      /home/amirhosein/Desktop/number.txt:         ASCII text
      /home/amirhosein/Desktop/Os.txt:             ASCII text
      /home/amirhosein/Desktop/T1est.txt:          empty
      /home/amirhosein/Desktop/test.txt:           ASCII text
      /home/amirhosein/Desktop/Test.txt:           empty
      /home/amirhosein/Desktop/tor-browser_en-US:  directory
        
    $ file /home/amirhosein/Desktop/[a-g]*
    # /home/amirhosein/Desktop/book:          directory
      /home/amirhosein/Desktop/filejadid.txt: ASCII text
                                                   


---
<div dir='rtl'>

### حالت تعاملی ابزار
برای استفاده از حالت تعاملی ما به سوییچی تحت عنوان f- نیاز داریم که برای نمایش فایلها استفاده میشود. سوییچ f- در واقع کارش خواندن مسیر فایلها از یک فایل دیگر است اما چون ما اینجا میخواهیم از حالت تعاملی استفاده کنیم با اضافه کردن - دش حالت تعاملی ابزار را اجرا میکنیم و زمانی که حالت تعاملی اجرا میشود به جای اینکه ابزار فایلی که مسیرها در آن قرار دارند را بخواند . مسیر فایلی که شما به ابزار میدهید را میخواند . لازم به ذکر است بدانید که این پروسه خواندن فایل تا ابد ادامه خواهد داشت . اگر خواستید که این پروسه را متوقف کنید از کلید ترکیبی ctrl+c استفاده کنید. برای درک بهتر به مثال زیر توجه فرمایید.
</div>

    $ cat test.txt
    # /home/amirhosein/Desktop/Os.txt
             
    $ file -f test.txt
    # /home/amirhosein/Desktop/Os.txt: ASCII text

    $ file -f -
    # Os.txt
      Os.txt:      ASCII text
      DEB.jpg
      DEB.jpg:       JPEG image data, JFIF       standard 1.02, resolution (DPI),       density 72x72, segment length 16,       baseline, precision 8, 300x300,       components 3
      ^C
     


---
<div dir='rtl'>

### چاپ محتویات بدون فاصله اضافی 
با استفاده از سوییچ N- میتوانید محتویات را در حالت بدون فاصله چاپ کنید . در حالت پیشفرض هنگام نمایش خروجی نوع فایلها در یک راستا قرار میگرفت . اگر میخواهید که هنگام خروجی نوع فایلها در یک راستا قرار نگیرد از سوییچ N- استفاده کنید.
</div>

    $ file *
    # book:               directory
      DEB.jpg:            JPEG image data,       JFIF standard 1.02, resolution (DPI),       density 72x72, segment length 16,       baseline, precision 8, 300x300,       components 3
      filejadid.txt:      ASCII text
      Hacking Tools:      directory
      import requests.py: ASCII text
      number.txt:         ASCII text
      Os.txt:             ASCII text
      T1est.txt:          empty
      test.txt:           ASCII text
      Test.txt:           empty
      tor-browser_en-US:  directory
      
    $ file -n *
    # book: directory
      DEB.jpg: JPEG image data, JFIF       standard 1.02, resolution (DPI),       density 72x72, segment length 16,       baseline, precision 8, 300x300,       components 3
      filejadid.txt: ASCII text
      Hacking Tools: directory
      import requests.py: ASCII text
      number.txt: ASCII text
      Os.txt: ASCII text
      T1est.txt: empty
      test.txt: ASCII text
      Test.txt: empty
      tor-browser_en-US: directory
      
---

### Author or Authors

- *[Amirhosein](https://github.com/amirhoseinsb)* | **<amirhoseinsohrabi.official@gmail.com>**

