---
title: "nano"
date: 2022-04-04T01:31:42+04:30
draft: false
---


<div dir='rtl'>

### فهرست

- [فهرست](#فهرست)
- [مقدمه](#مقدمه)
- [باز کردن فایل با ادیتور](#باز-کردن-فایل-با-ادیتور)
- [ذخیره فایل](#ذخیره-فایل)
- [خروج از ادیتور](#خروج-از-ادیتور)
- [نمایش خطوط در کنار هم](#نمایش-خطوط-در-کنار-هم)
- [لیست کردن تمامی دستورات ادیتور](#لیست-کردن-تمامی-دستورات-ادیتور)
- [جستجو در فایل](#جستجو-در-فایل)
- [کپی و کات کردن سریع](#کپی-و-کات-کردن-سریع)
- [برگشتن به کاراکتر قبلی و بعدی](#برگشتن-به-کاراکتر-قبلی-و-بعدی)
- [نمایش انتها و ابتدای خط](#نمایش-انتها-و-ابتدای-خط)
- [جابه جا شدن در فایل](#جابه-جا-شدن-در-فایل)
- [Author or Authors](#author-or-authors)
</div>

---
<div dir='rtl'>

### مقدمه
در گنو/لینوکس ادیتور های زیادی در محیط cli داریم ، که هرکدام بسته به سلیقه و راحتی افراد استفاده میشود. در این بخش شما با ادیتور nano آشنا خواهید شد . کار با این ادیتور بسیار ساده است و حتی افراد مبتدی هم میتوانند به راحتی و در کمترین زمان ممکن فایلهای خود را ویرایش کنند.
</div>


---
<div dir='rtl'>

### باز کردن فایل با ادیتور

برای باز کردن فایل با ادیتور nano کافیست از دستور nano قبل از محل قرار گیری فایل استفاده کنید. لازم به ذکر است بدانید که برای ادیت فایل ها با nano باید حتما دسترسی روت را به ابزار داده باشید زیرا در غیر اینصورت به مشکل خواهید خورد. در پایین محیط ابزار nano را مشاهده میکنید.

</div>

    $ sudo nano /var/log/dmesg
    
       GNU nano 4.8                                                     dmesg                                                           
     [    0.000000] kernel: microcode: microcode updated early to revision 0xb, date = 2007-05-10
     [    0.000000] kernel: Linux version 5.4.0-107-generic (buildd@lcy02-amd64-058) (gcc version 9.4.0 (Ubuntu 9.4.     0-1ubuntu1~20.>
     [    0.000000] kernel: Command line: BOOT_IMAGE=/boot/vmlinuz-5.4.0-107-generic      root=UUID=91309c14-dce5-456f-92d6-f53a170d0fd>
     [    0.000000] kernel: KERNEL supported cpus:
     [    0.000000] kernel:   Intel GenuineIntel
     [    0.000000] kernel:   AMD AuthenticAMD
     [    0.000000] kernel:   Hygon HygonGenuine
     [    0.000000] kernel:   Centaur CentaurHauls
     [    0.000000] kernel:   zhaoxin   Shanghai
     [    0.000000] kernel: x86/fpu: x87 FPU will use FXSAVE
     [    0.000000] kernel: BIOS-provided physical RAM map:
     [    0.000000] kernel: BIOS-e820: [mem 0x0000000000000000-0x000000000009fbff] usable
     [    0.000000] kernel: BIOS-e820: [mem 0x000000000009fc00-0x000000000009ffff] reserved
     [    0.000000] kernel: BIOS-e820: [mem 0x00000000000e4000-0x00000000000fffff] reserved
     [    0.000000] kernel: BIOS-e820: [mem 0x0000000000100000-0x00000000bff8ffff] usable
     [    0.000000] kernel: BIOS-e820: [mem 0x00000000bff90000-0x00000000bff9dfff] ACPI data
     [    0.000000] kernel: BIOS-e820: [mem 0x00000000bff9e000-0x00000000bffdffff] ACPI NVS
     [    0.000000] kernel: BIOS-e820: [mem 0x00000000bffe0000-0x00000000bfffffff] reserved
     [    0.000000] kernel: BIOS-e820: [mem 0x00000000ffb80000-0x00000000ffffffff] reserved
     [    0.000000] kernel: NX (Execute Disable) protection: active
     [    0.000000] kernel: SMBIOS 2.4 present.
     [    0.000000] kernel: DMI: ASUSTek Computer INC. P5PL2-E/P5PL2-E, BIOS 0803    04/13/2007
     [    0.000000] kernel: tsc: Fast TSC calibration using PIT
     [    0.000000] kernel: tsc: Detected 3412.130 MHz processor
     [    0.014557] kernel: e820: update [mem 0x00000000-0x00000fff] usable ==> reserved
     [    0.014561] kernel: e820: remove [mem 0x000a0000-0x000fffff] usable
     [    0.014568] kernel: last_pfn = 0xbff90 max_arch_pfn = 0x400000000
     [    0.014577] kernel: MTRR default type: uncachable
     [    0.014578] kernel: MTRR fixed ranges enabled:
     [    0.014581] kernel:   00000-9FFFF write-back
     [    0.014582] kernel:   A0000-DFFFF uncachable
     [    0.014584] kernel:   E0000-EFFFF write-through
     [    0.014585] kernel:   F0000-FFFFF write-protect
     [    0.014586] kernel: MTRR variable ranges enabled:
     [    0.014589] kernel:   0 base 000000000 mask F80000000 write-back
     [    0.014591] kernel:   1 base 080000000 mask FC0000000 write-back
     
     ^G Get Help    ^O Write Out   ^W Where Is    ^K Cut Text    ^J Justify     ^C Cur Pos     M-U Undo       M-A      Mark Text
     ^X Exit        ^R Read File   ^\ Replace     ^U Paste Text  ^T To Spell    ^_ Go To Line  M-E Redo       M-6      Copy Text



---
<div dir='rtl'>

### ذخیره فایل 
برای ذخیره فایل از کلید ترکیبی ctrl + o استفاده کنید. بعد از استفاده از این کلید ترکیبی کلید اینتر را فشار دهید تا تغییرات شما روی فایل اعمال شود.

</div>

    # select the CTRL + O & Enter for Save the file

---
<div dir='rtl'>

### خروج از ادیتور
برای خروج از ادیتور از کلید ترکیبی ctrl + x استفاده کنید. لازم به ذکر است بدانید اگر فایل را ادیت کرده باشید و تغییرات را ذخیره نکرده باشید هنگام خروج از شما سوال پرسیده میشود که آیا مایل به ذخیره تغییرات هستید یا نه، اگر کلید y را فشار دهید و اینتر بزنید فایل شما ذخیره میشود و از ادیتور خارج میشوید. اما اگر کلید n را فشار دهید تغییرات اعمال نمیشود و از ادیتور خارج میشوید.

</div>

    # select the ctrl + x for exit the editor
---
<div dir='rtl'>

### نمایش خطوط در کنار هم
با استفاده از کلیدهای ترکیبی ctrl + j میتوانید فایل را به شکل justify مشاهده کنید . به اینصورت که خطوط فایل شما در کنار هم قرار خواهند گرفت .

</div>

    $ cat amir.txt
    
    # OUTPUT
    # aalskdfapple
      computer
      linux
      android

    $ select the ctrl + j in nano
    
    # OUTPUT
    # aalskdfapple computer linux android
 
---
<div dir='rtl'>

### لیست کردن تمامی دستورات ادیتور
شما میتوانید با استفاده از کلیدهای ctrl + g تمامی دستورات ادیتور را مشاهده کنید.

</div>

    # View The All Command With ctrl + g
---
<div dir='rtl'>

### جستجو در فایل 
شما میتوانید با استفاده از کلید های ترکیبی ctrl + w در فایل به جستجو بپردازید.

</div>

    # select the ctrl + w For Search in the file
---
<div dir='rtl'>

### کپی و کات کردن سریع

به شکل عادی برای انتخاب کردن یک متن در ادیتور از موس استفاده میکنیم و بعد از انتخاب خط های انتخاب شده با کلید های ctrl + c & ctrl + x خطوط را کپی یا کات میکنیم . در ادیتور nano شما میتوانید با استفاده از کلید های ترکیبی ctrl + 6 حالت انتخاب را فعال کرده و بدون استفاده از موس بخشی از متن را انتخاب، و بعد از انتخاب شما میتوانید با کلید های ctrl + c یا ctrl + x بخش خاص را کپی یا کات کنید.
</div>

    # select the ctrl + 6 for enable mark mod
    # select the text with keyboard
    # copy or cut with select the ctrl + c or ctrl + x
---
<div dir='rtl'>

### برگشتن به کاراکتر قبلی و بعدی

شما میتوانید با استفاده از کلید های ترکیبی Ctrl + f & Ctrl + b به کاراکتر بعدی یا قبلی برگردید. با استفاده از کلیدهای ctrl + f میتوانید به کاراکتر بعدی و با استفاده از کلیدهای ctrl + b به کاراکتر قبلی برگردید.
</div>

    # select the Ctrl + b For Go back one character
    # select the Ctrl + f For Go forward one character
---
<div dir='rtl'>

### نمایش انتها و ابتدای خط

با استفاده از کلیدهای home & end میتوانید انتها و ابتدای خطی که در آن حضور دارید را مشاهده کنید. با استفاده از home میتوانید ابتدای خط و با استفاده از end میتوانید انتهای خط را مشاهده کنید.
</div>
    
    # select the Home for Go to beginning of current line
    # select the End for Go to end of current line
---
<div dir='rtl'>

### جابه جا شدن در فایل 
شما میتوانید با استفاده از دکمه های page down & page up در فایل به بالا و پایین جابه جا شوید. با استفاده از page up به بالای فایل و با استفاده از page down به انتهای فایل مهاجرت کنید. در ضمن اگر از کیبوردهایی استفاده میکنید که فاقد دکمه های گفته شده هستند، میتوانید با کلیدهای ترکیبی ctrl + y و ctrl + v به بالا و پایین فایل مهاجرت کنید. با استفاده از ctrl + y به بالای فایل و با استفاده از ctrl + v میتوانید به انتهای فایل مهاجرت کنید.

</div>

    # select the page up For rull up in file
    # select the page down for rull down in file

    # Or

    # select the ctrl + y for rull up in file
    # select the ctrl + v for rull down in file
---

### Author or Authors

- *[Amirhosein](https://github.com/amirhoseinsb)* | **<amirhoseinsohrabi.official@gmail.com>**
