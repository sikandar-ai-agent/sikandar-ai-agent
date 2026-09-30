[app]
# (str) Title of your application
title = Mera AI Agent

# (str) Package name
package.name = sikandaraiagent
package.domain = org.sikandar

# (str) Source code where the main.py live
source.dir = .

# (str) Source code where the result of install
source.include_exts = py,png,jpg,kv,atlas

# (str) Application version
version = 0.1

# (list) Application requirements

requirements = python3,kivy==2.3.0,sdl2,cython==3.0.8

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) The Android arch to build for, only armeabi-v7a is supported for now
android.archs = arm64-v8a

# (int) Target Android API, should be as high as possible.
android.api = 35

# (int) Minimum Android API required
android.minapi = 24

# (list) Android permissions
android.permissions = INTERNET

# (list) Path to a custom buildozer.spec
#spec.filename = %(source.dir)s/buildozer.spec

# (bool) If True, then logcat will be shown
log_level = 2

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (default))
log_level = 2

# (int) Display earth date
warn_on_root = 1

