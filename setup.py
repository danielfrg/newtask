from distutils.core import setup
import py2exe


includes = ['wx']
excludes = []
packages = []
dll_excludes = []
data_files = [
    ('images', ['./images/task.ico']),
    ('images', ['./images/settings.png']),
    ('images', ['./images/settings.ico'])
]

setup(
    data_files=data_files,
        options={"py2exe": {
                        "compressed": 2,
                        "optimize": 2,
                        "includes": includes,
                        "excludes": excludes,
                        "packages": packages,
                        "dll_excludes": dll_excludes,
                        "bundle_files": 3,
                        "dist_dir": "dist",
                        "xref": False,
                        "skip_archive": False,
                        "ascii": False,
                        "custom_boot_script": '',
                    }
                },
        zipfile=None,
        windows=['newtask.py']
)
