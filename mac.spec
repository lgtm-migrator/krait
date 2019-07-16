# -*- mode: python -*-

block_cipher = None


a = Analysis(['src/main.py'],
             pathex=[],
             binaries=[],
             datas=[('src/primer3_config', 'primer3_config'), ('src/template', 'template'), ('example', 'example')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['PyQt4', 'PyQt5', 'Tkinter', 'wx', 'pydoc', 'pkg_resources'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='Krait',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='src/icons/logo.icns')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='Krait')
app = BUNDLE(coll,
             name='Krait.app',
             icon='src/icons/logo.icns',
             bundle_identifier=None)
