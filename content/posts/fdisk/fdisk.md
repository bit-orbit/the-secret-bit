---
title: "fdisk"
date: 2022-04-04T20:44:32+04:30
draft: false
---

<div dir='rtl'>

### فهرست

> - [مقدمه](#مقدمه)
> - [لیست کردن پارتیشن های موجود](#لیست-کردن-پارتیشن-های-موجود)
> - [لیست کردن اطلاعات مربوط به هارد دیوایس خاص](#لیست-کردن-اطلاعات-مربوط-به-هارد-دیوایس-خاص)
> - [حذف کردن پارتیشن خاص](#حذف-کردن-پارتیشن-خاص)
> - [ایجاد پارتیشن](#ایجاد-پارتیشن)
> - [نمایش توضیحات راهنما](#نمایش-توضیحات-راهنما)
> - [همچنین مطالعه کنید](#همچنین-مطالعه-کنید)
> - [Author or Authors](#author-or-authors)
</div>


---
<div dir='rtl'>

### مقدمه
هنگامی که میخواهید از یک هارد یا یک فلش استفاده کنید،در قدم اول باید آن را پارتیشن بندی کنید. یعنی هارد یا فلش یا دیوایسی که 
کار ذخیره سازی اطلاعات را انجام میدهد را به چند بخش تقسیم کنید. شما با استفاده از ابزار
*fdisk*
میتوانید پارتیشن های ایجاد شده را مدیریت کنید یا پارتیشن جدیدی ایجاد کنید. اما بحث فقط پارتیشن بندی نیست. شما بعد از پارتیشن بندی نیاز به فرمت کردن پارتیشن ها دارید . وظیفه فرمت کردن را ابزار
[mkfs](/posts/mkfs/mkfs/)
به عهده دارد.

</div>

  
---
<div dir='rtl'>

### لیست کردن پارتیشن های موجود

با استفاده از سوییچ l- به تنهایی میتوانید اطلاعات کاملی راجب هارد دیوایس ها و پارتیشن های ایجاد شده دریافت کنید.
</div>

    $ sudo fdisk -l
    # OUTPUT
    # Disk /dev/loop0: 1.88 MiB, 1945600 bytes, 3800 sectors
    # Units: sectors of 1 * 512 = 512 bytes
    # Sector size (logical/physical): 512 bytes / 512 bytes
    # I/O size (minimum/optimal): 512 bytes / 512 bytes
    # 
    # 
    # Disk /dev/loop1: 110.69 MiB, 116051968 bytes, 226664 sectors
    # Units: sectors of 1 * 512 = 512 bytes
    # Sector size (logical/physical): 512 bytes / 512 bytes
    # I/O size (minimum/optimal): 512 bytes / 512 bytes
    # 
    # 
    # Disk /dev/loop2: 61.92 MiB, 64901120 bytes, 126760 sectors
    # Units: sectors of 1 * 512 = 512 bytes
    # Sector size (logical/physical): 512 bytes / 512 bytes
    # I/O size (minimum/optimal): 512 bytes / 512 bytes
    # 
    # 
    # Disk /dev/loop3: 54.28 MiB, 56905728 bytes, 111144 sectors
    # Units: sectors of 1 * 512 = 512 bytes
    # Sector size (logical/physical): 512 bytes / 512 bytes
    # I/O size (minimum/optimal): 512 bytes / 512 bytes
    # 
    # 
    # Disk /dev/loop4: 61.92 MiB, 64901120 bytes, 126760 sectors
    # Units: sectors of 1 * 512 = 512 bytes
    # Sector size (logical/physical): 512 bytes / 512 bytes
    # I/O size (minimum/optimal): 512 bytes / 512 bytes
    # 
    # 
    # Disk /dev/loop5: 43.64 MiB, 45748224 bytes, 89352 sectors
    # Units: sectors of 1 * 512 = 512 bytes
    # Sector size (logical/physical): 512 bytes / 512 bytes
    # I/O size (minimum/optimal): 512 bytes / 512 bytes
    # 
    # 
    # Disk /dev/sda: 149.5 GiB, 160041885696 bytes, 312581808 sectors
    # Disk model: WDC WD1600AABS-0
    # Units: sectors of 1 * 512 = 512 bytes
    # Sector size (logical/physical): 512 bytes / 512 bytes
    # I/O size (minimum/optimal): 512 bytes / 512 bytes
    # Disklabel type: gpt
    # Disk identifier: 1C4F28C8-8187-45DB-8B55-42931393BF3A
    # 
    # 
    # Disk /dev/sdb: 931.53 GiB, 1000204886016 bytes, 1953525168 sectors
    # Disk model: WDC WD10EZEX-22M
    # Units: sectors of 1 * 512 = 512 bytes
    # Sector size (logical/physical): 512 bytes / 4096 bytes
    # I/O size (minimum/optimal): 4096 bytes / 4096 bytes
    # Disklabel type: dos
    # Disk identifier: 0x00001727
    # 
    # Device     Boot      Start        End    Sectors   Size Id Type
    # /dev/sdb1  *          2048  195311615  195309568  93.1G 83 Linux
    # /dev/sdb2        195313662 1953523711 1758210050 838.4G  5 Extended
    # /dev/sdb5       1949618176 1953523711    3905536   1.9G 82 Linux swap / Solaris
    # /dev/sdb6        195313664  429686783  234373120 111.8G 83 Linux
    # /dev/sdb7        429688832  624998399  195309568  93.1G 83 Linux
      
  
  
---
<div dir='rtl'>

### لیست کردن اطلاعات مربوط به هارد دیوایس خاص
با استفاده از سوییچ l- و وارد کردن نام هارد دیوایس میتوانید اطلاعات مربوط به هارد دیوایس خاص و همچنین پارتیشن های هارد دیوایس خاص را مشاهده کنید. همانطور که میدانید هارد دیوایس ها با نام sd شناخته میشوند. برای مثال هارد شماره یک sda هارد شماره دوم sdb و به همین ترتیب تا انتها، در مثال زیر من اطلاعات مربوط به هارد دیسک شماره دو را از ابزار درخواست کردم.

</div>

    $ sudo fdisk -l /sev/sdb

    # OUTPUT
    # Disk /dev/sdb: 931.53 GiB, 1000204886016 bytes, 1953525168 sectors
    # Disk model: WDC WD10EZEX-22M
    # Units: sectors of 1 * 512 = 512 bytes
    # Sector size (logical/physical): 512 bytes / 4096 bytes
    # I/O size (minimum/optimal): 4096 bytes / 4096 bytes
    # Disklabel type: dos
    # Disk identifier: 0x00001727
    # 
    # Device     Boot      Start        End    Sectors   Size Id Type
    # /dev/sdb1  *          2048  195311615  195309568  93.1G 83 Linux
    # /dev/sdb2        195313662 1953523711 1758210050 838.4G  5 Extended
    # /dev/sdb5       1949618176 1953523711    3905536   1.9G 82 Linux swap / Solaris
    # /dev/sdb6        195313664  429686783  234373120 111.8G 83 Linux
    # /dev/sdb7        429688832  624998399  195309568  93.1G 83 Linux
      
   
  
---
<div dir='rtl'>

### حذف کردن پارتیشن خاص

برای حذف کردن یک پارتیشن خاص، ابتدا ابزار را با معرفی هارد خاص خود اجرا کنید، و بعد از اجرا شدن ابزار از کامند d استفاده کنید. در مرحله بعد تعداد پارتیشن ها به شما نمایش داده میشود که بر حسب عدد است. با تایپ عدد مورد نظر پارتیشن شما حذف میشود.فقط دقت داشته باشید که عملیات روی رم در حال اجراست، اگر میخواهید که واقعا عملیات اجرا شود در انتهای انجام کار کامند w را وارد کنید تا تغییرات روی هارد دیوایس شما اعمال شود. 
</div>

    # step 1 
    $ sudo fdisk /dev/sdc

    # OUTPUT
    # Welcome to fdisk (util-linux 2.34).
    # Changes will remain in memory only, until you decide to write them.
    # Be careful before using the write command.
    # 
    # 
    # Command (m for help): 
    

    # step 2 
    $ Enter the d command For delete the partition

    # OUTPUT
    # Command (m for help): d
    # Partition number (1-3, default 3): 


    # step 3 
    $ Enter the partition number For example 1

    # OUTPUT
    # Partition number (1-3, default 3): 1
    # Partition 1 has been deleted.


    # step 4 
    $ Enter the w for apply changes
    
    # OUTPUT
    # Command (m for help): w
    # The partition table has been altered.
    # Failed to remove partition 1 from system: Device or resource busy
    # 
    # The kernel still uses the old partitions. The new table will be used at the next reboot. 
    # Syncing disks.
      
    

  
---
<div dir='rtl'>

### ایجاد پارتیشن
برای ایجاد پارتیشن از کامند n استفاده کنید. بعد از تایپ کامند n از شما سوال پرسیده میشود که مایل به ایجاد پارتیشن primary هستید یا extended . در این مرحله اگر میخواستید که پارتیشن primary ایجاد کنید از کامند p و اگر میخواستید که پارتیشن extended ایجاد کنید از کامند e استفاده کنید. در مرحله بعدی از شما راجب شماره پارتیشن سوال میشود که میتوانید از بازه ی عددی که به شما نشان داده میشود یک عددی را انتخاب کنید. در مرحله بعدی first sector از شما خواسته میشود که بهتر است از ۲۰۴۸ که حالت پیشفرض و بهینه هم هست استفاده کنید. در مرحله بعدی last sector از شما پرسیده میشود که به معنی فضای پارتیشن است . به عنوان مثال میتوانید به ابزار بگویید +6G که مخفف شش گیگابایت میباشد. و در این مرحله کار شما تمام شده است. میتوانید با تایپ کامند w تغییرات را اعمال کنید. 

</div>

    # step 1
    $ sudo fdisk /dev/sdc

    # OUTPUT
    # Welcome to fdisk (util-linux 2.34).
    # Changes will remain in memory only, until you decide to write them.
    # Be careful before using the write command.
    # 
    # 
    # Command (m for help): n
    # Partition type
    # p   primary (0 primary, 0 extended, 4 free)
    # e   extended (container for logical partitions)

    # step 2 
    $ Enter The p Or e for create the partition

    # OUTPUT
    # Partition type
    # p   primary (0 primary, 0 extended, 4 free)
    # e   extended (container for logical partitions)
    # Select (default p): p
    
    # step 3 
    $ Enter the partition number for example 1

    # OUTPUT
    # Partition number (1-4, default 1): 1

    # step 4 
    $ Enter The First Sector , for example 2048

    # OUTPUT
    # First sector (2048-15950591, default 2048): 2048

    # step 5 
    $ Enter The Last Sector , for example +6G

    # OUTPUT
    # Last sector, +/-sectors or +/-size{K,M,G,T,P} (2048-15950591, default 15950591): +6G
    #
    # Created a new partition 1 of type 'Linux' and of size 6 GiB.


    # step 6 
    $ Enter The w for apply changes

    # OUTPUT
    # The partition table has been altered.
    # Failed to add partition 1 to system: Device or resource busy
    # 
    # The kernel still uses the old partitions. The new table will be used at the next reboot. 
    # Syncing disks.
      
      
---
<div dir='rtl'>

### نمایش توضیحات راهنما
هنگام استفاده از ابزار چنانچه دچار مشکل شدید میتوانید از کامند m استفاده کنید. هنگام استفاده از این کامند تمامی کامند های مورد استفاده در ابزار به شما نمایش داده خواهد شد و میتوانید به راحتی عملیات پارتیشن بندی را روی هارد دیوایس انجام دهید.

</div>

    # step 1
    $ Enter The m Command For Help

    # OUTPUT
    # Command (m for help): m
    #
    # Help:
    # 
    #   DOS (MBR)
    #    a   toggle a bootable flag
    #    b   edit nested BSD disklabel
    #    c   toggle the dos compatibility flag
    # 
    #   Generic
    #    d   delete a partition
    #    F   list free unpartitioned space
    #    l   list known partition types
    #    n   add a new partition
    #    p   print the partition table
    #    t   change a partition type
    #    v   verify the partition table
    #    i   print information about a partition
    # 
    #   Misc
    #    m   print this menu
    #    u   change display/entry units
    #    x   extra functionality (experts only)
    # 
    #   Script
    #    I   load disk layout from sfdisk script file
    #    O   dump disk layout to sfdisk script file
    # 
    #   Save & Exit
    #    w   write table to disk and exit
    #    q   quit without saving changes
    # 
    #   Create a new label
    #    g   create a new empty GPT partition table
    #    G   create a new empty SGI (IRIX) partition table
    #    o   create a new empty DOS partition table
    #    s   create a new empty Sun partition table
      
---
<div dir='rtl'>

### همچنین مطالعه کنید

[mkfs](/posts/mkfs/mkfs/)
</div>

---
### Author or Authors

- *[Amirhosein](https://github.com/amirhoseinsb)* | **<amirhoseinsohrabi.official@gmail.com>**
