"""Make file to package the Pyms application as a windows app and then create a windows deistribution packahe
uses:
pyinstaller_versionfile to create the version text files ina windows format
pyinstaller to build the windows executables
sourceforge to create a windows setupfile """

import os
import shutil
from datetime import datetime
import pyinstaller_versionfile
import PyInstaller.__main__
from app_control import VERSION
from document_from_code import create_docs

starttime = datetime.now()

print('Creating documentation from code')
create_docs()

print('Starting build for Version: %s' % VERSION)



# set version information
winver = '%s.0' % VERSION
print('Updating version info in build files to %s' % winver)


pyinstaller_versionfile.create_versionfile(
    output_file="pyms-version.txt",
    version=winver,
    company_name="Gary Twinn",
    file_description="PyMS Main application",
    internal_name="PyMSapp",
    legal_copyright="© Gary Twinn. All rights reserved.",
    original_filename="PyMSapp.exe",
    product_name="Python Mass Spectrometry",
    translations=[0, 1200]
)
print('Finished updating version info in pyms-version.txt')


pyinstaller_versionfile.create_versionfile(
    output_file="ncc-version.txt",
    version=winver,
    company_name="Gary Twinn",
    file_description="PyMS Ncc file viewer and calculator",
    internal_name="NccViewer",
    legal_copyright="© Gary Twinn. All rights reserved.",
    original_filename="NccViewer.exe",
    product_name="Python Mass Spectrometry",
    translations=[0, 1200]
)
print('Finished updating version info in ncc-version.txt')

pyinstaller_versionfile.create_versionfile(
    output_file="cycle-version.txt",
    version=winver,
    company_name="Gary Twinn",
    file_description="PyMS cycle editor",
    internal_name="CycleEditor",
    legal_copyright="© Gary Twinn. All rights reserved.",
    original_filename="CycleEditor.exe",
    product_name="Python Mass Spectrometry",
    translations=[0, 1200]
)
print('Finished updating version info in cycle-version.txt')

pyinstaller_versionfile.create_versionfile(
    output_file="testgen-version.txt",
    version=winver,
    company_name="Gary Twinn",
    file_description="PyMS test application",
    internal_name="PyMS",
    legal_copyright="© Gary Twinn. All rights reserved.",
    original_filename="testgen.exe",
    product_name="Python Mass Spectrometry",
    translations=[0, 1200]
)
print('Finished updating version info in testgen-version.txt')

pyinstaller_versionfile.create_versionfile(
    output_file="pyms-laserviewer.txt",
    version=winver,
    company_name="Gary Twinn",
    file_description="PyMS Laser Camera Viewer Application",
    internal_name="PyMSLV",
    legal_copyright="© Gary Twinn. All rights reserved.",
    original_filename="PyMSLV.exe",
    product_name="Python Mass Spectrometry",
    translations=[0, 1200]
)
print('Finished updating version info in pyms-version.txt')

if not os.path.exists('..\\distribution'):
    os.makedirs('..\\distribution')

package_data = []
with open("package.ifp", "r", encoding='utf-8') as packagefile:
    for line in packagefile:
        package_data.append(line)
packagefile.close()

with open("package.ifp", "w", encoding='utf-8') as packagefile:
    for line in package_data:
        if line[:15] == 'Program version':
            line = 'Program version = %s\n' % VERSION
        packagefile.write(line)
packagefile.close()


# run pyinstaller
print('Starting Pyinstaller - this may take some time only warn logs are output')

PyInstaller.__main__.run(['package.spec', '--noconfirm', '--log-level=WARN'])

print('Pyinstaller Completed')

print('copying json files for testing')
shutil.copy('..\\settings.json', '.\\dist\\PyMS')
shutil.copy('..\\alerts.json', '.\\dist\\PyMS')
print('copy completed')

print('Starting Installforge')
os.system('package.ifp')
print('make script finished after %s seconds' % (datetime.now() - starttime).seconds)
