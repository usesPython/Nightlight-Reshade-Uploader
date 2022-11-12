# Nightlight Reshade Uploader
## Setup Guide
### Step 1: Download the .exe
Download the latest nightlight_upload.exe from https://github.com/usesPython/Nightlight-Reshade-Uploader/releases/tag/release and save it somewhere

### Step 2: Get a Nightlight API key
Go to https://nightlight.gg/account/api and make a new API token, making sure to give it upload permissions. Copy the API key you get when you generate it, you'll need it later

### Step 3: Setup Reshade to interface with the .exe
In the settings tab of Reshade, scroll down to Screenshots.

Set Screenshot path to be a folder you want screenshots to be stored in locally

Set Screenshot name to be %DateYear%%DateMonth%%DateDay%%TimeHour%%TimeMinute%%TimeSecond%

Set Screenshot format to be .png or .jpeg (Haven't tested .jpeg but should work, if it doesn't switch to .png)

Set Post-save command to be the path to nightlight_upload.exe

Set Post-save command working directory to be the same as Screenshot path

#### IF YOU ARE USING RESHADE FILTERS

Make sure that "Save before and after images" is ticked

Set Post-save command arguments to be --delete-non-original -a=YOUR_API_KEY %DateYear%%DateMonth%%DateDay%%TimeHour%%TimeMinute%%TimeSecond%.png

#### IF YOU ARE NOT USING RESHADE FILTERS

Make sure that "Save before and after images" in unticked

Set Post-save command arguments to be -a=YOUR_API_KEY %DateYear%%DateMonth%%DateDay%%TimeHour%%TimeMinute%%TimeSecond%.png

#### Example of how it should look like configured for reshade filters:
![Example settings](/images/example_settings.png)

## Building from the source code
If you're a regular user you can skip this part and just grab the .exe from https://github.com/usesPython/Nightlight-Reshade-Uploader/releases/tag/release

This assumes you have a working version of Python set up, get the requests library with
```
pip install requests
```
and get auto-py-to-exe with
```
pip install auto-py-to-exe
```
After that, run
```
auto-py-to-exe
```
Set Script Location to the path to nightlight_upload.py

Set Onefile to One File

Set Console Window to Window Based

Set Ouput Directory in Settings to the directory you want to build in

Press Convert .py to .exe
