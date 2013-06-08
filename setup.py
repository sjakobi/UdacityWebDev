from setuptools import setup

requires = [
        "pyramid",
        ]

setup(name="udacitywebdev",
      entry_points="""\
      [paste.app_factory]
      main = udacitywebdev:main
      """,
      )
