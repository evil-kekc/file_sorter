# File sorter

![GitHub last commit](https://img.shields.io/github/last-commit/evil-kekc/file_sorter)
![GitHub repo size](https://img.shields.io/github/repo-size/evil-kekc/file_sorter)
![GitHub pull requests](https://img.shields.io/github/issues-pr/evil-kekc/file_sorter)
![Stars](https://img.shields.io/github/stars/evil-kekc/file_sorter?style=social)

Python script for sorting files into folders by extensions

## Quick start

1. Open [config.py](config.py) and write the path to the folder where the sort will be performed:

```python
folder_path = Path('drive:/folder/another-folder/yet-another-folder')
```

Example

```python
folder_path = Path(r'X:\test')
```

2. Set up a dictionary `subfolder_name_to_extensions` for your sorting method.

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
    # 'subfolder-name': ('extension', 'another-extension')
}
```

## Logs

You can check the logs in `logs/file_sorter.log` after script execution.

```
[12:15:43] INFO - 33594725.zip ---> archive/33594725.zip
[12:15:43] INFO - 3d графика (1920x1080).jpg ---> image/3d графика (1920x1080).jpg
[12:15:43] INFO - Anketa_14-15.docx ---> text/Anketa_14-15.docx
[12:15:43] INFO - Anketa_16-18.docx ---> text/Anketa_16-18.docx
[12:15:43] INFO - ArmouryCrateInstallTool.zip ---> archive/ArmouryCrateInstallTool.zip
[12:15:43] INFO - ASUSSystemControlInterfacev3_ASUS_Z_V3.1.3.0_14144.exe ---> exe/ASUSSystemControlInterfacev3_ASUS_Z_V3.1.3.0_14144.exe
[12:15:43] INFO - bandicam 2022-08-30 21-01-48-419 (online-video-cutter.com) (1).mp4 ---> video/bandicam 2022-08-30 21-01-48-419 (online-video-cutter.com) (1).mp4
[12:15:43] INFO - bandicam 2022-08-30 21-01-48-419 (online-video-cutter.com) (2).mp4 ---> video/bandicam 2022-08-30 21-01-48-419 (online-video-cutter.com) (2).mp4
[12:15:43] INFO - bandicam 2022-08-30 21-01-48-419 (online-video-cutter.com) (3).mp4 ---> video/bandicam 2022-08-30 21-01-48-419 (online-video-cutter.com) (3).mp4
[12:15:43] INFO - bandicam 2022-08-30 21-01-48-419 (online-video-cutter.com).mp4 ---> video/bandicam 2022-08-30 21-01-48-419 (online-video-cutter.com).mp4
[12:15:43] INFO - bandicam 2022-08-31 12-42-43-361 (online-video-cutter.com).mp4 ---> video/bandicam 2022-08-31 12-42-43-361 (online-video-cutter.com).mp4
[12:15:43] INFO - bandicam 2022-08-31 13-21-55-142 (online-video-cutter.com) (1).mp4 ---> video/bandicam 2022-08-31 13-21-55-142 (online-video-cutter.com) (1).mp4
[12:15:43] INFO - bandicam 2022-08-31 13-21-55-142 (online-video-cutter.com).mp4 ---> video/bandicam 2022-08-31 13-21-55-142 (online-video-cutter.com).mp4
[12:15:43] INFO - bandicam 2022-09-27 11-49-52-875.gif ---> gif/bandicam 2022-09-27 11-49-52-875.gif
[12:15:43] INFO - CodeGlance-1.5.4.zip ---> archive/CodeGlance-1.5.4.zip
[12:15:43] INFO - drive-download-20220925T141033Z-001.zip ---> archive/drive-download-20220925T141033Z-001.zip
[12:15:43] INFO - GeForce_Experience_v3.25.1.27.exe ---> exe/GeForce_Experience_v3.25.1.27.exe
[12:15:43] INFO - Glossy Black Cubes Marble Madness (1920x1080).jpg ---> image/Glossy Black Cubes Marble Madness (1920x1080).jpg
[12:15:43] INFO - jaba.jpg ---> image/jaba.jpg
[12:15:43] INFO - Linux.png ---> image/Linux.png
[12:15:43] INFO - Matematicheskiye_Golovolomki.pdf ---> text/Matematicheskiye_Golovolomki.pdf
[12:15:43] INFO - MSI Afterburner 4.6.4.16255 Final.exe ---> exe/MSI Afterburner 4.6.4.16255 Final.exe
[12:15:43] INFO - OperaGXSetup.exe ---> exe/OperaGXSetup.exe
[12:15:43] INFO - pycharm-professional-2021.1.exe ---> exe/pycharm-professional-2021.1.exe
[12:15:43] INFO - RefreshRateService_V2.0.8_13230_1.zip ---> archive/RefreshRateService_V2.0.8_13230_1.zip
[12:15:43] INFO - Revo Uninstaller Pro 5.0.6 RePack (& Portable) by TryRooM.zip ---> archive/Revo Uninstaller Pro 5.0.6 RePack (& Portable) by TryRooM.zip
[12:15:43] INFO - tsetup-x64.4.1.0.exe ---> exe/tsetup-x64.4.1.0.exe
[12:15:43] INFO - Use_example.gif ---> gif/Use_example.gif
[12:15:43] INFO - Windows 10 (1920x1080).jpg ---> image/Windows 10 (1920x1080).jpg
[12:15:43] INFO - Wirelessradiocontroldriver_ASUS_Z_V1.0.0.14_13413.exe ---> exe/Wirelessradiocontroldriver_ASUS_Z_V1.0.0.14_13413.exe
[12:15:43] INFO - [NNMClub.to]_Adobe Acrobat Pro DC 2022.002.20212 RePack by KpoJIuK.torrent ---> torrent/[NNMClub.to]_Adobe Acrobat Pro DC 2022.002.20212 RePack by KpoJIuK.torrent
[12:15:43] INFO - [NNMClub.to]_Adobe Premiere Pro 2022 22.6.0.68 RePack by KpoJIuK.exe.torrent ---> torrent/[NNMClub.to]_Adobe Premiere Pro 2022 22.6.0.68 RePack by KpoJIuK.exe.torrent
[12:15:43] INFO - [NNMClub.to]_Adobe Premiere Pro 22.6 U2B AIO [RiD].dmg.torrent ---> torrent/[NNMClub.to]_Adobe Premiere Pro 22.6 U2B AIO [RiD].dmg.torrent
[12:15:43] INFO - [NNMClub.to]_Bandicam 6.0.1.2003 RePack (& portable) by KpoJIuK (1).torrent ---> torrent/[NNMClub.to]_Bandicam 6.0.1.2003 RePack (& portable) by KpoJIuK (1).torrent
[12:15:43] INFO - [NNMClub.to]_Bandicam 6.0.1.2003 RePack (& portable) by KpoJIuK.torrent ---> torrent/[NNMClub.to]_Bandicam 6.0.1.2003 RePack (& portable) by KpoJIuK.torrent
[12:15:43] INFO - [NNMClub.to]_Bandicam 6.0.2.2018 RePack (& portable) by KpoJIuK (1).torrent ---> torrent/[NNMClub.to]_Bandicam 6.0.2.2018 RePack (& portable) by KpoJIuK (1).torrent
[12:15:43] INFO - [NNMClub.to]_Bandicam 6.0.2.2018 RePack (& portable) by KpoJIuK.torrent ---> torrent/[NNMClub.to]_Bandicam 6.0.2.2018 RePack (& portable) by KpoJIuK.torrent
[12:15:43] INFO - [NNMClub.to]_City Car Driving xatab.torrent ---> torrent/[NNMClub.to]_City Car Driving xatab.torrent
[12:15:43] INFO - [NNMClub.to]_GTA 5 xatab.torrent ---> torrent/[NNMClub.to]_GTA 5 xatab.torrent
[12:15:43] INFO - [NNMClub.to]_Microsoft Office 2016 Pro Plus + Visio Pro + Project Pro VL x86 RePack by SPecialiST V22.8.torrent ---> torrent/[NNMClub.to]_Microsoft Office 2016 Pro Plus + Visio Pro + Project Pro VL x86 RePack by SPecialiST V22.8.torrent
[12:15:43] INFO - [NNMClub.to]_MSI Afterburner 4.6.4.16255 Final.exe.torrent ---> torrent/[NNMClub.to]_MSI Afterburner 4.6.4.16255 Final.exe.torrent
[12:15:43] INFO - [NNMClub.to]_pycharm-professional-2021.1.exe.torrent ---> torrent/[NNMClub.to]_pycharm-professional-2021.1.exe.torrent
[12:15:43] INFO - [NNMClub.to]_WinRAR 6.11 RePack (& Portable) by KpoJIuK.torrent ---> torrent/[NNMClub.to]_WinRAR 6.11 RePack (& Portable) by KpoJIuK.torrent
[12:15:43] INFO - Копия Презентация для друзей.pptx ---> presentation/Копия Презентация для друзей.pptx
[12:15:43] INFO - Логотип (1920x1080).jpg ---> image/Логотип (1920x1080).jpg
[12:15:43] INFO - Основы python.pptx ---> presentation/Основы python.pptx
[12:15:43] INFO - Files sorted: 46
```

