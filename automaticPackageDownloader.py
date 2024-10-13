import sys
import subprocess

PackageNameToInstall = ['cvzone','opencv-contrib-python','numpy','python-math','pillow','imutils' ]

for element in PackageNameToInstall:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install',f'{element}'])

    reqs = subprocess.check_output([sys.executable, '-m', 'pip',
    'freeze'])
    installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

    print(installed_packages)
