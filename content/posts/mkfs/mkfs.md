---
title: "mkfs"
date: 2022-04-09T18:01:46+04:30
draft: false
---


<div dir='rtl'>

### فهرست

- [فهرست](#فهرست)
- [مقدمه](#مقدمه)
- [ایجاد یک پارتیشن و فرمت کردن آن](#ایجاد-یک-پارتیشن-و-فرمت-کردن-آن)
- [](#)
- [](#-1)
- [](#-2)
- [](#-3)
- [](#-4)
- [](#-5)
- [](#-6)
- [](#-7)
- [](#-8)
- [Author or Authors](#author-or-authors)
</div>

---
<div dir='rtl'>

### مقدمه
برای ایجاد فایل سیستم یا تغییر فرمت یک پارتیشن به فرمت دیگر میتوانید از از ابزار mkfs استفاده کنید. mkfs مخفف عبارت make file system میباشد. لازم به ذکر است بدانید که هنگام فرمت یک پارتیشن تمامی اطلاعات موجود در پارتیشن از بین خواهند رفت.
</div>

---
<div dir='rtl'>

### ایجاد یک پارتیشن و فرمت کردن آن
در قدم اول با استفاده از ابزار fdisk وضعیت دیسک را چک کنید. در همین کتاب ابزار fdisk به شکل کامل توضیح داده شده است، بنابر این به جزئیات fdisk نمیپردازیم.
پس در قدم اول با سوییچ l- fdisk وضعیت یک هارد دیوایس خاص را چک میکنیم. در قدم دوم بعد از اطمینان هارد دیوایس را با fdisk باز میکنیم. چنانچه به راهنمایی نیاز داشتید از کامند m استفاده کنید. در قدم سوم با استفاده از کامند n وارد محیط ایجاد پارتیشن میشویم و با کامند p یک پارتیشن primary ایجاد میکنیم. در قدم بعد شماره پارتیشن را وارد میکنیم که به شکل پیشفرض برای اولین پارتیشن شماره یک در نظر گرفته میشود. در مرحله بعدی فضای آغازین یا first sector یا محل شروع پارتیشن مشخص میشود، من اینتر میکنم تا همان مقدار پیشفرض 2048 در نظر گرفته شود. در مرحله بعدی فضای پارتیشن مشخص میشود که من با استفاده از کامند +4G ۴ گیگ فضا در نظر میگیرم.
حالا پارتیشن برای ما ایجاد شد، با استفاده از کامند w تغییرات را اعمال میکنیم و از ابزار خارج میشویم. حالا یک پارتیشن خام داریم، میخواهیم این پارتیشن را با فرمت ext4 فرمت دهی کنیم. در این مرحله از ابزار mkfs استفاده میکنیم، نحوه فرمت کردن با ابزار mkfs در پایین توضیح داده شده است.
فقط لازم به ذکر است بدانید که قبل از فرمت کردن حتما پارتیشن یا هارد دیوایس را umount کنید.
<p align = "center">
    <img src = "1.png">
</p>

<p align = "center">
    <img src = "2.png">
</p>

<p align = "center">
    <img src = "3.png">
</p>

</div>

    # step 1
    # Monitor the hard device with fdisk -l 
    $ sudo fdisk -l /dev/sdc

    # step 2 
    # Open the Device with fdisk
    $ sudo fdisk /dev/sdc

    # step 3
    # Create the new partition with n command

    # step 4
    # Enter the w for apply the changes

    # step 5
    # umount the hard for format
    $ umount /dev/sdc1

    # step 6
    # format the partition with mkfs
    $ sudo mkfs.ext4 /dev/sdc1

---
<div dir='rtl'>

### 

</div>



---
<div dir='rtl'>

### 

</div>


---
<div dir='rtl'>

### 

</div>



---
<div dir='rtl'>

### 

</div>


---
<div dir='rtl'>

### 

</div>


---
<div dir='rtl'>

### 

</div>


---
<div dir='rtl'>

### 

</div>


---
<div dir='rtl'>

### 

</div>


---
<div dir='rtl'>

### 

</div>

---

### Author or Authors

- *[Amirhosein](https://github.com/amirhoseinsb)* | **<amirhoseinsohrabi.official@gmail.com>**
