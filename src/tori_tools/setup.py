import os
from glob import glob
from setuptools import setup

package_name = 'tori_tools'
share_path = os.path.join('share', package_name)

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join(share_path, 'launch'), glob('launch/*.launch.py')),
        (os.path.join(share_path, 'config'), glob('config/*.yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ktaha',
    maintainer_email='ksk.tahara@gmail.com',
    description='Tools for torisuke',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
