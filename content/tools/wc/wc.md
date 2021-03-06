---
title: "wc"
date: 2021-12-13T14:57:49+03:30
draft: false
tags: [
    "tools",
    "text-processing",
    "program",
    "wc",
    "word-count"
]
---

<div dir='rtl'>

### فهرست

> [نمایش تعداد خط](#نمایش-تعداد-خط)
>
> [نمایش تعداد کلمات](#نمایش-تعداد-کلمات)
>
> [نمایش تعداد کاراکتر](#نمایش-تعداد-کاراکتر)
>
> [پایپ | pipe ](#pipe) 
>
> [نویسنده | نویسندگان](#author-or-authors)

---

### مرور
نام برنامه
wc
مختصر
word count
به معنی شمارش کلمات
است، این برنامه متنی را از ورودی استاندار می‌خواند و یا لیستی از فایل ها را می‌گیرد
و در خروجی با توجه به سوییچ های انتخاب شده تعداد خط های جدید، تعداد کلمات و یا تعداد کاراکتر ها
را نمایش می‌دهد.

---

### نمایش تعداد خط
فرض کنید فایلی به اسم 
`write.txt`
با این محتوا داریم

```bash
hi,
my name is Arya
and im so happy towday
```
برای شمارش تعداد خط های داخل این فایل کافیست
روبروی نام
wc
نام فایل و سوییچ
`-l`
را بنویسیم

```bash
 wc write.txt -l
```
خروجی
```bash
3   write.txt
```

---

### نمایش تعداد کلمات

سوییچ
`-w`
برای شمارش تعداد کلمات استفاده می‌شود

```bash
 wc -w write.txt
```
خروجی
```bash
10  write.txt
```

---

### نمایش تعداد کاراکتر

برای شمارش تعداد کاراکتر های بکار رفته در فایل از سوییچ
`m-`
استفاده می‌شود

```bash
 wc -m write.txt
```
خروجی
```bash
43 write.txt
```

---

### pipe
برنامه
wc
یکی از برنامه هایی است که می‌تواند یک ورودی را از خروجی برنامه‌ای دیگر بوسیله عمگر
pipe
بگیرد. برای مثال فایل 
`write.txt`
را با برنامه
[cat](https://bit-orbit.github.io/the-secret-bit/posts/cat/cat)
می‌خوانیم و خروجی آن را به
wc
پایپ می‌کنیم تا تعداد خط های این فایل را بشمارد.

```bash
cat write.txt | wc -l
```

---

### Author or Authors:

- *[Arya](https://github.com/shabane)* | **<m.mohamadshabane@gmail.com>**

</div>