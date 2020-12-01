# -*- mode: python -*-

block_cipher = None


a = Analysis(['/Users/user/Desktop/QCEdit/QCEdit_Prod/src/main/python/main.py'],
             pathex=['/Users/user/Desktop/QCEdit/QCEdit_Prod/target/PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['/Users/user/Desktop/QCEdit/TESTS_PYSIDE2/venv/lib/python3.6/site-packages/fbs/freeze/hooks'],
             runtime_hooks=['/Users/user/Desktop/QCEdit/QCEdit_Prod/target/PyInstaller/fbs_pyinstaller_hook.py'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='QCEdit',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=False , icon='/Users/user/Desktop/QCEdit/QCEdit_Prod/target/Icon.icns')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='QCEdit')
app = BUNDLE(coll,
             name='QCEdit.app',
             icon='/Users/user/Desktop/QCEdit/QCEdit_Prod/target/Icon.icns',
             bundle_identifier=None)
