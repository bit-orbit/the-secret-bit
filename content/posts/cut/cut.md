---
title: "cut"
date: 2022-03-08T15:50:23+03:30
draft: false
---



<div dir='rtl'>

### فهرست

> - [فهرست](#فهرست)
> - [مقدمه](#مقدمه)
> - [جداسازی محدوده‌ای از کاراکتر ها](#جداسازی-محدودهای-از-کاراکتر-ها)
> - [جدا کردن کاراکتر ها](#جدا-کردن-کاراکتر-ها)
> - [جدا سازی ستون](#جدا-سازی-ستون)
> - [جدا کردن ستون با استفاده از جداکننده متفاوت](#جدا-کردن-ستون-با-استفاده-از-جداکننده-متفاوت)
> - [ترکیب ابزار ها با یکدیگر](#ترکیب-ابزار-ها-با-یکدیگر)
> - [Author or Authors](#author-or-authors)




</div>

---
<div dir='rtl'>

### مقدمه
ابزارهای بسیار زیادی در سیستم عامل لینوکس وجود دارد که به شما امکان پردازش و فیلتر کردن فایل را میدهند . ابزار cut هم یکی از ابزارهای تحت فرمان برای برش و اعمال تغییرات روی فایل است.

برای مثال فایلی رو در نظر بگیرید که سه ستون دارد، ستون اول نام، ستون دوم
فامیلی و در ستون سوم سن نوشته شده است، حال اگر نیاز داشته باشید
تا فقط تمامی سطر های ستون دوم این فایل را مشاهده کنید ابزار
cat
به کمک شما خواهد آمد.
</div>

---
<div dir='rtl'>

### جداسازی محدوده‌ای از کاراکتر ها

فرض کنید ما فایلی از اسم و حروف مختلف داریم، برای جدا سازی حروف یا کاراکترهای خاص 
از سوییچ
`b-`
استفاده می‌کنیم
</div>

    $ cat test.txt
    # amirhosein
      jadi
      arya
      mehran
      amiryasin
      mahya
      
    $ cut -b 1-2,3 test.txt
    # ami
      jad
      ary
      meh
      ami
      mah


    $ cut -b -3 test.txt  
    # ami
      jad
      ary
      meh
      ami
      mah
      

---
<div dir='rtl'>

### جدا کردن کاراکتر ها

با استفاده از سوییچ `c-` میتوانید یک ستون خاص یا یک ستون با طول خاص را جدا کنید.
</div>

    $ cat test.txt
    # amirhosein
      jadi
      arya
      mehran
      amiryasin
      mahya


    $ cut -c 2 test.txt
    # m
      a
      r
      e
      m
      a
    
    $ cut -c -5 test.txt
    # amirh
      jadi
      arya
      mehra
      amiry
      mahya
      
      
      

---

<div dir='rtl'>

### جدا سازی ستون

فایلی با سه ستون نام، نام خانوادگی و سن را در نظر بگیرید،
برای جدا سازی تنها ستون **نام خانوادگی** از دیگر ستون ها از سوییچ
`f-`
استفاده می‌کنیم.
به صورت پیشرض جدا کننده ستون ها فاصه خالی در نظر گرفته می‌شود.
</div>

```bash
$ cat test.txt
# sima    abasy   19
shima   akbary  22
leyla   hoseni  29
first   second  20

$ cut -f 2 test.txt
# abasy
akbary
hoseni
second

```

---
<div dir='rtl'>

### جدا کردن ستون با استفاده از جداکننده متفاوت

ممکن است درون یک فایل از جدا کننده خاصی برای مشخص کردن ستون ها استفاده
شده باشید، برای مثال در فایل های
csv
از ویرگول برای جدا کردن ستون ها استفاده می‌شود.
</div>

    $ cat test.csv
    # amirhosein, sohrabi
      jadi, mirmirani
      arya, shabane
      mehran, ghafoorian
      amiryasin, sohrabi
      mahya, sohrabi
      

    $ cut -d "," -f 1 test.csv
    # amirhosein
      jadi
      arya
      mehran
      amiryasin
      mahya
      

    $ cut -d "," -f 2 test.csv 
    # sohrabi
      mirmirani
      shabani
      ghafoorian
      sohrabi
      sohrabe
      
      

---
<div dir='rtl'>

### ترکیب ابزار ها با یکدیگر

با ترکیب خروجی یک ابزار با ابزار های دیگر، می‌توان به خروجی های دقیق تری دست پیدا 
کرد.  چند نمومه از ترکیب های پر استفاده را برسی کرده‌ایم.

</div>

    $ cat test.txt
    # amirhosein sohrabi
      jadi mirmirani
      arya shabani
      mehran ghafoorian
      amiryasin sohrabi
      mahya sohrabi

> مرتب سازی متن

    $ cat test.txt | cut -d ' ' -f 2 | sort
    # ghafoorian
      mirmirani
      shabani
      sohrabi
      sohrabi
      sohrabi
      
> گرفتن سه سطر و سه ستون اول فایل، و ذخیره این خروجی در فایلی دیگر

    $ cat test.txt | head -n 3 | cut -d ' ' -f 1 > /tmp/Newfile.txt

    $ cat /tmp/Newfile.txt
    # amirhosein
      jadi
      arya
      
      

---      

### Author or Authors

- *[Amirhosein](https://github.com/amirhoseinsb)* | **<amirhoseinsohrabi.official@gmail.com>**
- *[Arya](https://github.com/shabane)* | **m.mohamadshabane@gmail.com**

