# File sorter

![GitHub last commit](https://img.shields.io/github/last-commit/evil-kekc/file_sorter)
![GitHub repo size](https://img.shields.io/github/repo-size/evil-kekc/file_sorter)
![GitHub pull requests](https://img.shields.io/github/issues-pr/evil-kekc/file_sorter)
![Stars](https://img.shields.io/github/stars/evil-kekc/file_sorter?style=social)

Python script for sorting files into folders by extensions

![til](images/Sorter_example.gif)
## Quick start

1. Clone the [repository](https://github.com/evil-kekc/file_sorter):

```python
git clone https://github.com/evil-kekc/file_sorter --branch develop --single-branch
```

2. Set up a dictionary `subfolder_name_to_extensions` in the [config.py](config.py) for your sorting method.

**Key** - subfolder name, **value** - tuple of file extensions for this subfolder.

```python
subfolder_name_to_extensions = {
    'video': ('mp4', 'mov', 'avi', 'mkv', 'wmv', 'mpg', 'mpeg', 'm4v', 'h264'),
    'audio': ('mp3', 'wav', 'ogg', 'flac', 'aif', 'mid', 'midi', 'wma'),
    'image': ('jpg', 'png', 'bmp', 'jpeg', 'svg', 'tif', 'tiff'),
    'archive': ('zip', 'rar', '7z', 'z', 'gz', 'pkg', 'deb'),
    'text': ('pdf', 'txt', 'doc', 'docx', 'rtf', 'odt'),
    'spreadsheet': ('xlsx', 'xls', 'xlsm'),
    'presentation': ('pptx', 'ppt'),
    'book': ('fb2', 'epub', 'mobi'),
    'gif': ('gif',),
    'torrent': ('torrent',),
    'exe': ('exe',)
}
```

## Logs

You can check the logs in `logs/file_sorter.log` after script execution.

```
[11:49:56] INFO - 33594725.zip ---> archive/33594725.zip
[11:49:56] INFO - 3d графика (1920x1080).jpg ---> image/3d графика (1920x1080).jpg
[11:49:56] INFO - Anketa_14-15.docx ---> text/Anketa_14-15.docx
[11:49:56] INFO - Anketa_16-18.docx ---> text/Anketa_16-18.docx
[11:49:56] INFO - ArmouryCrateInstallTool.zip ---> archive/ArmouryCrateInstallTool.zip
[11:49:56] INFO - ASUSSystemControlInterfacev3_ASUS_Z_V3.1.3.0_14144.exe ---> exe/ASUSSystemControlInterfacev3_ASUS_Z_V3.1.3.0_14144.exe
[11:49:56] INFO - bandicam 2022-08-30 21-01-48-419 (online-video-cutter.com) (1).mp4 ---> video/bandicam 2022-08-30 21-01-48-419 (online-video-cutter.com) (1).mp4
[11:49:56] INFO - bandicam 2022-08-30 21-01-48-419 (online-video-cutter.com) (2).mp4 ---> video/bandicam 2022-08-30 21-01-48-419 (online-video-cutter.com) (2).mp4
[11:49:56] INFO - bandicam 2022-08-30 21-01-48-419 (online-video-cutter.com) (3).mp4 ---> video/bandicam 2022-08-30 21-01-48-419 (online-video-cutter.com) (3).mp4
[11:49:56] INFO - bandicam 2022-08-30 21-01-48-419 (online-video-cutter.com).mp4 ---> video/bandicam 2022-08-30 21-01-48-419 (online-video-cutter.com).mp4
[11:49:56] INFO - bandicam 2022-08-31 12-42-43-361 (online-video-cutter.com).mp4 ---> video/bandicam 2022-08-31 12-42-43-361 (online-video-cutter.com).mp4
[11:49:56] INFO - bandicam 2022-08-31 13-21-55-142 (online-video-cutter.com) (1).mp4 ---> video/bandicam 2022-08-31 13-21-55-142 (online-video-cutter.com) (1).mp4
[11:49:56] INFO - bandicam 2022-08-31 13-21-55-142 (online-video-cutter.com).mp4 ---> video/bandicam 2022-08-31 13-21-55-142 (online-video-cutter.com).mp4
[11:49:56] INFO - CodeGlance-1.5.4.zip ---> archive/CodeGlance-1.5.4.zip
[11:49:56] INFO - drive-download-20220925T141033Z-001.zip ---> archive/drive-download-20220925T141033Z-001.zip
[11:49:56] INFO - GeForce_Experience_v3.25.1.27.exe ---> exe/GeForce_Experience_v3.25.1.27.exe
[11:49:56] INFO - Glossy Black Cubes Marble Madness (1920x1080).jpg ---> image/Glossy Black Cubes Marble Madness (1920x1080).jpg
[11:49:56] INFO - jaba.jpg ---> image/jaba.jpg
[11:49:56] INFO - Linux.png ---> image/Linux.png
[11:49:56] INFO - Matematicheskiye_Golovolomki.pdf ---> text/Matematicheskiye_Golovolomki.pdf
[11:49:56] INFO - MSI Afterburner 4.6.4.16255 Final.exe ---> exe/MSI Afterburner 4.6.4.16255 Final.exe
[11:49:56] INFO - OperaGXSetup.exe ---> exe/OperaGXSetup.exe
[11:49:56] INFO - pycharm-professional-2021.1.exe ---> exe/pycharm-professional-2021.1.exe
[11:49:56] INFO - RefreshRateService_V2.0.8_13230_1.zip ---> archive/RefreshRateService_V2.0.8_13230_1.zip
[11:49:56] INFO - Revo Uninstaller Pro 5.0.6 RePack (& Portable) by TryRooM.zip ---> archive/Revo Uninstaller Pro 5.0.6 RePack (& Portable) by TryRooM.zip
[11:49:56] INFO - tsetup-x64.4.1.0.exe ---> exe/tsetup-x64.4.1.0.exe
[11:49:56] INFO - Windows 10 (1920x1080).jpg ---> image/Windows 10 (1920x1080).jpg
[11:49:56] INFO - Wirelessradiocontroldriver_ASUS_Z_V1.0.0.14_13413.exe ---> exe/Wirelessradiocontroldriver_ASUS_Z_V1.0.0.14_13413.exe
[11:49:56] INFO - [NNMClub.to]_Adobe Acrobat Pro DC 2022.002.20212 RePack by KpoJIuK.torrent ---> torrent/[NNMClub.to]_Adobe Acrobat Pro DC 2022.002.20212 RePack by KpoJIuK.torrent
[11:49:56] INFO - [NNMClub.to]_Adobe Premiere Pro 2022 22.6.0.68 RePack by KpoJIuK.exe.torrent ---> torrent/[NNMClub.to]_Adobe Premiere Pro 2022 22.6.0.68 RePack by KpoJIuK.exe.torrent
[11:49:56] INFO - [NNMClub.to]_Adobe Premiere Pro 22.6 U2B AIO [RiD].dmg.torrent ---> torrent/[NNMClub.to]_Adobe Premiere Pro 22.6 U2B AIO [RiD].dmg.torrent
[11:49:56] INFO - [NNMClub.to]_Bandicam 6.0.1.2003 RePack (& portable) by KpoJIuK (1).torrent ---> torrent/[NNMClub.to]_Bandicam 6.0.1.2003 RePack (& portable) by KpoJIuK (1).torrent
[11:49:56] INFO - [NNMClub.to]_Bandicam 6.0.1.2003 RePack (& portable) by KpoJIuK.torrent ---> torrent/[NNMClub.to]_Bandicam 6.0.1.2003 RePack (& portable) by KpoJIuK.torrent
[11:49:56] INFO - [NNMClub.to]_Bandicam 6.0.2.2018 RePack (& portable) by KpoJIuK (1).torrent ---> torrent/[NNMClub.to]_Bandicam 6.0.2.2018 RePack (& portable) by KpoJIuK (1).torrent
[11:49:56] INFO - [NNMClub.to]_Bandicam 6.0.2.2018 RePack (& portable) by KpoJIuK.torrent ---> torrent/[NNMClub.to]_Bandicam 6.0.2.2018 RePack (& portable) by KpoJIuK.torrent
[11:49:56] INFO - [NNMClub.to]_City Car Driving xatab.torrent ---> torrent/[NNMClub.to]_City Car Driving xatab.torrent
[11:49:56] INFO - [NNMClub.to]_GTA 5 xatab.torrent ---> torrent/[NNMClub.to]_GTA 5 xatab.torrent
[11:49:56] INFO - [NNMClub.to]_Microsoft Office 2016 Pro Plus + Visio Pro + Project Pro VL x86 RePack by SPecialiST V22.8.torrent ---> torrent/[NNMClub.to]_Microsoft Office 2016 Pro Plus + Visio Pro + Project Pro VL x86 RePack by SPecialiST V22.8.torrent
[11:49:56] INFO - [NNMClub.to]_MSI Afterburner 4.6.4.16255 Final.exe.torrent ---> torrent/[NNMClub.to]_MSI Afterburner 4.6.4.16255 Final.exe.torrent
[11:49:56] INFO - [NNMClub.to]_pycharm-professional-2021.1.exe.torrent ---> torrent/[NNMClub.to]_pycharm-professional-2021.1.exe.torrent
[11:49:56] INFO - [NNMClub.to]_WinRAR 6.11 RePack (& Portable) by KpoJIuK.torrent ---> torrent/[NNMClub.to]_WinRAR 6.11 RePack (& Portable) by KpoJIuK.torrent
[11:49:56] INFO - Копия Презентация для друзей.pptx ---> presentation/Копия Презентация для друзей.pptx
[11:49:56] INFO - Логотип (1920x1080).jpg ---> image/Логотип (1920x1080).jpg
[11:49:56] INFO - Основы python.pptx ---> presentation/Основы python.pptx
[11:49:56] INFO - Files sorted: 44
```
