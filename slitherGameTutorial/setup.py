import os
os.environ['TCL_LIBRARY'] = "C:\\Program Files (x86)\\Python35-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Program Files (x86)\\Python35-32\\tcl\\tk8.6"




import cx_Freeze

executables=[cx_Freeze.Executable("pyGameTutorial.py")]
cx_Freeze.setup(
    name="Slither",
    options={"build_exe":{"packages":["pygame"],"include_files":["apple.png","snake2.png"]}},
    description="Slither Game Tutorial",
    executables=executables
    )
