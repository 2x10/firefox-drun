# firefox-drun
A python script to easily use any dmenu for your firefox profile.

Configure ``config.py`` to your needs:

You can select a firefox binary (e.g. a fork of firefox like librewolf or just ``firefox``)
the path containing your ``profiles.ini`` and then the dmenu command you want to use. 
as long as it will support names seperated by newlines piped into the command it should work with any dmenus working like that.
tested with: ``rofi, wofi``

### Example:
```
config = {
    "firefox_bin"     : "lfirefox",                        # can be a file path too
    "firefox_path"    : "/.config/firefox/profiles.ini",   # it looks in ~ and not actually in /
    "dmenu"           : "wofi --show dmenu",               # any dmenu command should work
}
```
