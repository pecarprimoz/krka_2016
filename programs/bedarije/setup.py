from distutils.core import setup

setup(windows=[{"script": "C:/KRKA_DELO/testi.py"}],
      options={"py2exe": {"includes": ["risar"], "includes": ["turtle"], "includes": ["sip"]}})
