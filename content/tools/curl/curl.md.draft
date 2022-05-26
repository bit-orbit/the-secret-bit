---
title: "curl"
date: 2022-03-21T19:28:11+03:30
draft: true
---



<div dir='rtl'>

### فهرست

> - [مقدمه](#مقدمه)
> - [نمایش محتوای HTML موجود در URL](#نمایش-محتوای-html-موجود-در-url)
> - [دانلود فایل](#دانلود-فایل)
> - [ادامه دانلود قطع شده](#ادامه-دانلود-قطع-شده)
> - [دانلود فایل از url های مختلف](#دانلود-فایل-از-url-های-مختلف)
> - [شبیه سازی مرورگر](#شبیه-سازی-مرورگر)
> - [محدود کردن سرعت فایل](#محدود-کردن-سرعت-فایل)
> - [دانلود فایل از ftpserver](#دانلود-فایل-از-ftpserver)
> - [آپلود فایل در ftpserver](#آپلود-فایل-در-ftpserver)
> - [نمایش جزئیات عملیات](#نمایش-جزئیات-عملیات)
> - [ارسال درخواست در صورت مشکل](#ارسال-درخواست-در-صورت-مشکل)
> - [ارسال درخواست با زمان تاخیر دلخواه](#ارسال-درخواست-با-زمان-تاخیر-دلخواه)
> - [ارسال درخواست با حالت های متفاوت](#ارسال-درخواست-با-حالت-های-متفاوت)
> - [Author or Authors](#author-or-authors)
</div>




---
<div dir='rtl'>

### مقدمه
ابزار curl در واقع ابزاری برای انتقال داده ها از سمت سرور به کلاینت، اتصال به سرور، آپلود داده ها روی سرور و ... است. تاریخچه این ابزار به برنامه نویس سوئدی به نام دنیل استنبرگ بر میگردد. دنیل در اواسط ۱۹۹۰ زمانی که اینترنت تازه در حال شکل گرفتن بود پروژه ای را با نام curl آغاز کرد که در ابتدا هدف وی توسعه یک ربات بود . کار ربات به این صورت بود که نرخ تبدیل ارز را از یک صفحه وب به صورت دوره ای دانلود کند و معادل کرون سوئدی را به دلار آمریکا برای کاربران IRC ارائه دهد. و در نهایت پروژه دنیل تبدیل به پروژه ای شد که امروزه داریم از آن استفاده میکنیم.
</div>


---
<div dir='rtl'>

### نمایش محتوای HTML موجود در URL
برای نمایش محتویات موجود در یک صفحه از سوییچ --url استفاده کنید. با استفاده از این سوییچ محتویات html صفحه برای شما چاپ میشود.

</div>

    $ curl --url https://jadi.net

---
<div dir='rtl'>

### دانلود فایل
با استفاده از سوییچ های o- و O- به سادگی میتوانید فایلی را از اینترنت با استفاده از curl دانلود کنید. اما این دو سوییچ با هم تفاوت دارند، سوییچ O- فایل را در دایرکتوری جاری شما و با همان نام ذخیره میکند. اما سوییچ o- از شما محل ذخیره فایل و نام جدید فایل را دریافت میکند و فایل دانلود شده را با نام جدید در یک دایرکتوری دیگر ذخیره میکند. 
</div>

    # Download File With Curl
    $ curl -O "Downloadlink.com/linux.iso"

    # Download File And Change Name & Change Directory For Save file
    $ curl -o "/home/amirhosein/Donwload/linuxnew.iso" "Downloadlink.com/linux.iso" 


---
<div dir='rtl'>

### ادامه دانلود قطع شده
اگر یک دانلود به هر دلیلی قطع شد، شما میتوانید به راحتی با استفاده از سوییچ c- - آن را مجدد از جایی که قطع شده دانلود کنید.

</div>
    
    # Resume Download 
    $ curl -c - -O "Downloadlink.com/linux.iso"


---
<div dir='rtl'>

### دانلود فایل از url های مختلف
شما میتوانید با ترکیب ابزار با xargs url هایی که درون یک فایل متنی قرار دارند را دانلود کنید.

</div>

    # Download Multiply file with xargs
    $ xargs -n 1 curl -O < url.txt


---
<div dir='rtl'>

### شبیه سازی مرورگر 
گاهی اوقات ممکن است به دلایلی نیاز داشته باشید که یک مرورگر را شبیه سازی کنید. زیرا ممکن است برخی سرورها بسته به دستگاه ها یا مرورگر های مختلف محتویات مختلف را برگردانند. برای مثال ممکن است سرور تنظیم شده باشد تا درخواست های curl را مسدود کند. در چنین شرایطی برای شبیه سازی یک مرورگر از سوییچ A- استفاده کنید.
در مثال زیر من فایرفاکس را شبیه سازی کرده ام.

</div>

    # Simulation Web Browser
    $ curl -A "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0" https://linux.org

---
<div dir='rtl'>

### محدود کردن سرعت فایل
شما میتوانید با استفاده از سوییچ limit-rate -- سرعت دانلود خود را محدود کنید. 
</div>

    # limit download speed
    $ curl --limit-rate 1m -O https://dl.google.com/go/go1.10.3.linux-amd64.tar.gz


---
<div dir='rtl'>

### دانلود فایل از ftpserver
اگر که میخواهید از ftp server خاصی فایلی را دانلود کنید، ابتدا باید به ftp server لاگین کنید. بعد از لاگین به سرور تمام فایلها و دایرکتوری ها برای شما فهرست میشود و میتوانید به راحتی فایلهای مورد نظر را دانلود کنید.


</div>

    # login to ftp server & list all files and directory
    $ curl -u FTP_USERNAME:FTP_PASSWORD ftp://ftp.server.com/

    # download file with ftp server
    $ curl -u FTP_USERNAME:FTP_PASSWORD ftp://ftp.server.com/file.iso


---
<div dir='rtl'>

### آپلود فایل در ftpserver
با استفاده از سوییچ T- میتوانید فایلهای خود را روی ftp سرور آپلود کنید.
بعد از نام سوییچ 
</div>



---
<div dir='rtl'>

### نمایش جزئیات عملیات
با استفاده از سوییچ v- میتوانید جزئیات عملیات اجرا شده در بک گراند را مشاهده نمایید.

</div>

    $ curl -v https://jadi.net
    # OUTPUT
    # * Trying 104.21.34.122:80...
    # * Connected to jadi.net (104.21.34.122) port 80 (#0)
    # > GET / HTTP/1.1
    # > Host: jadi.net
    # > User-Agent: curl/7.82.0
    # > Accept: */*
    # > 
    # * Mark bundle as not supporting multiuse
    # < HTTP/1.1 301 Moved Permanently
    # < Date: Mon, 21 Mar 2022 19:24:36 GMT
    # < Transfer-Encoding: chunked
    # < Connection: keep-alive
    # < Cache-Control: max-age=3600
    # < Expires: Mon, 21 Mar 2022 20:24:36 GMT
    # < Location: https://jadi.net/
    # < Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?       s=Fs0XLl5TqO3fqsqKNLAmdELws%2F7%2BsOFILnyEs0zAFajujIUskLNagSh6nQcy8I%2BI411vTFPe7BHgY0Gl72A%2      Fsy7KUlz6XO1QgNn5aK6y%2BteRP12irKBPdKgnhA%3D%3D"}],"group":"cf-nel","max_age":604800}
    # < NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
    # < Server: cloudflare
    # < CF-RAY: 6ef911974ca68ce0-EWR
    # < alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400
    # < 
    # * Connection #0 to host jadi.net left intact
      


---
<div dir='rtl'>

### ارسال درخواست در صورت مشکل
اگر پکت های شما به مقصد نرسند یا به هردلیلی نتوانید با سرور ارتباط برقرار کنید، ارتباط شما قطع میشود و دوباره باید درخواست خود را ارسال کنید. برای رفع این مشکل از سوییچ --retry استفاده کنید. با استفاده از این سوییچ میتوانید تعیین کنید که چه تعداد درخواست در صورت به وجود آمدن مشکل به سمت سرور ارسال شود.
</div>

    $ curl --retry 7 https://examplkhbkhgkljhe.com
    # OUTPUT
    # curl: (6) Could not resolve host: examplkhbkhgkljhe.com
    # Warning: Problem : timeout. Will retry in 1 seconds. 7 retries left.
    # curl: (6) Could not resolve host: examplkhbkhgkljhe.com
    # Warning: Problem : timeout. Will retry in 2 seconds. 6 retries left.
    # curl: (6) Could not resolve host: examplkhbkhgkljhe.com
    # Warning: Problem : timeout. Will retry in 4 seconds. 5 retries left.
    # curl: (6) Could not resolve host: examplkhbkhgkljhe.com
    # Warning: Problem : timeout. Will retry in 8 seconds. 4 retries left.
    # curl: (6) Could not resolve host: examplkhbkhgkljhe.com
    # Warning: Problem : timeout. Will retry in 16 seconds. 3 retries left.
    # curl: (6) Could not resolve host: examplkhbkhgkljhe.com
    # Warning: Problem : timeout. Will retry in 32 seconds. 2 retries left.
    # curl: (6) Could not resolve host: examplkhbkhgkljhe.com
    # Warning: Problem : timeout. Will retry in 64 seconds. 1 retries left.
      


---
<div dir='rtl'>

### ارسال درخواست با زمان تاخیر دلخواه

با استفاده از سوییچ retry-delay-- و retry-- میتوانید درخواست های خود را در محدوده زمانی خاصی ارسال کنید. در مثال زیر هرپنج ثانیه یکبار یک درخواست به سمت سرور ارسال میشود و تا اتمام ۱۰۰ درخواست طول میکشد. زمانی که تمامی ۱۰۰ درخواست به سمت سرور ارسال شدند، عملیات تمام میشود.


</div>

    $ curl --retry-delay 5 --retry 100 https://examplsadfadsfasde.com 
    # OUTPUT
    # curl: (6) Could not resolve host: examplsadfadsfasde.com
    # Warning: Problem : timeout. Will retry in 5 seconds. 100 retries left.
    # curl: (6) Could not resolve host: examplsadfadsfasde.com
    # Warning: Problem : timeout. Will retry in 5 seconds. 99 retries left.
    # curl: (6) Could not resolve host: examplsadfadsfasde.com
    # Warning: Problem : timeout. Will retry in 5 seconds. 98 retries left.
    # curl: (6) Could not resolve host: examplsadfadsfasde.com
    # Warning: Problem : timeout. Will retry in 5 seconds. 97 retries left.
    # ^C
      

---
<div dir='rtl'>

### ارسال درخواست با حالت های متفاوت
همانطور که میدانید ما چهار حالت ارسال درخواست به سرور داریم، GET,PUT,POST,DELETE حالا اگر شما بخواهید یک درخواست DELETE به سمت سرور ارسال کنید، باید چه کاری انجام دهید؟
در این حالت شما میتوانید از سوییچ X- استفاده کنید. با استفاده از این سوییچ میتوانید درخواست های خود را با حالت های متفاوت ارسال کنید.

</div>

    $ curl -X "DELETE" https://url.com 

---

### Author or Authors

- *[Amirhosein](https://github.com/amirhoseinsb)* | **<amirhoseinsohrabi.official@gmail.com>**
