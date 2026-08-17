---
title: "ip"
date: 2026-08-17T12:14:42+03:30
draft: true
---

<div dir='rtl'>

### فهرست

> - [مقدمه](#مقدمه)
> - [نمایش آدرس IP سیستم](#نمایش-آدرس-IP-سیستم)
> - [نمایش جدول مسیریابی (Routing)](#نمایش-جدول-مسیریابی-(Routing))

> - [Author or Authors](#author-or-authors)

</div>

---

<div dir='rtl'>

### مقدمه

ابزار ip دستوری قدرتمند برای پیکربندی و نمایش تنظیمات شبکه در لینوکس است. این ابزار جایگزین مدرن‌تری برای دستور قدیمی `ifconfig` محسوب می‌شود و امکانات بسیار بیشتری در زمینه مسیریابی (Routing) و اینترفیس‌های شبکه دارد.

</div>

---

<div dir='rtl'>

### نمایش آدرس IP سیستم

برای دیدن آدرس IP تمام کارت شبکه‌های سیستم خود از دستور زیر استفاده کنید:

<div dir='ltr'>

```bash
$ ip addr show
```
</div>
یا به صورت خلاصه:
<div dir='ltr'>

```bash
$ ip a
```
</div>

</div>

---

<div dir='rtl'>

### نمایش جدول مسیریابی (Routing)

برای دیدن روت‌ها و Default Gateway سیستم می‌توانید از کامند زیر استفاده کنید:

<div dir='ltr'>

```bash
$ ip route show
```
</div>

</div>

---


---

<div dir='rtl'>

### Author or Authors:

- *[Arya Shabane](https://github.com/shabane)* | **<m.mohamadshabane@gmail.com>**

</div>
