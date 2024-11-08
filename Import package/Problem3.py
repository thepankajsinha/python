# Write a python program to print the contents of a directory using the os module.

import os

directory_path = '/'

contents = os.listdir(directory_path)

for item in contents:
    print(item)


#Output
# $RECYCLE.BIN
# Acer Diagnostic Suite Toolkit_v1.00.3035
# AcerWarrantyRegistration
# Documents and Settings
# DumpStack.log.tmp
# hiberfil.sys
# inetpub
# MinGW
# OEM
# OneDriveTemp
# pagefile.sys
# PerfLogs
# Program Files
# Program Files (x86)
# ProgramData
# Recovery
# swapfile.sys
# System Volume Information
# Users
# Voiceover
# Windows
