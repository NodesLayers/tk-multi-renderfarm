#!/usr/bin/env python
#
# Copyright (c) 2022 Nodes&Layers Ltd.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.
#
#################################
# USAGE:                        #
#################################
# Python 3.7 - PySide2 required
# Install PySide2 to your Virtual Environment!
#

import os
import fileinput

# The path to output all built .py files to:
UI_PYTHON_PATH = "../python/app/ui"
current_dir = os.path.dirname(__file__)


# Helper functions to build UI files
def build_py(ui_name):
    print("Building {}...".format(ui_name))

    ui_path = os.path.join(current_dir, ui_name + ".ui").replace("\\", "/")
    print(ui_path)
    python_path = os.path.join(os.path.dirname(current_dir), "python", "app", "ui", ui_name + ".py").replace("\\", "/")
    print(python_path)

    # compile ui to python
    cmd = 'pyside2-uic --from-imports "{}" -o "{}"'.format(ui_path, python_path)
    print(cmd)
    os.system(cmd)

    # replace PySide imports with tank.platform.qt and remove line containing Created by date
    # echo 'sed -i "" -e "s/from PySide import/from tank.platform.qt import/g" -e "/# Created:/d" '
    # echo $UI_PYTHON_PATH/$3.py
    # find_replace_in_file(python_path, {
    #     "from PySide import": "from tank.platform.qt import",
    #     "Ui_Dialog(object)": "Ui_Dialog(QtWidgets.QWidget)",
    #     "from PySide2.QtCore import *": "from tank.platform.qt5 import QtCore",
    #     "from PySide2.QtGui import *": "from tank.platform.qt5 import QtGui",
    #     "from PySide2.QtWidgets import *": "from tank.platform.qt5 import QtWidgets",
    # })

    # find_replace_in_file(python_path, {
    #     "from PySide2.QtGui import *": "",
    #     "from PySide2.QtWidgets import *": "",
    #     "from PySide2.QtCore import *": "try:\n    from tank.platform.qt5 import *\nexcept:\n    from PySide2.QtCore import *\n    from PySide2.QtGui import *\n    from PySide2.QtWidgets import *",
    # })


def build_rcc(name):
    """
    Build a .rcc file from a .qrc file
    """
    print("Building {}...".format(name))

    qrc_path = os.path.join(current_dir, name + ".qrc").replace("\\", "/")
    print(qrc_path)
    rcc_path = os.path.join(os.path.dirname(current_dir), "python", "app", "ui", name + "_rc.py").replace("\\", "/")
    print(rcc_path)

    # compile qrc to rcc
    cmd = 'pyside2-rcc "{}" -o "{}"'.format(qrc_path, rcc_path)
    print(cmd)
    os.system(cmd)


def find_replace_in_file(filename, find_replace_dict):
    try:
        with open(filename, 'r+') as file:
            content = file.read()
            for find, replace in find_replace_dict.items():
                content = content.replace(find, replace)
            file.seek(0)
            file.write(content)
            file.truncate()
        print("Find/replace operation completed successfully.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    build_py("dialog")
    build_py("output_item")
    build_rcc("resources")
