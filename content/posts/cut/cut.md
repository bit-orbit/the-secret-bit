---
title: "Cut"
date: 2022-03-08T15:50:23+03:30
draft: false
---



<div dir='rtl'>

### فهرست

- [فهرست](#فهرست)
- [مقدمه](#مقدمه)
- [جداسازی یک یا چند کاراکتر](#جداسازی-یک-یا-چند-کاراکتر)
- [جدا کردن به روش ستونی](#جدا-کردن-به-روش-ستونی)
- [جدا کردن با استفاده از جداکننده خاص](#جدا-کردن-با-استفاده-از-جداکننده-خاص)
- [ترکیب ابزار ها با هم دیگر](#ترکیب-ابزار-ها-با-هم-دیگر)
- [Author or Authors:](#author-or-authors)




</div>

---
<div dir='rtl'>

### مقدمه
ابزارهای بسیار زیادی در سیستم عامل لینوکس وجود دارد که به شما امکان پردازش و فیلتر کردن فایل را میدهند . ابزار cut هم یکی از ابزارهای تحت فرمان برای برش و اعمال تغییرات روی فایل است. با ترکیب این ابزار با دیگر ابزارهای قدرتمند لینوکس میتوانید به سرعت روی فایلهای خود تغییرات گسترده ای ایجاد کنید.
</div>

---
<div dir='rtl'>

### جداسازی یک یا چند کاراکتر
فرض کنید ما فایلی داریم که پر از اسم یا حروف مختلف هست. برای جدا کردن حروف یا کاراکترهای خاص استفاده از سوییچ b یکی از راههایی است که میتوانید کاراکترهای خاص یا کلمات خاص را فیلتر کنید.
</div>

    $ cat test.txt 
    # amirhosein
      jadi
      arya
      mehran
      amiryasin
      mahya
      
    $ cut -b 1-2,3 test.txt
    # amr
      jai
      ara
      mer
      amr
      may

    $ cut -b -3 test.txt  
    # ami
      jad
      ary
      meh
      ami
      mah
      

---
<div dir='rtl'>

### جدا کردن به روش ستونی
با استفاده از سوییچ c میتوانید یک ستون خاص یا یک ستون با طول خاص را جدا کنید.
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

### جدا کردن با استفاده از جداکننده خاص

با استفاده از سوییچ d میتوانید فیلد ها را جدا کنید.    
</div>

    $ cat test.txt
    # amirhosein sohrabi
      jadi mirmirani
      arya shabani
      mehran ghafoorian
      amiryasin sohrabi
      mahya sohrabi
      

    $ cut -d " " -f 1 test.txt
    # amirhosein
      jadi
      arya
      mehran
      amiryasin
      mahya
      

    $ cut -d " " -f 2 test.txt 
    # sohrabi
      mirmirani
      shabani
      ghafoorian
      sohrabi
      sohrabi
      
      

---
<div dir='rtl'>

### ترکیب ابزار ها با هم دیگر
در ابتدای توضیحات گفتم که میتوانید با ترکیب این ابزار با دیگر ابزار خروجی های فوق العاده ای بگیرید به همین خاطر برای درک بهتر شما عزیزان چند نمونه دستور ترکیبی در زیر آورده ام که امیدوارم از آن ها نهایت استفاده را ببرید.
</div>

    $ cat test.txt
    # amirhosein sohrabi
      jadi mirmirani
      arya shabani
      mehran ghafoorian
      amiryasin sohrabi
      mahya sohrabi

    $ cat test.txt | cut -d ' ' -f 2 | sort
    # ghafoorian
      mirmirani
      shabani
      sohrabi
      sohrabi
      sohrabi
      
    $ cat test.txt | head -n 3 | cut -d ' ' -f 1 > /home/amirhosein/Desktop/Newfile.txt

    $ cat /home/amirhosein/Desktop/Newfile.txt
    # amirhosein
      jadi
      arya
      
      

      

### Author or Authors:

- *[Amirhosein](https://github.com/amirhoseinsb)* | **<amirhoseinsohrabi.official@gmail.com>**

