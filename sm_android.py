import toga
from colosseum import CSS
#from toga_android import Android
import os

def launch_streamlit():
    os.system("streamlit run stock_manager.py")

def build(app):
    container = toga.Container(style=CSS(flex=1, padding=10))
    button = toga.Button('Launch Streamlit', on_press=launch_streamlit)
    container.add(button)
    return container

def main():
    app = toga.App('Streamlit Launcher', 'org.example.streamlitlauncher', startup=build)
    app.main_loop()
