---
title: "Head"
date: 2022-03-07T16:13:49+03:30
draft: false
---




<div dir='rtl'>

### فهرست

> - [فهرست](#فهرست)
> - [مقدمه](#مقدمه)
> - [نمایش فایل با head](#نمایش-فایل-با-head)
> - [تغییر مقدار پیش فرض خروجی](#تغییر-مقدار-پیش-فرض-خروجی)
> - [نمایش مقدار مشخصی از فایل به بایت](#نمایش-مقدار-مشخصی-از-فایل-به-بایت)
> - [نمایش خط خاص با ترکیب grep](#نمایش-خط-خاص-با-ترکیب-grep)
> - [Author or Authors](#author-or-authors)
</div>

---

<div dir='rtl'>

### مقدمه


در انگلیسی head به معنای "سر" میباشد و اینجا هم همین معنی را دارد زیرا ابزار head
چند خط ابتدایی فایل را نمایش میدهد . شما میتوانید با استفاده از سوییچ های مختلف ابزار یا ترکیب آن با ابزارهای دیگر از ابزار بهترین استفاده را ببرید.
</div>

---

<div dir='rtl'>

### نمایش فایل با head

برای نمایش ده خط اول یک فایل با استفاده از ابزار head 
head،
کافیست دستور 
را قبل از مسیر فایل خود قرار دهید.

</div>

    $ head cpuinfo 
    # processor       : 0
      vendor_id       : GenuineIntel
      cpu family      : 15
      model           : 6
      model name      : Intel(R) Pentium(R) 4 CPU 3.40GHz
      stepping        : 5
      microcode       : 0xb
      cpu MHz         : 2400.000
      cache size      : 2048 KB
      physical id     : 0

---
<div dir='rtl'>

### تغییر مقدار پیش فرض خروجی

به صورت پیش فرض خروجی ابزار head 
روی ده خط تنظیم شده است. به این معنی که
اگر شما دستور را اجرا کنید خواهید دید که ده خط از فایل شما چاپ شده است. بنابر این اگر خواستید تعداد خط بیشتری در خروجی برای شما چاپ شود باید از سوییچ N استفاده کنید.

</div>

    $ head -n 25 /proc/cpuinfo
    # processor       : 0
      vendor_id       : GenuineIntel
      cpu family      : 15
      model           : 6
      model name      : Intel(R) Pentium(R) 4 CPU 3.40GHz
      stepping        : 5
      microcode       : 0xb
      cpu MHz         : 2400.000
      cache size      : 2048 KB
      physical id     : 0
      siblings        : 2
      core id         : 0
      cpu cores       : 1
      apicid          : 0
      initial apicid  : 0
      fpu             : yes
      fpu_exception   : yes
      cpuid level     : 6
      wp              : yes
      flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr   pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm   pbe syscall nx lm constant_tsc pebs bts nopl cpuid pni dtes64 monitor   ds_cpl est tm2 cid cx16 xtpr pdcm lahf_lm pti
      bugs            : cpu_meltdown spectre_v1 spectre_v2   spec_store_bypass l1tf mds swapgs itlb_multihit
      bogomips        : 6824.12
      clflush size    : 64
      cache_alignment : 128
      address sizes   : 36 bits physical, 48 bits virtual
                    

---
<div dir='rtl'>

### نمایش مقدار مشخصی از فایل به بایت
گاهی اوقات در انجام کارهای پیشرفته با فایل نیاز داریم که مقداری از فایل را به بایت مشاهده کنیم . برای مشاهده مقدار مشخصی از فایل به بایت از سوییچ c استفاده کنید.

</div>

    $ head -c 400 /proc/cpuinfo
    # processor       : 0
      vendor_id       : GenuineIntel
      cpu family      : 15
      model           : 6
      model name      : Intel(R) Pentium(R) 4 CPU 3.40GHz
      stepping        : 5
      microcode       : 0xb
      cpu MHz         : 2400.000
      cache size      : 2048 KB
      physical id     : 0
      siblings        : 2
      core id         : 0
      cpu cores       : 1
      apicid          : 0
      initial apicid  : 0
      fpu             : yes
      fpu_exception   : yes
      cpuid level     : 6
      wp              : yes
      flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr   pge mca cmov   pa                                                           
---

<div dir='rtl'>

### نمایش خط خاص با ترکیب grep

گاهی اوقات نیاز میشود تا در خروجی خط خاصی را جست و جو کنید. با ترکیب head با ابزار grep میتوانید به آسانی خط خاص را در صورت وجود مشاهده کنید.

</div>

    $ head /proc/cpuinfo | grep "model name"
    # model name      : Intel(R) Pentium(R) 4 CPU 3.40GHz
                                

---

### Author or Authors:

- *[Amirhosein](https://github.com/amirhoseinsb)* | **<amirhoseinsohrabi.official@gmail.com>**

