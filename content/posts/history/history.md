---
title: "history"
date: 2022-03-12T00:13:25+03:30
draft: false
---

<div dir='rtl'>

### فهرست

- [فهرست](#فهرست)
- [مقدمه](#مقدمه)
- [نمایش سوابق دستورات](#نمایش-سوابق-دستورات)
- [جداکردن دستور خاص از سابقه](#جداکردن-دستور-خاص-از-سابقه)
- [گرفتن نسخه پشتیبان از سابقه دستورات](#گرفتن-نسخه-پشتیبان-از-سابقه-دستورات)
- [گرفتن نسخه پشتیبان از دستور خاص](#گرفتن-نسخه-پشتیبان-از-دستور-خاص)
- [Author or Authors](#author-or-authors)
</div>

---
<div dir='rtl'>

### مقدمه
اگر از ترمینال لینوکس استفاده میکنید ممکن است برایتان پیش آمده باشد که دستوری را در ترمینال اجرا کرده باشید و آن دستور رافراموش کرده باشید. با استفاده از دستور history میتوانید سابقه دستورات خود را مشاهده کنید.
</div>

---
<div dir='rtl'>

### نمایش سوابق دستورات
برای نمایش تمامی سوابق دستورات خود در ترمینال از دستور history استفاده کنید.
اینجا من از ابزار head هم در کنار ابزار history استفاده کردم . چون در غیر اینصورت ابزار کل سابقه دستورات را برای من چاپ میکرد.
</div>

    $ history | head
    # 1  man apt-get
      3  man pm
      4  sudo apt-get install pm
      7  sudo apt upgrade
      11  sudo dpkg -i        'google-chrome-stable_current_amd6      4 (1).deb'\n
      13  which chrome
      14  whereis chrome
      15  مس
      17  sensors -v
      18  git --version

---
<div dir='rtl'>

### جداکردن دستور خاص از سابقه
شما میتوانید با استفاده از ابزار grep دستور خاص مد نظر را از سایر دستورات جدا کنید.
</div>

    $ history | grep 'apt-get'
    # 1  man apt-get
      4  sudo apt-get install pm
      23  $ sudo apt-get install simplescreenrecorder\n
      24  $ sudo apt-get install simplescreenrecorder
      341  sudo apt-get install kget
      429  apt-get install tor
      430  sudo apt-get install tor
      513  sudo apt-get upgrade bzr
      701  sudo apt-get libwxgtk2.8-dev
      717  sudo apt-get install woeusb
      719  sudo apt-get install woeusb-frontend-wxgtk
      724  sudo apt-get intall aptitude
      1169  sudo apt-get update
      1991  sudo apt-get upgrade locate
---
<div dir='rtl'>

### گرفتن نسخه پشتیبان از سابقه دستورات
شما میتوانید با استفاده از اوپراتور خروجی از سابقه دستورات خود پشتیبان تهیه کنید.
</div>

    $ history > backup.txt
                                                 
---
<div dir='rtl'>

### گرفتن نسخه پشتیبان از دستور خاص
شما میتوانید با استفاده از ابزار grep دستورات را فیلتر کنید و خروجی را به فایل بکاپ اضافه کنید.
</div>

    $ history | grep 'apt-get' >> backup.txt
                     
---
### Author or Authors

- *[Amirhosein](https://github.com/amirhoseinsb)* | **<amirhoseinsohrabi.official@gmail.com>**
