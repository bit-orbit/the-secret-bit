---
title: "cp"
date: 2022-03-04T16:28:45+03:30
draft: false
---

<div dir='rtl'>

[!["cp command in linux"](cp.jpg)](cp.jpg)

### فهرست

> - [مقدمه](#مقدمه)
> - [کپی کردن فایل](#کپی-کردن-فایل)
> - [کپی کردن چندین فایل به یک دایرکتوری](#کپی-کردن-چندین-فایل-به-یک-دایرکتوری)
> - [کپی کردن یک پوشه](#کپی-کردن-یک-پوشه)
> - [دیدن تغییرات](#دیدن-تغییرات)
> - [Author or Authors:](#author-or-authors)

---

### مقدمه

ابزار
cp
یکی پر استفاده ترین ابزار های کامندلاین است.
cp
برای کپی کردن فایل ها و دایرکتوری ها استفاده می‌شود.

---

### کپی کردن فایل

برای کپی کردن یک فایل به یک دایرکتوری دیگر، دو آرگومان نیاز است.
ارگومان اول منبع و دومین آرگومان مقصد.

<div dir='ltr'>

```
# source dest
$ cp /var/log/syslog ~/Desktop/system_logs.log
```
</div>

---

### کپی کردن چندین فایل به یک دایرکتوری

زمانی که نیاز شد چندین فایل را به یک دایرکتوری منتقل کنید، تمام ارگومان های
اولی را به عنوان فایل منبع و آخرین آرگومان را به عنوان دایرکتوری مقصد وارد مشخص می‌کنید.

<div dir='ltr'>

```
$ cp /var/log/syslog /var/log/boot.log /var/log/apt/history.log ~/Destop/logs
```
</div>

---

### کپی کردن یک پوشه

برای کپی کردن یک پوشه از سوییچ
`-r`
استفاده می‌کنیم، این سوییچ تمامی فایل ها و دایرکتوری های داخل پوشه منبع را
به مقصد منتقل می‌کند

<div dir='ltr'>

```
$ cp -r /var/log ~/Desktop/backups
```
</div>

---

### دیدن تغییرات

به صورت پیشفرض زمانی که شما فایلی را کپی می‌کنید
cp
هیچ یک از کپی ها را به شما گزارش نخواهد داد، پس برای اینکه پیشرفت
کپی را ببینید کافی است از سوییچ
`v-`
استفاده کنید.

<div dir='ltr'>

```
$ cp -v -r /var/log/apt /tmp

# '/var/log/apt' -> '/tmp/apt'
# '/var/log/apt/eipp.log.xz' -> '/tmp/apt/eipp.log.xz'
# '/var/log/apt/term.log' -> '/tmp/apt/term.log'
# '/var/log/apt/term.log.1.gz' -> '/tmp/apt/term.log.1.gz'
# '/var/log/apt/history.log' -> '/tmp/apt/history.log'
# '/var/log/apt/history.log.1.gz' -> '/tmp/apt/history.log.1.gz'
# '/var/log/apt/term.log.2.gz' -> '/tmp/apt/term.log.2.gz'
# '/var/log/apt/history.log.2.gz' -> '/tmp/apt/history.log.2.gz'
```

</div>

</div>

---

### Author or Authors:

- *[Arya](https://github.com/shabane)* | **<m.mohamadshabane@gmail.com>**

