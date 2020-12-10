# -*- mode: python -*-

block_cipher = None


a = Analysis(['/Users/Yoko/PycharmProjects/QEDIT/src/main/python/main.py'],
             pathex=['/Users/Yoko/PycharmProjects/QEDIT/target/PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['/Users/Yoko/PycharmProjects/QEDIT/venv/lib/python3.6/site-packages/fbs/freeze/hooks'],
             runtime_hooks=['/Users/Yoko/PycharmProjects/QEDIT/target/PyInstaller/fbs_pyinstaller_hook.py'],
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
          console=False , icon='/Users/Yoko/PycharmProjects/QEDIT/target/Icon.icns')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='QCEdit')
app = BUNDLE(coll,
             name='QCEdit.app',
             icon='/Users/Yoko/PycharmProjects/QEDIT/target/Icon.icns',
             bundle_identifier=None)
