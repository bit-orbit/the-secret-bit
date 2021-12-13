---
title: "نحوه مشارکت"
date: 2021-09-15T16:33:15+04:30
draft: false
tags : ["how-to-contribute", "مشارکت"]
---

اگر اینجا هستید یعنی شما هم حرفی برای گفتن دارید.

برای مشارکت ما چند اصول و مفهموم داریم که رعایت آنها باعث می‌شود کتاب با یک ساختار منظم ادامه پیدا کند.

نکته اول اینه که همه فصل ها **قالب** یکسانی دارند. درواقع باید با توجه به یک مدل خاصی از
md
نوشته بشن. با
همکاری شما یک تمپلیت مشخص کردیم. عالی میشه که بر اساس این بنویسید.
ممکنه ابزار ها نیازی به عکس نداشته باشند، ولی اگه نیاز بود دقیقا مثل تمپلیت عکس رو لینک کنید.

فهرست دقیقا یک فهرست برای یک ابزار است، ممکنه یک ابزار موضوعات مختلفی داشته باشد پس سعی کنید موضوعات رو در 
فهرست بنویسید.

و در پایین ترین قسمت بودید **ایمل** و **نامتون** رو به عنوان نویسنده *چپتر* بنویسید.

```md

<div dir='rtl'>

[!["Image Alt"](img src)](Link of image)

فهرست

- [مقدمه](id)
- [قسمت دوم](id)

---

### مقدمه
توضیحات

---

# قسمت اول
توضیحات

---

### قسمت دوم
توضیحات

---

Author or Authors:

- name1 <email@example.com>
- name2 <email2@some.com>

</div>

```

برای شروع باید
[hugo](https://gohugo.io/getting-started/installing/)
را نصب کنید. بعد از نصب، سایت را از
[ریپازیتوری](https://github.com/bit-orbit/the-secret-bit.git)
گیت هاب کلون کنید.

```bash
git clone --recursive https://github.com/bit-orbit/the-secret-bit.git
```

برای درست کردن یک چپتر جدید باید در ریپازیتوری سایت این دستور رو بزنید و
همانطور که می‌دانید جای
NameOfTool
باید نام ابزاری که می‌خواهید دربارش بنویسید را بنویسید.
```bash
hugo new posts/NameOfTool/NameOfTool.md
```
فایل مارک داون هر ابزار در یک پوشه ای به نام خود آن ابزار قرار دارد.
اگر نیاز شد تا فایلی مانند عکس برای یک چپتر قرار دهیم، درون خود پوشه ابزار یک پوشه به همان نام فایل
md
بسازید.
. و عکس ها درون آن قرار بدهید.

```
content/posts/
└── ls
    └── ls.md
    └── ls
        ├── image1.jpg
        ├── image2.png
```

برای مسیر دهی فایل/عکس، کافیه نام و پسوند عکس  را بنویسیم.
```bash
image1.jpg
```

فراموش نکنید که در هدر هر فایل
md
یک لیست از تگ ها وجود دارد، این لیست به راحت تر پیدا شدن ابزار شما کمک میکند، سعی کنید این لیست را به اندازه کافی کامل کنید.

```md
tags : [
    "tool-name",
    "what-it-do",
    "go-on"
    ]
```

از الان شما هم می‌توانید به ما توی کامل تر کردن این کتاب کمک کنید. یادتون باشه که سایت رو بیلد نکنید. فقط فایل هاتون رو که نوشتید پوش کنید. خِرَد یارتون.