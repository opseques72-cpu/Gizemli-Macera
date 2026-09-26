[app]
title = Gizemli Macera
package.name = gizemli_macera
package.domain = org.gizemli
source.dir = .
source.include_exts = py,png,wav,json
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 1
android.api = 35
android.minapi = 23
android.archs = arm64-v8a, armeabi-v7a
android.permissions = VIBRATE

[buildozer]
log_level = 2
warn_on_root = 0

[app:android]
android.add_src =
android.gradle_dependencies =
android.enable_androidx = True