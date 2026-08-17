---
title: "systemctl"
date: 2026-08-17T12:14:42+03:30
draft: true
---

<div dir='rtl'>

### فهرست

> - [مقدمه](#مقدمه)
> - [بررسی وضعیت یک سرویس](#بررسی-وضعیت-یک-سرویس)
> - [شروع و توقف سرویس](#شروع-و-توقف-سرویس)

> - [Author or Authors](#author-or-authors)

</div>

---

<div dir='rtl'>

### مقدمه

ابزار systemctl ابزار اصلی برای مدیریت سرویس‌ها در سیستم‌های لینوکسی است که از systemd (مدیر سیستم و سرویس) استفاده می‌کنند. با این ابزار می‌توانید سرویس‌ها را استارت کنید، متوقف کنید، ری‌استارت کنید یا وضعیت آن‌ها را ببینید.

</div>

---

<div dir='rtl'>

### بررسی وضعیت یک سرویس

برای دیدن اینکه یک سرویس (مثلا nginx) در چه وضعیتی است و آیا در حال اجراست یا خیر:

<div dir='ltr'>

```bash
$ systemctl status nginx
```
</div>

</div>

---

<div dir='rtl'>

### شروع و توقف سرویس

برای روشن (start) یا خاموش (stop) کردن سرویس از دستورهای زیر استفاده کنید (معمولا نیاز به دسترسی sudo دارید):

<div dir='ltr'>

```bash
$ sudo systemctl start nginx
$ sudo systemctl stop nginx
```
</div>

</div>

---


---

<div dir='rtl'>

### Author or Authors:

- *[Arya Shabane](https://github.com/shabane)* | **<m.mohamadshabane@gmail.com>**

</div>
