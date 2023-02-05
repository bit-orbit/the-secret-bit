---
title: "strace"
tags: [strace]
---
![https://strace.io](https://strace.io/Straus.png)

[strace](https://strace.io)
<div dir='rtl'>

### فهرست

> - [مقدمه](#مقدمه)
> - [فرمت خروجی برنامه](#فرمت-خروجی-برنامه)
> -  [کاربرد ها](#کاربرد-ها)
> -  [برخی از معایب این برنامه](#برخی-از-معایب-این-برنامه)
> -  [کاربرد ها](#کاربرد-ها)
> -  [مثال](#مثال)

---	


# مقدمه

گزارش تمام 
system call
ها و
signal
های ورودی به برنامه.

---

## فرمت خروجی برنامه

هر خط از برنامه یک
system call
بعلاوه آرگومان ها و همچنین مقداری که آن system call برگردانده را نشان می دهد به عنوان مثال:
<div dir='ltr'>

```c
open("/dev/null", O_RDONLY) = 3
```
</div>
سیستم کال open که مقدار بازگشت این فراخوان 3 می باشد.

معمولا 
system call
در صورت مواجه با خطا مقدار
1-
را بر می گردانند و برای مشخص کردن علت خطا یک متغییر global به نام errno را تغییر می دهد تا بفهمیم علت آن خطا چه بوده.
اگر 
system call
ای مقدار
1-
را برگرداند برنامه
strace
مقدار 
errno
را هم نشان می دهد.

<div dir='ltr'>

```c
open("/foo/bar", O_RDONLY) = -1 ENOENT (No such file or directory)
```
</div>

---

## سوئیچ ها


### c-
نشان داده خلاصه ای از سیستم کال های صدا زده شده
<div dir='ltr'>

```
$ strace -c ls > /dev/null
% time     seconds  usecs/call     calls    errors syscall
------ ----------- ----------- --------- --------- ----------------
  0.00    0.000000           0         5           read
  0.00    0.000000           0       152           write
  0.00    0.000000           0        10           close
  0.00    0.000000           0        19           mmap
  0.00    0.000000           0         6           mprotect
  0.00    0.000000           0         1           munmap
  0.00    0.000000           0         3           brk
  0.00    0.000000           0         2           ioctl
  0.00    0.000000           0         4           pread64
  0.00    0.000000           0         2         2 access
  0.00    0.000000           0         1           execve
  0.00    0.000000           0         2         2 statfs
  0.00    0.000000           0         2         1 arch_prctl
  0.00    0.000000           0         1           futex
  0.00    0.000000           0         2           getdents64
  0.00    0.000000           0         1           set_tid_address
  0.00    0.000000           0         8           openat
  0.00    0.000000           0         9           newfstatat
  0.00    0.000000           0         1           set_robust_list
  0.00    0.000000           0         1           prlimit64
  0.00    0.000000           0         1           getrandom
  0.00    0.000000           0         1           rseq
------ ----------- ----------- --------- --------- ----------------
100.00    0.000000           0       234         5 total
```
</div>

---

## کاربرد ها

مهم ترین کاربرد
strace
این است که می توانید هر رابطه و انتقال پیامی بین برنامه های کاربر و کرنل را ببینید.

برای ردگیری race condition ها نیاز دارید که 
system call
ها را رهگیری کنید تا 
bug
برنامه مشخص شود. یا شاید کنجکاو باشید که برنامه شما چه پیام هایی را با کرنل رد و بدل می کند.

strace
در این ضمینه ها می تواند به شما کمک کند.

# برخی از معایب این برنامه
اگر
strace
را برای برنامه های مختلفی اجرا کنید می بینید که حدودا 30 فراخوان اول برای همه برنامه ها یکسان می باشد که این فراخوان ها مربوط به لینک کردن با
dynamic library
ها می باشد از جمله
glibc.
این موضوع باعث شلوغ شدن صفحه می شود و اطلاعات مفیدی هم در اختیار ما نمی گذارد.

### مثال
<div dir='ltr'>

```c
int main(){
return 0;
}
```
</div>
این برنامه را کامپایل کنید به اسم prog1.

حال با دستور:
<div dir='ltr'>

```
$ strace ./prog1
```
</div>
می توانید تمام 
system call
هایی که این برنامه فراخوان می کند را ببینید:
<div dir='ltr'>

```
execve("./simple", ["./simple"], 0x7ffe541a17c0 /* 61 vars */) = 0
brk(NULL)                               = 0x55898aa74000
arch_prctl(0x3001 /* ARCH_??? */, 0x7ffc513cf890) = -1 EINVAL (Invalid argument)
mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f669dfab000
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=131211, ...}, AT_EMPTY_PATH) = 0
mmap(NULL, 131211, PROT_READ, MAP_PRIVATE, 3, 0) = 0x7f669df8a000
close(3)                                = 0
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0P\237\2\0\0\0\0\0"..., 832) = 832
pread64(3, "\6\0\0\0\4\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0"..., 784, 64) = 784
pread64(3, "\4\0\0\0 \0\0\0\5\0\0\0GNU\0\2\0\0\300\4\0\0\0\3\0\0\0\0\0\0\0"..., 48, 848) = 48
pread64(3, "\4\0\0\0\24\0\0\0\3\0\0\0GNU\0i8\235HZ\227\223\333\350s\360\352,\223\340."..., 68, 896) = 68
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=2216304, ...}, AT_EMPTY_PATH) = 0
pread64(3, "\6\0\0\0\4\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0"..., 784, 64) = 784
mmap(NULL, 2260560, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7f669dc00000
mmap(0x7f669dc28000, 1658880, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x28000) = 0x7f669dc28000
mmap(0x7f669ddbd000, 360448, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1bd000) = 0x7f669ddbd000
mmap(0x7f669de15000, 24576, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x214000) = 0x7f669de15000
mmap(0x7f669de1b000, 52816, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7f669de1b000
close(3)                                = 0
mmap(NULL, 12288, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f669df87000
arch_prctl(ARCH_SET_FS, 0x7f669df87740) = 0
set_tid_address(0x7f669df87a10)         = 41210
set_robust_list(0x7f669df87a20, 24)     = 0
rseq(0x7f669df880e0, 0x20, 0, 0x53053053) = 0
mprotect(0x7f669de15000, 16384, PROT_READ) = 0
mprotect(0x558989fc2000, 4096, PROT_READ) = 0
mprotect(0x7f669dfe5000, 8192, PROT_READ) = 0
prlimit64(0, RLIMIT_STACK, NULL, {rlim_cur=8192*1024, rlim_max=RLIM64_INFINITY}) = 0
munmap(0x7f669df8a000, 131211)          = 0
exit_group(0)                           = ?
+++ exited with 0 +++

```
</div>
 برنامه را تغییر می دهیم:
 
<div dir='ltr'>

```c
include<stdlib.h>
int main(){
printf("Hello World!\n");
return 0;
}
```
</div>
که پس از اجرا کردن 
strace
می بینیم
system call
مربوط به آن 
<div dir='ltr'>

`write(1, "Hello World!\n", 13Hello World!)= 13`
</div>
می باشد.
</div>

---

- *[arash attari](https://github.com/arashatt)* | **<attariarash@gmai.com>**

