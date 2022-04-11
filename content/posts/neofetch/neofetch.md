---
title: "neofetch"
date: 2022-04-07T01:27:14+04:30
draft: false
---


<div dir='rtl'>

### فهرست

- [فهرست](#فهرست)
- [مقدمه](#مقدمه)
- [نمایش اطلاعات به شکل کامل](#نمایش-اطلاعات-به-شکل-کامل)
- [ذخیره خروجی در فایل](#ذخیره-خروجی-در-فایل)
- [نمایش مشخصات cpu](#نمایش-مشخصات-cpu)
- [نمایش مشخصات کارت گرافیک](#نمایش-مشخصات-کارت-گرافیک)
- [خروجی گرفتن از مدل سی پی یو](#خروجی-گرفتن-از-مدل-سی-پی-یو)
- [Author or Authors](#author-or-authors)
</div>

---
<div dir='rtl'>

### مقدمه
برای نمایش اطلاعات کاملی راجب سیستم عامل، سی پی یو، رم و .... میتوانید از ابزار neofetch استفاده کنید.
</div>

---
<div dir='rtl'>

### نمایش اطلاعات به شکل کامل

برای اینکه اطلاعات را به شکل کامل، رنگی و مرتب شده ببینید کافیست از دستور neofetch در خط فرمان استفاده کنید. بعد از استفاده از این دستور اطلاعات برای شما در خط فرمان چاپ خواهد شد. 

<p align="center">
 <img src="Neofetch.png"/>
</p>

</div>
    
    # View the information with neofetch
    $ neofetch


---
<div dir='rtl'>

### ذخیره خروجی در فایل
اگر میخواهید که خروجی را در فایلی ذخیره کنید تا بعدا آن را بخوانید از اوپراتور < استفاده کنید. با استفاده از این اوپراتور میتوانید خروجی دستور را به یک فایل متنی انتقال دهید.

<p align="center">
 <img src="cat neofetch.png"/>
</p>

</div>

    # step 1
    # save the output in the test.txt 
    $ neofetch > test.txt

    # step 2
    # view the test.txt with cat
    # cat test.txt

    # OUTPUT
    #                  ...-:::::-...                 amirhosein@P5PL2-E 
    #           .-MMMMMMMMMMMMMMM-.              ------------------ 
    #       .-MMMM`..-:::::::-..`MMMM-.          OS: Linux Mint 20.3 x86_64 
    #     .:MMMM.:MMMMMMMMMMMMMMM:.MMMM:.        Host: P5PL2-E Rev 1.xx 
    #    -MMM-M---MMMMMMMMMMMMMMMMMMM.MMM-       Kernel: 5.4.0-91-generic 
    #  `:MMM:MM`  :MMMM:....::-...-MMMM:MMM:`    Uptime: 2 hours, 47 mins 
    #  :MMM:MMM`  :MM:`  ``    ``  `:MMM:MMM:    Packages: 2037 (dpkg), 9 (snap) 
    # .MMM.MMMM`  :MM.  -MM.  .MM-  `MMMM.MMM.   Shell: bash 5.0.17 
    # :MMM:MMMM`  :MM.  -MM-  .MM:  `MMMM-MMM:   Resolution: 1024x768 
    # :MMM:MMMM`  :MM.  -MM-  .MM:  `MMMM:MMM:   DE: Xfce 
    # :MMM:MMMM`  :MM.  -MM-  .MM:  `MMMM-MMM:   WM: Xfwm4 
    # .MMM.MMMM`  :MM:--:MM:--:MM:  `MMMM.MMM.   WM Theme: Mint-Y 
    #  :MMM:MMM-  `-MMMMMMMMMMMM-`  -MMM-MMM:    Theme: Mint-Y-Dark [GTK2/3] 
    #   :MMM:MMM:`                `:MMM:MMM:     Icons: Mint-Y [GTK2/3] 
    #    .MMM.MMMM:--------------:MMMM.MMM.      Terminal: xfce4-terminal 
    #      '-MMMM.-MMMMMMMMMMMMMMM-.MMMM-'       Terminal Font: Monospace 12 
    #        '.-MMMM``--:::::--``MMMM-.'         CPU: Intel Pentium 4 3.40GHz (2) @ 3.400GHz 
    #             '-MMMMMMMMMMMMM-'              GPU: NVIDIA GeForce GT 430 
    #                ``-:::::-``                 Memory: 1678MiB / 2991MiB 
      
                                                           

---
<div dir='rtl'>

### نمایش مشخصات cpu
شما میتوانید با ترکیب ابزار با ابزار grep مشخصات cpu را مشاهده کنید.

</div>

    # View The Cpu Information with grep 
    $ neofetch | grep "CPU"

    # OUTPUT
    # CPU: Intel Pentium 4 3.40GHz (2) @ 3.400GHz 


---
<div dir='rtl'>

### نمایش مشخصات کارت گرافیک
شما میتوانید به جای عبارت CPU از عبارت GPU هنگام ترکیب ابزار با grep استفاده کنید. در اینصورت مشخصات کارت گرافیک برای شما چاپ خواهد شد.

</div>

    # View The Gpu Information With grep 
    $ neofetch | grep "GPU"

    # OUTPUT
    # GPU: NVIDIA GeForce GT 430 


---
<div dir='rtl'>

### خروجی گرفتن از مدل سی پی یو
شما میتوانید خروجی فیلتر شده با grep را با استفاده از اوپراتور خروجی < به فایل متنی انتقال دهید و آن را بخوانید.

</div>

    # save the output with > Operator
    $ neofetch | grep "CPU" > test.txt

    # view the file with cat
    $ cat test.txt
    
    # OUTPUT
    # CPU: Intel Pentium 4 3.40GHz (2) @ 3.400GHz 

---

### Author or Authors

- *[Amirhosein](https://github.com/amirhoseinsb)* | **<amirhoseinsohrabi.official@gmail.com>**
