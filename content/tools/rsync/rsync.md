---
title: "rsync"
date: 2026-08-17T12:14:42+03:30
draft: true
---

<div dir='rtl'>

### فهرست

> - [مقدمه](#مقدمه)
> - [کپی کردن دایرکتوری به صورت محلی](#کپی-کردن-دایرکتوری-به-صورت-محلی)
> - [انتقال فایل به یک سرور دیگر](#انتقال-فایل-به-یک-سرور-دیگر)

> - [Author or Authors](#author-or-authors)

</div>

---

<div dir='rtl'>

### مقدمه

ابزار rsync (Remote Sync) ابزاری بی‌نظیر برای کپی و همگام‌سازی (Synchronize) فایل‌ها و دایرکتوری‌هاست. مهم‌ترین ویژگی rsync این است که فقط تفاوت‌ها (Delta) را کپی می‌کند که باعث می‌شود در انتقال فایل‌های حجیم یا بک‌آپ‌گیری، سرعت بسیار بالایی داشته باشد.

</div>

---

<div dir='rtl'>

### کپی کردن دایرکتوری به صورت محلی

برای کپی کامل یک پوشه به همراه تمام محتویات آن به مسیری دیگر (مشابه cp اما هوشمندتر):

<div dir='ltr'>

```bash
$ rsync -av /path/to/source/ /path/to/destination/
```
</div>
سوییچ `a-` برای آرشیو و کپی بازگشتی (recursive) و `v-` برای نمایش فایل‌های در حال انتقال است.

</div>

---

<div dir='rtl'>

### انتقال فایل به یک سرور دیگر

همچنین می‌توانید فایل‌ها را از طریق شبکه به یک سرور دیگر انتقال دهید (rsync از ssh برای انتقال امن استفاده می‌کند):

<div dir='ltr'>

```bash
$ rsync -av /local/dir/ user@remote_host:/remote/dir/
```
</div>

</div>

---


---

<div dir='rtl'>

### Author or Authors:

- *[Arya Shabane](https://github.com/shabane)* | **<m.mohamadshabane@gmail.com>**

</div>
