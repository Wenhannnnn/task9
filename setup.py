import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'gz_example_robot_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Include launch directory
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
        # Include URDF directory
        (os.path.join('share', package_name, 'urdf'), glob(os.path.join('urdf', '*.urdf*')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='DrAndyWest',
    maintainer_email='andrew.west@manchester.ac.uk',
    description='Description file for an example two-wheeled robot.',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
