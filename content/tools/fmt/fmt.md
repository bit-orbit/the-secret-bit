---
title: "fmt"
date: 2022-03-07T18:44:26+03:30
draft: false
---

<div dir='rtl'>

### فهرست

> - [مقدمه](#مقدمه)
> - [نمایش فایل متنی با fmt](#نمایش-فایل-متنی-با-fmt)
> - [نمایش فایل با طول دلخواه](#نمایش-فایل-با-طول-دلخواه)
> - [برجسته کردن خط اول فایل](#برجسته-کردن-خط-اول-فایل)
> - [حذف کردن فاصله بین کلمات](#حذف-کردن-فاصله-بین-کلمات)
> - [Author or Authors:](#author-or-authors)




</div>

---
<div dir='rtl'>

### مقدمه
اگر فایل متنی کوتاه یا بلندی دارید که به هم ریخته است یا به درستی قالب بندی نشده است . میتوانید با ابزار fmt به سرعت فایل خود را قالب بندی کنید.
</div>

---
<div dir='rtl'>

### نمایش فایل متنی با fmt
اگر به شکل عادی از دستور fmt استفاده کنید تمامی کلمات موجود در فایل در یک خط مساوی قرار خواهند گرفت.
</div>

    $ cat test.txt
    # Hi,
      this
      is
      a
      test
      file
      written by AmirHosein Sohrabi.
      Always strive to achieve the goal. life is Beautiful.

    $ fmt test.txt
    # Hi,this is a test file
      written by AmirHosein Sohrabi.Always strive to achieve the goal. life is Beautiful.


---
<div dir='rtl'>

### نمایش فایل با طول دلخواه
اگر خواستید که فایل شما با طول دلخواهی نمایش داده شود از سوییچ w استفاده کنید.توجه داشته باشید که اندازی گیری طول در این ابزار بر اساس کاراکتر است!!!
</div>

    
    $ cat test.txt
    # Hi, this is a test file written by AmirHosein Sohrabi.
      Always strive to achieve the goal. life is Beautiful.
    
    $ fmt -w 20 test.txt
    # Hi, this is a test
      file written by
      AmirHosein Sohrabi.
      Always strive
      to achieve the
      goal. life is
      Beautiful.

            

---
<div dir='rtl'>

### برجسته کردن خط اول فایل
اگر فایل بزرگی دارید قطعا تشخیص خط اول آن در ترمینال مشکل است. برای حل این مشکل از سوییچ t استفاده کنید. شما با استفاده از این سوییچ فرو رفتگی خط اول و دوم با سایر خطوط تفاوت خواهد داشت و بدین ترتیب میتوانید به راحتی خط اول را پیدا کنید.
</div>


    $ cat test.txt
    # Hi, this is a test file written by AmirHosein Sohrabi.  Always   strive to
      achieve the goal. life is Beautiful.  Hi, this is a test file written   by
      AmirHosein Sohrabi.  Always strive to achieve the goal. life is   Beautiful.
      Hi, this is a test file written by AmirHosein Sohrabi.  Always strive
      to achieve the goal. life is Beautiful.

    $ fmt -t test.txt
    # Hi, this is a test file written by AmirHosein Sohrabi.
      Always strive to achieve the goal. life is Beautiful.
      Hi, this is a test
      file written by
      AmirHosein Sohrabi.
      Always strive
      to achieve the
      goal. life is
      Beautiful.
      Hi, this is a test
      file written by
      AmirHosein Sohrabi.
      Always strive
      to achieve the
      goal. life is
      Beautiful.
                  
---


<div dir='rtl'>

### حذف کردن فاصله بین کلمات
اگر فایل شما از فاصله های بی خودی پر شده است میتوانید با سوییچ u فاصله های بین کلمات را تنظیم کنید. این سوییچ از یک فاصله برای بین کلمه ها و از دو فاصله برای اتمام جملات استفاده میکند.
</div>

    $ cat test.txt   
    # Hi   ,  this  is   a      test    file     written by AmirHosein   Sohrabi.
      Always strive to   achieve    the  goal.     life is Beautiful. 
                    
    $ fmt -u test.txt
    # Hi , this is a test file written by AmirHosein Sohrabi.  Always strive
      to achieve the goal.  life is Beautiful.
                                    

---

### Author or Authors:

- *[Amirhosein](https://github.com/amirhoseinsb)* | **<amirhoseinsohrabi.official@gmail.com>**

