---
title: "Git"
date: 2021-09-17T14:20:01+04:30
tags: ['git', 'VCS', ]
draft: true
---


<div dir='rtl'>

### فهرست

> - [مقدمه](#مقدمه)
> - [وارد کردن گیت به داخل پروژه](#وارد-کردن-گیت-به-داخل-پروژه)
> - [بررسی وضعیت فایل های پروژه](#بررسی-وضعیت-فایل-های-پروژه)
</div>

---
### مقدمه
گیت یک سیستم کنترل ورژن
(VCS)
میباشد.ما سیستم های کنترل ورژن زیادی داریم اما در این بین امروزه گیت محبوبترین آنهاست.گیت در سال 2005 توسط لینوس توروالدز خالق کرنل لینوکس ساخته و بصورت اوپن سورس منتشر شد.

---
### وارد کردن گیت به داخل پروژه
برای کار کردن و استفاده از گیت ابتدا باید آن را وارد پروژه کرد.با دستور زیر در فایل های پروژه شما یک پوشه
```.git```
ساخته میشود و به این ترتیب گیت وارد پروژه شما میشود.
</div>
    
    $ git init                             
    # Initialized empty Git repository in <your folder path>/.git/
 
---
<div dir='rtl'>

### بررسی فایل های پروژه
برای اینکه وضعیت پروژه را بررسی کنیم((از نظر اینکه چه فایل های جدیدی به پروژه اضافه شدند یا فایل هایی که از قبل در پروژه بودند محتوایشان تغغیری کرده یا نه از دستور زیر استفاده میکنیم

</div>
    
    $ git status                       
    # On branch main
    Your branch is up to date with 'origin/main'.

    Changes not staged for commit:
      (use "git add <file>..." to update what will be committed)
      (use "git restore <file>..." to discard changes in working directory)
            modified:   <file name>

    Untracked files:
      (use "git add <file>..." to include in what will be committed)
            <file name>

    no changes added to commit (use "git add" and/or "git commit -a")
 
---
<div dir='rtl'>
    

---
Author or Authors: Shahriar Ghasempour

- Email: <shahriaarrr@gmail.com>
