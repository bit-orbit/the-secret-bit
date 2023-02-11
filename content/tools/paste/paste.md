---
title: "paste"
date: 2022-03-08T19:01:01+03:30
draft: false
toc:True
---


---
<div dir='rtl'>

### مقدمه
ابزاری که پیش رو دارید برای ادغام فایل ها به کار میرود و کاربرد اصلی آن ادغام فایلها با همدیگر است. با استفاده از ابزار paste و سوییچ های مختلف آن میتوانید به سرعت فایل هایتان را ترکیب کنید .اما بهتر است بدانید که این ابزار در استفاده های روزانه به شما بسیار زیاد کمک خواهد کرد. خواه مدیر سیستم باشید یا کاربر معمولی . در هرصورت به کارتان خواهد آمد.
</div>


---
<div dir='rtl'>

### ادغام سریع دو فایل با یکدیگر
برای ادغام فایلها با هم دیگر کافیست نام ابزار را قبل از فایلهایی که قرار هست با هم ادغام شوند قرار دهید.
</div>

    $ paste number.txt test.txt Os.txt
    # 1       amirhosein sohrabi      Kali
      2       jadi mirmirani  ubuntu
      3       arya shabani    fedora
      4       mehran ghafoorian       ubuntu
      5       amiryasin sohrabi       kali
      6       mahya sohrabi   mint
      7               ubuntu
      8
      9
      10
      

---
<div dir='rtl'>

### استفاده از جدا کننده هنگام ادغام فایل
اگر به دستور بالا دقت کرده باشید متوجه خواهید شد که فایل ها به شکل نامنظیم باهم دیگر ادغام شده اند. برای رفع این مشکل از سوییچ -d استفاده میکنیم. با استفاده از این سوییچ میتوانید مشکل نامنظم ادغام شدن فایلها را رفع کنید. به دو مثال زیر توجه کنید.
</div>

    $ paste -d "| " number.txt test.txt Os.txt
    # 1|amirhosein sohrabi Kali
      2|jadi mirmirani ubuntu
      3|arya shabani fedora
      4|mehran ghafoorian ubuntu
      5|amiryasin sohrabi kali
      6|mahya sohrabi mint
      7| ubuntu
      8| 
      9| 
      10| 

    $ paste -d "|," number.txt test.txt Os.txt
    # 1|amirhosein sohrabi,Kali
      2|jadi mirmirani,ubuntu
      3|arya shabani,fedora
      4|mehran ghafoorian,ubuntu
      5|amiryasin sohrabi,kali
      6|mahya sohrabi,mint
      7|,ubuntu
      8|,
      9|,
      10|,
      

---
<div dir='rtl'>

### ادغام فایلها به شکل خطی
به شکل عادی زمانی که از ابزار استفاده میکنید ابزار فایلها را به شکل ستونی یا عمودی ادغام میکند. اگر خواستید که فایلهای شما به شکل افقی یا خطی ادغام شوند از سوییچ -s استفاده کنید.
در مثال زیر شما دوحالت نامنظم و منظم را خواهید دید.
</div>

    $ paste -s number.txt test.txt Os.txt 
    # 1       2       3       4       5       6       7       8  910
      amirhosein sohrabi      jadi mirmirani  arya shabani    mehran ghafoorian     amiryasin       sohrabi       mahya sohrabi
      Kali    ubuntu  fedora  ubuntu  kali    mint    ubuntu
                              
    $ paste -sd " : " number.txt test.txt Os.txt
    # 1 2:3 4 5:6 7 8:9 10
      amirhosein sohrabi jadi mirmirani:arya shabani mehran ghafoorian amiryasin   sohrabi:mahya       sohrabi 
      Kali ubuntu:fedora ubuntu kali:mint ubuntu 
---

### Author or Authors

- *[Amirhosein](https://github.com/amirhoseinsb)* | **<amirhoseinsohrabi.official@gmail.com>**

