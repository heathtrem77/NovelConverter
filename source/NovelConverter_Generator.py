import os
import shutil

FILE_NAME = f'Novel Converter'
SOURCE_NAME = 'NovelConverter'
UI_NAME = 'NovelConverter_layout'

uiCompileCommand = f'pyuic5 -x {UI_NAME}.ui -o {UI_NAME}.py'
# rscCompileCommand = f'pyrcc5 {SOURCE_PATH}rsc.qrc -o {SOURCE_PATH}rsc_rc.py'
exeGenerateCommand = f'pyinstaller -w -F --hidden-import PyQt5 --name="{FILE_NAME}" {SOURCE_NAME}.py'

def Build():
    os.system(uiCompileCommand)
    # os.system(rscCompileCommand)

    os.system(exeGenerateCommand)
    if os.path.isfile(f'../{FILE_NAME}.exe'):
        os.remove(f'../{FILE_NAME}.exe')
    shutil.move(f'./dist/{FILE_NAME}.exe', '../')

    os.remove(f'{FILE_NAME}.spec')

Build()