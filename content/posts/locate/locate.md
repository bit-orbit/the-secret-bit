---
title: "Locate"
date: 2022-03-09T18:47:24+03:30
draft: false
---

<div dir='rtl'>

### فهرست

- [فهرست](#فهرست)
- [مقدمه](#مقدمه)
- [نکته ی مهم برای استفاده از ابزار](#نکته-ی-مهم-برای-استفاده-از-ابزار)
- [جستجوی فایلها](#جستجوی-فایلها)
- [خوانایی بهتر هنگام جستجو با ترکیب ابزار با less](#خوانایی-بهتر-هنگام-جستجو-با-ترکیب-ابزار-با-less)
- [جستجوی فایلهای با پسوند خاص](#جستجوی-فایلهای-با-پسوند-خاص)
- [محدود کردن نتایج خروجی](#محدود-کردن-نتایج-خروجی)
- [جستجوی فایلها بدون حساسیت روی اسم](#جستجوی-فایلها-بدون-حساسیت-روی-اسم)
- [دیدن تعداد فایل های موجود](#دیدن-تعداد-فایل-های-موجود)
- [Author or Authors:](#author-or-authors)
</div>


---
<div dir='rtl'>

### مقدمه
یکی از سریع ترین و کاربردی ترین ابزارهای سرچ در لینوکس که میتوانید با ترکیب آن با سایر ابزارها به سرعت فایلهای خود را در لینوکس پیدا کنید.
</div>

---
<div dir='rtl'>

### نکته ی مهم برای استفاده از ابزار
ابزار locate با استفاده از یک دیتا بیس که هر ۲۴ ساعت یکبار آپدیت میشود کار میکند . به طور مثال اگر شما در لینوکس فایلی ایجاد کرده اید بعد از ۲۴ ساعت فایل شما روی دیتا بیس نوشته میشود . و شما اگر قبل از ۲۴ ساعت به جستجوی فایل مورد نظر بپردازید آن را پیدا نخواهید کرد. اما برای رفع این مشکل و آپدیت دستی دیتابیس دستوری تحت عنوان updatedb وجود دارد که با دسترسی روت کار میکند. شما وقتی دستور updated را استفاده میکنید بلافاصله دیتابیس شما آپدیت میشود و هنگام جستجو به مشکلی بر نخواهید خورد.
</div>

    $ sudo updatedb
---
<div dir='rtl'>

### جستجوی فایلها
برای جستجوی فایل مورد نظر بعد از آپدیت دیتابیس از دستور locate استفاده کنید. به مثال زیر توجه کنید.
</div>

    $ sudo updatedb
    $ locate /home/amirhosein/Desktop .txt
    # /home/amirhosein/Desktop/Os.txt
      /home/amirhosein/Desktop/filejadid.txt
      /home/amirhosein/Desktop/number.txt
      /home/amirhosein/Desktop/test.txt
      
---
<div dir='rtl'>

### خوانایی بهتر هنگام جستجو با ترکیب ابزار با less 
اگر نتیجه ی جستجوی شما طولانی و خسته کنندست میتوانید ترکیب locate با less را امتحان کنید.
</div>

    $ sudo updatedb
    $ locate /home/amirhosein/Desktop .txt | less
    # /home/amirhosein/Desktop/Os.txt
      /home/amirhosein/Desktop/filejadid.txt
      /home/amirhosein/Desktop/number.txt
      /home/amirhosein/Desktop/test.txt
      (END)

---
<div dir='rtl'>

### جستجوی فایلهای با پسوند خاص
با استفاده از نماد ستاره در کنار دستور میتوانید تمام فایلهایی که پسوند خاص مد نظر شما را دارند به راحتی پیدا کنید.
</div>

    $ sudo updatedb
    $ locate *.py
    Or 
    $ locate /home *.py
---
<div dir='rtl'>

### محدود کردن نتایج خروجی
شما میتوانید با استفاده از سوییچ -n و عدد مورد نظر نتایج خروجی را به عددی خاص محدود کنید.
</div>
    
    $ sudo updatedb
    $ locate -n 2 *.py
    # /etc/python2.7/sitecustomize.py
      /etc/python3.10/sitecustomize.py
                           
---
<div dir='rtl'>

### جستجوی فایلها بدون حساسیت روی اسم
در حالت پیش فرض ابزار روی حروف بزرگ و کوچک حساس است . اگر میخواهید که ابزار روی حروف بزرگ و کوچک حساسیتی نشان ندهد از سوییچ -i استفاده کنید.
برای درک بهتر موضوع به دستورات زیر توجه کنید.

</div>

    $ sudo updatedb
    $ locate /home/amirhosein/Desktop test.txt
    # /home/amirhosein/Desktop test.txt


    $ locate /home/amirhosein/Desktop -i test.txt
    # /home/amirhosein/Desktop/Test.txt
      /home/amirhosein/Desktop/test.txt
      
---
<div dir='rtl'>

### دیدن تعداد فایل های موجود
اگر میخواستید ببینید که با پسوند خاصی که شما در نظر گرفته اید یا کلا در فلان دایرکتوری چند فایل وجود دارد میتوانید از سوییچ -c استفاده کنید.
برای درک بهتر موضوع به دستورات زیر دقت کنید.
</div>

    $ sudo updatedb
    $ locate -c /home/amirhosein/Desktop .txt
    # 35

    $ locate -c /home/amirhosein/Desktop
    # 1967

---

### Author or Authors:

- *[Amirhosein](https://github.com/amirhoseinsb)* | **<amirhoseinsohrabi.official@gmail.com>**
