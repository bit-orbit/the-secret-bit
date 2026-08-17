---
title: "uname"
date: 2026-08-17T12:14:42+03:30
draft: true
---

<div dir='rtl'>

### فهرست

> - [مقدمه](#مقدمه)
> - [نمایش اطلاعات کلی سیستم](#نمایش-اطلاعات-کلی-سیستم)
> - [نمایش نسخه کرنل](#نمایش-نسخه-کرنل)

> - [Author or Authors](#author-or-authors)

</div>

---

<div dir='rtl'>

### مقدمه

ابزار uname برای چاپ اطلاعات پایه درباره سیستم عامل و سخت‌افزار کامپیوتری که در حال کار با آن هستید، استفاده می‌شود. نام این ابزار مخفف Unix Name است.

</div>

---

<div dir='rtl'>

### نمایش اطلاعات کلی سیستم

با استفاده از سوییچ `a-` (مخفف all) می‌توانید تمام اطلاعات از جمله ورژن کرنل، معماری پردازنده و نام هاست را مشاهده کنید:

<div dir='ltr'>

```bash
$ uname -a
```
</div>

خروجی به این شکل خواهد بود:
<div dir='ltr'>

```text
Linux myserver 5.15.0-78-generic #85-Ubuntu SMP x86_64 x86_64 x86_64 GNU/Linux
```
</div>

</div>

---

<div dir='rtl'>

### نمایش نسخه کرنل

اگر فقط نیاز دارید که نسخه کرنل (Kernel) سیستم عامل را بدانید، از سوییچ `r-` (مخفف release) استفاده کنید:

<div dir='ltr'>

```bash
$ uname -r
```
</div>

</div>

---


---

<div dir='rtl'>

### Author or Authors:

- *[Arya Shabane](https://github.com/shabane)* | **<m.mohamadshabane@gmail.com>**

</div>
