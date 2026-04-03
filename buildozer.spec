[app]
title = Exzo AI
package.name = exzoai
package.domain = org.jaili
source.dir = .
source.include_exts = py,png,jpg,json,ttf
version = 1.0

# المتطلبات الصارمة لضمان التشغيل
requirements = python3, kivy==2.1.0, kivymd, pyjnius, android, certifi, arabic-reshaper, python-bidi

orientation = portrait
fullscreen = 1

# معمارية الموبايلات الحديثة
android.archs = arm64-v8a
android.api = 31
android.minapi = 21

# أهم سطر: صلاحيات الميكروفون
android.permissions = RECORD_AUDIO, INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# لمنع الكراش عند الفتح
android.accept_sdk_license = True
android.skip_update = False
