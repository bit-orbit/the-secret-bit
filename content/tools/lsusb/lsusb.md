---
title: "lsusb"
date: 2022-03-19T01:18:08+03:30
draft: false
---



<div dir='rtl'>

### فهرست

> - [مقدمه](#مقدمه)
> - [نمایش دستگاه های متصل شده](#نمایش-دستگاه-های-متصل-شده)
> - [نمایش وضعیت پورت ها با جزئیات تکمیلی](#نمایش-وضعیت-پورت-ها-با-جزئیات-تکمیلی)
> - [مانیتور کردن پورت ها به شکل دائم](#مانیتور-کردن-پورت-ها-به-شکل-دائم)
> - [مانیتور کردن پورت خاص](#مانیتور-کردن-پورت-خاص)
> - [نمایش وضعیت پورت ها به شکل درختی](#نمایش-وضعیت-پورت-ها-به-شکل-درختی)
> - [Author or Authors](#author-or-authors)
</div>



---
<div dir='rtl'>

### مقدمه
با استفاده از lsusb میتوانید اطلاعات کاملی راجب وضعیت پورت های usb و دستگاه های متصل شده به آن ها مشاهده کنید.
</div>

---
<div dir='rtl'>

### نمایش دستگاه های متصل شده
برای نمایش دستگاه متصل شده به پورت های یو اس بی کافیست از دستور lsusb استفاده کنید.

</div>

    # show the status usbport
    $ lsusb
    
    #OUTPUT
    # Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    # Bus 005 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
    # Bus 004 Device 010: ID 08bb:2902 Texas Instruments PCM2902 Audio Codec
    # Bus 004 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
    # Bus 003 Device 004: ID 1a2c:2c27 China Resource Semico Co., Ltd USB Keyboard
    # Bus 003 Device 002: ID 30fa:0301  USB OPTICAL MOUSE 
    # Bus 003 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
    # Bus 002 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
      



---
<div dir='rtl'>

### نمایش وضعیت پورت ها با جزئیات تکمیلی
برای نمایش وضعیت پورت ها با جزئیات تکمیلی از سوییچ v- استفاده کنید. با استفاده از این سوییچ میتوانید اطلاعات کاملی راجب پورت و دستگاه متصل شده به آن را مشاهده کنید.

</div>

    # show the complete status usbport
    $ lsusb -v

    # OUTPUT
    # Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    # Couldn't open device, some information will be missing
    # Device Descriptor:
    # bLength                18
    # bDescriptorType         1
    # bcdUSB               2.00
    # bDeviceClass            9 Hub
    # bDeviceSubClass         0 
    # bDeviceProtocol         0 Full speed (or root) hub
    # bMaxPacketSize0        64
    # idVendor           0x1d6b Linux Foundation
    # idProduct          0x0002 2.0 root hub
    # bcdDevice            5.04
    # iManufacturer           3 
    # iProduct                2 
    # iSerial                 1 
    # bNumConfigurations      1
    # Configuration Descriptor:
    # bLength                 9
    # bDescriptorType         2
    # wTotalLength       0x0019
    # bNumInterfaces          1
    # bConfigurationValue     1
    # iConfiguration          0 
    # bmAttributes         0xe0
    #   Self Powered
    #   Remote Wakeup
    # MaxPower                0mA
    # Interface Descriptor:
    #   bLength                 9
    #   bDescriptorType         4
    #   bInterfaceNumber        0
    #   bAlternateSetting       0
    #   bNumEndpoints           1
    #   bInterfaceClass         9 Hub
    #   bInterfaceSubClass      0 
    #   bInterfaceProtocol      0 Full speed (or root) hub
    #   iInterface              0 
    #   Endpoint Descriptor:
    #     bLength                 7
    #     bDescriptorType         5
    #     bEndpointAddress     0x81  EP 1 IN
    #     bmAttributes            3
    #       Transfer Type            Interrupt
    #       Synch Type               None
    #       Usage Type               Data
    #     wMaxPacketSize     0x0004  1x 4 bytes
    #     bInterval              12




---
<div dir='rtl'>

### مانیتور کردن پورت ها به شکل دائم
اگر میخواهید که وضعیت یک پورت یا چند پورت را مانیتور کنید باید به شکل مکرر دستور lsusb را تایپ کنید تا از وضعیت پورت ها مطلع شوید. برای رفع این مشکل از ابزار watch استفاده کنید.
این ابزار تا زمانی که شما کلید های ترکیبی ctrl + c را فشار نداده اید وضعیت را برای شما مانیتور خواهد کرد.

</div>

    # monitor with watch
    $ watch lsusb



---
<div dir='rtl'>

### مانیتور کردن پورت خاص
هر پورت دارای دو شماره است . شماره اول متعلق به پورت و شماره دوم متعلق به دستگاه متصل شده است.
با استفاده از سوییچ s- میتوانید پورت خاص را مانیتور کنید.

</div>

    # monitor the specific usbport
    $ lsusb

    # Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    # Bus 005 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
    # Bus 004 Device 010: ID 08bb:2902 Texas Instruments PCM2902 Audio Codec
    # Bus 004 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
    # Bus 003 Device 004: ID 1a2c:2c27 China Resource Semico Co., Ltd USB Keyboard
    # Bus 003 Device 002: ID 30fa:0301  USB OPTICAL MOUSE 
    # Bus 003 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
    # Bus 002 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub

    $ lsusb -s 5:1
    # Bus 005 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub




---
<div dir='rtl'>

### نمایش وضعیت پورت ها به شکل درختی
با استفاده از سوییچ t- میتوانید وضعیت پورت ها را به شکل درختی مانیتور کنید.

</div>

    $ lsusb -t
    
    # OUTPUT
    # /:  Bus 05.Port 1: Dev 1, Class=root_hub, Driver=uhci_hcd/2p, 12M
    # /:  Bus 04.Port 1: Dev 1, Class=root_hub, Driver=uhci_hcd/2p, 12M
    #     |__ Port 1: Dev 10, If 0, Class=Audio, Driver=snd-usb-audio, 12M
    #     |__ Port 1: Dev 10, If 1, Class=Audio, Driver=snd-usb-audio, 12M
    #     |__ Port 1: Dev 10, If 2, Class=Audio, Driver=snd-usb-audio, 12M
    #     |__ Port 1: Dev 10, If 3, Class=Human Interface Device, Driver=usbhid, 12M
    # /:  Bus 03.Port 1: Dev 1, Class=root_hub, Driver=uhci_hcd/2p, 12M
    #     |__ Port 1: Dev 2, If 0, Class=Human Interface Device, Driver=usbhid, 1.5M
    #     |__ Port 2: Dev 4, If 0, Class=Human Interface Device, Driver=usbhid, 1.5M
    #     |__ Port 2: Dev 4, If 1, Class=Human Interface Device, Driver=usbhid, 1.5M
    # /:  Bus 02.Port 1: Dev 1, Class=root_hub, Driver=uhci_hcd/2p, 12M
    # /:  Bus 01.Port 1: Dev 1, Class=root_hub, Driver=ehci-pci/8p, 480M




---
### Author or Authors

- *[Amirhosein](https://github.com/amirhoseinsb)* | **<amirhoseinsohrabi.official@gmail.com>**
