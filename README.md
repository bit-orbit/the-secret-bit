<div align="center" dir="rtl">

# 🐧 کتاب راز بیت (The Secret Bit)
### دانشنامه آزاد، جامعه‌محور و کاربردی ابزارها و مفاهیم بنیادین لینوکس

[![Website](https://img.shields.io/badge/Website-bit--orbit.github.io-10b981?style=for-the-badge&logo=hugo&logoColor=white)](https://bit-orbit.github.io/the-secret-bit/)
[![Gitab Online](https://img.shields.io/badge/گیتاب-مطالعه_آنلاین_در_گیتاب-8b5cf6?style=for-the-badge&logo=gitbook&logoColor=white)](https://hheydarian.github.io/Gitab/books/book11/)
[![Telegram](https://img.shields.io/badge/Telegram-کانال_تلگرام-229ED9?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/s/bit_orbit)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](https://bit-orbit.github.io/the-secret-bit/nav/contribute/how-to-contribute/)
[![License](https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-lightgrey.svg?style=for-the-badge)](LICENSE)

<br/>

<img src="https://raw.githubusercontent.com/hheydarian/Gitab/master/src/images/the-secret-bit/Cover.jpg" alt="The Secret Bit Cover" width="380" style="border-radius: 14px; box-shadow: 0 16px 36px rgba(0,0,0,0.35);" />

<br/>
<br/>

**«این کتاب با قدرت انگشتان و کیبورد شما نوشته می‌شود؛ امیدوارم شما هم بخشی از این کتاب باشید.»**

</div>

---

<div dir="rtl">

## 📖 درباره کتاب

کتاب **«راز بیت» (The Secret Bit)** احتمالاً نخستین کتاب جامع، آزاد و فارسی در حوزه گنو/لینوکس است که **توسط جامعه، برای جامعه** نوشته می‌شود.

هدف این کتاب صرفاً آموزش نحو و سینتکس خشک دستورات نیست؛ بلکه ایجاد **شناخت و دید درست مهندسی** نسبت به ابزارهاست تا بدانید پشت هر ابزار چه فلسفه‌ای نهفته است، چه زمانی باید به سراغ آن رفت و چگونه می‌توان با اتصال ابزارها (ترکیب خط لوله‌ها و اسکریپت‌نویسی شل)، کارهای بزرگ و پیچیده را در کمترین زمان به سرانجام رساند.

---

## ✨ ویژگی‌های برجسته کتاب

- 🐧 **مفاهیم بنیادین یونیکس:** درک عمیق ساختار مجوزها، لوله‌ها (Pipes)، دستگاه‌های حلقه (Loop Device)، شبانگ (Shebang) و مدیریت حافظه سواپ.
- 🛠️ **بیش از ۶۶ ابزار حیاتی خط فرمان:** بررسی موشکافانه دستورات روزمره و پیشرفته همراه با مثال‌های واقعی و قابل لمس.
- 🤝 **۱۰۰٪ جامعه‌محور و متن‌باز:** نگارش و توسعه مشارکتی با همت توسعه‌دهندگان، ادمین‌های سیستم و علاقه‌مندان لینوکس.
- 📱 **مطالعه آنلاین چندپلتفرمه:** قابل مطالعه هم در وب‌سایت اصلی پروژه و هم بر روی پلتفرم کتابخانه آزاد [گیتاب (Gitab)](https://hheydarian.github.io/Gitab/books/book11/).

---

## 📚 سرفصل‌ها و ساختار کتاب

### ۱. مفاهیم پایه (Linux Fundamentals)
| رديف | سرفصل آموزشی | توضیح کوتاه |
| :---: | :--- | :--- |
| ۱ | [متغیرهای محیطی (Environment Variables)](content/fundamentals/environment%20variables/) | مدیریت متغیرهای سیستمی، PATH و پیکربندی‌های شل |
| ۲ | [دستگاه‌های حلقه (Loop Device)](content/fundamentals/loop-device/) | ماونت کردن فایل‌های ایمیج و دیسک‌های مجازی |
| ۳ | [مجوزها و سطوح دسترسی (Permissions)](content/fundamentals/permissions/) | کنترل دسترسی فایل‌ها، بیت‌های ویژه SUID/SGID/Sticky |
| ۴ | [پایپ و خط لوله (Pipe & Redirection)](content/fundamentals/pipe/) | استریم‌های استاندارد stdin/stdout/stderr و فیلترینگ |
| ۵ | [شبانگ در اسکریپت‌ها (Shebang!)](content/fundamentals/shebang/) | تعیین مفسر فایل‌های اجرایی با `#!/bin/...` |
| ۶ | [فضای سواپ (Swap Space)](content/fundamentals/swap/) | مدیریت پارتیشن و فایل سواپ و بهینه‌سازی حافظه رم |

---

### ۲. ابزارهای خط فرمان لینوکس (Linux CLI Tools — ۶۶ ابزار)

```text
├── مدیریت فایل و دایرکتوری: ls, cd, pwd, mkdir, rmdir, cp, mv, rm, touch, ln
├── مشاهده و پردازش متن:     cat, less, head, tail, grep, sed, awk, cut, tr, sort, uniq, wc, fmt, fold, tee
├── فشرده‌سازی و آرشیو:     tar, gzip
├── جستجو و مکان‌یابی:      find, which, whereis, locate
├── نظارت بر سیستم و منابع: top, htop, btop, free, df, du, uptime
├── مدیریت فرآیندها:         ps, kill, nice, nohup, sleep
├── شبکه و ارتباطات:        curl, ping, ip, ifconfig, netstat, nslookup, ssh
├── دیسک و فایل‌سیستم:       dd, fdisk, fsck, loop-device, swap
├── کاربران و امنیت:        chmod, chown, id, whoami, who, last, passwd, su, sudo
├── سرویس‌ها و زمان‌بندی:    systemctl, cron, date, reboot, shutdown
└── کنترل نسخه:             Git
```

---

## 🌐 نحوه مطالعه کتاب

شما می‌توانید محتوای کامل کتاب را به دو روش آنلاین مطالعه کنید:
1. وب‌سایت رسمی پروژه بر بستر گیت‌هاب پیجز: **[bit-orbit.github.io/the-secret-bit](https://bit-orbit.github.io/the-secret-bit/)**
2. پلتفرم کتابخانه تخصصی گیتاب: **[hheydarian.github.io/Gitab/books/book11](https://hheydarian.github.io/Gitab/books/book11/)**

---

## 🤝 نحوه مشارکت در نوشتن و ویرایش کتاب

جامعه متن‌باز قلب تپنده کتاب «راز بیت» است. شما می‌توانید با نوشتن فصلی جدید برای یک ابزار معرفی‌نشده، افزودن مثال‌های کاربردی به فصل‌های موجود، یا رفع ایرادات نگارشی در این اثر جاودانه سهیم شوید:

1. این مخزن را فورک (Fork) کنید.
2. یک برنچ جدید برای تغییرات خود بسازید:
   ```bash
   git checkout -b feature/new-tool-name
   ```
3. فایل مارک‌داون ابزار مورد نظر را درون پوشه `content/tools/` اضافه یا ویرایش کنید.
4. تغییرات را کامیت کرده و یک Pull Request ارسال فرمایید.

> راهنمای مشروح و استانداردهای نگارش را در صفحه [چگونه مشارکت کنیم؟](https://bit-orbit.github.io/the-secret-bit/nav/contribute/how-to-contribute/) مطالعه فرمایید.

---

## 💻 راه‌اندازی و اجرای لوکال با هیوگو (Hugo)

برای مشاهده پیش‌نمایش محلی سایت:
```bash
# کلون کردن پروژه به همراه زیرماژول‌ها
git clone --recurse-submodules https://github.com/bit-orbit/the-secret-bit.git
cd the-secret-bit

# اجرای سرور توسعه محلی Hugo
hugo server -D
```
سپس آدرس `http://localhost:1313` را در مرورگر باز کنید.

---

## 📬 راه‌های ارتباطی

- **سرپرست و پدیدآورنده:** محمد شبانه ([@shabane](https://github.com/shabane))
- **کانال تلگرام:** [bit_orbit@](https://t.me/s/bit_orbit)
- **ارتباط تلگرام:** [m_shabane@](https://t.me/m_shabane)
- **ایمیل:** `m.mohamadshabane@gmail.com`

---

## ⚖️ مجوز استفاده (License)

استفاده، بازنشر و بهره‌برداری از محتوای این کتاب تحت مجوز **[کرییتیو کامنز (CC BY-NC-SA 4.0)](LICENSE)** آزاد است. فروش چاپی یا دیجیتالی کتاب مجاز نمی‌باشد.

</div>
