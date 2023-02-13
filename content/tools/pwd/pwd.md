---
title: "Pwd"
date: 2023-02-13T16:40:56+03:30
draft: true
---


<div dir='rtl'>

### فهرست

> - [مقدمه](#مقدمه)
> - [مسیر لاجیکال](#مسیر-لاجیکال)
> - [مسیر فیزیکال](#مسیر-فیزیکال)
> - [Author or Authors](#author-or-authors)
</div>

---
<div dir='rtl'>

### مقدمه
با استفاده از ابزار pwd می‌توان نام کامل مسیری که در حال حاضر در آن هستید را پرینت کنید.

> PWD: print working directory
</div>

```
$ pwd
# /home/mehdi/Desktop
```

---
<div dir='rtl'>

### مسیر لاجیکال

با استفاده از گزینه L- یا logical-- می‌توانید مسیر جاری را از env لینوکس پرینت کنید که از مقدار PWD در environment ذخیره می‌شود، می‌خواند.

</div>

```
$ pwd -L
# /home/mehdi/Desktop
```

---
<div dir='rtl'>

### مسیر فیزیکال

با استفاده از گزینه P- یا physical-- می‌توانید مسیر جاری را بدون در درنظر گرفتن هیچ کدوم از symlinksها پرینت کنید.
</div>
{{< note >}}

<div dir='rtl'>
این گزینه مقدار پیش‌فرض دستور pwd است.
</div>

{{< /note >}}

```
$ pwd -P
# /home/mehdi/Desktop
```

---


### Author or Authors:

- *[Mehdi](https://github.com/mahdimmr)* | **<mahdi.rezayi76@gmail.com>**

