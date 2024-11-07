from cx_Freeze import setup,Executable

icon_path = "icon.ico"

executable = Executable(script="guessing_game_gui.py",icon=icon_path)

options = {"build_exe":{"include_files": [icon_path]}}

setup(
    name = "Guessing Game",
    version = "1.0",
    description = "Guessing Game",
    options = options,
    executables = [executable]
)