---
title: "sed"
date: 2026-08-17T12:14:42+03:30
draft: true
---

<div dir='rtl'>

### فهرست

> - [مقدمه](#مقدمه)
> - [جایگزینی یک کلمه در متن](#جایگزینی-یک-کلمه-در-متن)
> - [جایگزینی تمام کلمات در متن](#جایگزینی-تمام-کلمات-در-متن)

> - [Author or Authors](#author-or-authors)

</div>

---

<div dir='rtl'>

### مقدمه

ابزار sed که مخفف stream editor است، برای ویرایش و پردازش متن‌ها در ترمینال لینوکس استفاده می‌شود. با sed می‌توانید عملیات‌هایی مثل جستجو، جایگزینی (Find and Replace) و حذف بخش‌هایی از متن را بدون نیاز به باز کردن فایل در ادیتور انجام دهید.

</div>

---

<div dir='rtl'>

### جایگزینی یک کلمه در متن

برای جایگزینی کلمه اول یافت شده در هر خط از دستور زیر استفاده کنید:

<div dir='ltr'>

```bash
$ sed 's/old/new/' file.txt
```
</div>

</div>

---

<div dir='rtl'>

### جایگزینی تمام کلمات در متن

اگر بخواهید تمام کلمات یافت شده در یک خط جایگزین شوند، باید از فلگ `g` (global) استفاده کنید.

<div dir='ltr'>

```bash
$ sed 's/old/new/g' file.txt
```
</div>

</div>

---


---

<div dir='rtl'>

### Author or Authors:

- *[Arya Shabane](https://github.com/shabane)* | **<m.mohamadshabane@gmail.com>**

</div>
