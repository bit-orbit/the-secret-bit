---
title: "Nl"
date: 2022-03-07T17:58:20+03:30
draft: false
---

<div dir='rtl'>

### فهرست

- [فهرست](#فهرست)
- [مقدمه](#مقدمه)
- [نمایش شماره خطوط با nl](#نمایش-شماره-خطوط-با-nl)
- [شماره گذاری خطوط خالی](#شماره-گذاری-خطوط-خالی)
- [شمارش خطوط با شماره دلخواه](#شمارش-خطوط-با-شماره-دلخواه)
- [نمایش صفر های ابتدایی حین شمارش](#نمایش-صفر-های-ابتدایی-حین-شمارش)
- [Author or Authors:](#author-or-authors)




</div>

---
<div dir='rtl'>

### مقدمه

ابزار nl ابزاری است برای شمارش خطوط . شما میتوانید با استفاده از این ابزار خطوط فایل خود را شمارش کنید . همچنین با ترکیب این ابزار با ابزارهای دیگر میتوانید کارهای مفیدی با این ابزار انجام دهید.
</div>

---

<div dir='rtl'>

### نمایش شماره خطوط با nl

برای شمارش کردن خطوط فایل با استفاده از ابزار nl کافیست دستور را قبل از فایل قرار دهید.
</div>
$ nl /proc/cpuinfo

     1  processor       : 0
     2  vendor_id       : GenuineIntel
     3  cpu family      : 15
     4  model           : 6
     5  model name      : Intel(R) Pentium(R) 4 CPU 3.40GHz
     6  stepping        : 5
     7  microcode       : 0xb
     8  cpu MHz         : 2400.000
     9  cache size      : 2048 KB
    10  physical id     : 0
    11  siblings        : 2
    12  core id         : 0
    13  cpu cores       : 1
    14  apicid          : 0
    15  initial apicid  : 0
    16  fpu             : yes
    17  fpu_exception   : yes
    18  cpuid level     : 6
    19  wp              : yes
    20  flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx lm constant_tsc pebs bts nopl cpuid pni dtes64 monitor ds_cpl est tm2 cid cx16 xtpr pdcm lahf_lm pti
    21  bugs            : cpu_meltdown spectre_v1 spectre_v2 spec_store_bypass l1tf mds swapgs itlb_multihit
    22  bogomips        : 6824.12
    23  clflush size    : 64
    24  cache_alignment : 128
    25  address sizes   : 36 bits physical, 48 bits virtual
    26  power management:
       
    27  processor       : 1
    28  vendor_id       : GenuineIntel
    29  cpu family      : 15
    30  model           : 6
    31  model name      : Intel(R) Pentium(R) 4 CPU 3.40GHz
    32  stepping        : 5
    33  microcode       : 0xb
    34  cpu MHz         : 3400.000
    35  cache size      : 2048 KB
    36  physical id     : 0
    37  siblings        : 2
    38  core id         : 0
    39  cpu cores       : 1
    40  apicid          : 1
    41  initial apicid  : 1
    42  fpu             : yes
    43  fpu_exception   : yes
    44  cpuid level     : 6
    45  wp              : yes
    46  flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx lm constant_tsc pebs bts nopl cpuid pni dtes64 monitor ds_cpl est tm2 cid cx16 xtpr pdcm lahf_lm pti
    47  bugs            : cpu_meltdown spectre_v1 spectre_v2 spec_store_bypass l1tf mds swapgs itlb_multihit
    48  bogomips        : 6824.12
    49  clflush size    : 64
    50  cache_alignment : 128
    51  address sizes   : 36 bits physical, 48 bits virtual
    52  power management:
       

---

<div dir='rtl'>

### شماره گذاری خطوط خالی
اگر در فایل خود خطوط خالی داشته باشید ابزار آن ها را شمارش نمیکند . برای شمارش خطوط خالی از سوییچ و آپشن  -b a استفاده کنید.
</div>
$ nl -b a /proc/cpuinfo

     1  processor       : 0
     2  vendor_id       : GenuineIntel
     3  cpu family      : 15
     4  model           : 6
     5  model name      : Intel(R) Pentium(R) 4 CPU 3.40GHz
     6  stepping        : 5
     7  microcode       : 0xb
     8  cpu MHz         : 2400.000
     9  cache size      : 2048 KB
    10  physical id     : 0
    11  siblings        : 2
    12  core id         : 0
    13  cpu cores       : 1
    14  apicid          : 0
    15  initial apicid  : 0
    16  fpu             : yes
    17  fpu_exception   : yes
    18  cpuid level     : 6
    19  wp              : yes
    20  flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx lm constant_tsc pebs bts nopl cpuid pni dtes64 monitor ds_cpl est tm2 cid cx16 xtpr pdcm lahf_lm pti
    21  bugs            : cpu_meltdown spectre_v1 spectre_v2 spec_store_bypass l1tf mds swapgs itlb_multihit
    22  bogomips        : 6824.12
    23  clflush size    : 64
    24  cache_alignment : 128
    25  address sizes   : 36 bits physical, 48 bits virtual
    26  power management:
    27
    28  processor       : 1
    29  vendor_id       : GenuineIntel
    30  cpu family      : 15
    31  model           : 6
    32  model name      : Intel(R) Pentium(R) 4 CPU 3.40GHz
    33  stepping        : 5
    34  microcode       : 0xb
    35  cpu MHz         : 3400.000
    36  cache size      : 2048 KB
    37  physical id     : 0
    38  siblings        : 2
    39  core id         : 0
    40  cpu cores       : 1
    41  apicid          : 1
    42  initial apicid  : 1
    43  fpu             : yes
    44  fpu_exception   : yes
    45  cpuid level     : 6
    46  wp              : yes
    47  flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx lm constant_tsc pebs bts nopl cpuid pni dtes64 monitor ds_cpl est tm2 cid cx16 xtpr pdcm lahf_lm pti
    48  bugs            : cpu_meltdown spectre_v1 spectre_v2 spec_store_bypass l1tf mds swapgs itlb_multihit
    49  bogomips        : 6824.12
    50  clflush size    : 64
    51  cache_alignment : 128
    52  address sizes   : 36 bits physical, 48 bits virtual
    53  power management:
    54


---
<div dir='rtl'>

### شمارش خطوط با شماره دلخواه
اگر خواستید که فایل شما با شماره خاصی شمارش شود از سوییچ v استفاده کنید.
</div>
$ nl -v 45 /proc/cpuinfo

    45  processor       : 0
    46  vendor_id       : GenuineIntel
    47  cpu family      : 15
    48  model           : 6
    49  model name      : Intel(R) Pentium(R) 4 CPU 3.40GHz
    50  stepping        : 5
    51  microcode       : 0xb
    52  cpu MHz         : 2400.000
    53  cache size      : 2048 KB
    54  physical id     : 0
    55  siblings        : 2
    56  core id         : 0
    57  cpu cores       : 1
    58  apicid          : 0
    59  initial apicid  : 0
    60  fpu             : yes
    61  fpu_exception   : yes
    62  cpuid level     : 6
    63  wp              : yes
    64  flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx lm constant_tsc pebs bts nopl cpuid pni dtes64 monitor ds_cpl est tm2 cid cx16 xtpr pdcm lahf_lm pti
    65  bugs            : cpu_meltdown spectre_v1 spectre_v2 spec_store_bypass l1tf mds swapgs itlb_multihit
    66  bogomips        : 6824.12
    67  clflush size    : 64
    68  cache_alignment : 128
    69  address sizes   : 36 bits physical, 48 bits virtual
    70  power management:
       
    71  processor       : 1
    72  vendor_id       : GenuineIntel
    73  cpu family      : 15
    74  model           : 6
    75  model name      : Intel(R) Pentium(R) 4 CPU 3.40GHz
    76  stepping        : 5
    77  microcode       : 0xb
    78  cpu MHz         : 3400.000
    79  cache size      : 2048 KB
    80  physical id     : 0
    81  siblings        : 2
    82  core id         : 0
    83  cpu cores       : 1
    84  apicid          : 1
    85  initial apicid  : 1
    86  fpu             : yes
    87  fpu_exception   : yes
    88  cpuid level     : 6
    89  wp              : yes
    90  flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx lm constant_tsc pebs bts nopl cpuid pni dtes64 monitor ds_cpl est tm2 cid cx16 xtpr pdcm lahf_lm pti
    91  bugs            : cpu_meltdown spectre_v1 spectre_v2 spec_store_bypass l1tf mds swapgs itlb_multihit
    92  bogomips        : 6824.12
    93  clflush size    : 64
    94  cache_alignment : 128
    95  address sizes   : 36 bits physical, 48 bits virtual
    96  power management:
---

<div dir='rtl'>

### نمایش صفر های ابتدایی حین شمارش
اگر خواستید که فایل شما با پنج صفر اضافی شمارش شود از سوییچ n و آپشن rz استفاده کنید.
</div>
$ nl -n rz cpuinfo

    000001  processor       : 0
    000002  vendor_id       : GenuineIntel
    000003  cpu family      : 15
    000004  model           : 6
    000005  model name      : Intel(R) Pentium(R) 4 CPU 3.40GHz
    000006  stepping        : 5
    000007  microcode       : 0xb
    000008  cpu MHz         : 2800.000
    000009  cache size      : 2048 KB
    000010  physical id     : 0
    000011  siblings        : 2
    000012  core id         : 0
    000013  cpu cores       : 1
    000014  apicid          : 0
    000015  initial apicid  : 0
    000016  fpu             : yes
    000017  fpu_exception   : yes
    000018  cpuid level     : 6
    000019  wp              : yes
    000020  flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx lm constant_tsc pebs bts nopl cpuid pni dtes64 monitor ds_cpl est tm2 cid cx16 xtpr pdcm lahf_lm pti
    000021  bugs            : cpu_meltdown spectre_v1 spectre_v2 spec_store_bypass l1tf mds swapgs itlb_multihit
    000022  bogomips        : 6824.12
    000023  clflush size    : 64
    000024  cache_alignment : 128
    000025  address sizes   : 36 bits physical, 48 bits virtual
    000026  power management:


---

### Author or Authors:

- *[Amirhosein](https://github.com/amirhoseinsb)* | **<amirhoseinsohrabi.official@gmail.com>**

