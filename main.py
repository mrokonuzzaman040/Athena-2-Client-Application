from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.progressbar import ProgressBar
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooser
import os
import shutil

# Set the window size
Window.size = (1280, 720)

class FileSelectorPopup(Popup):
    def __init__(self, select_callback, **kwargs):
        super(FileSelectorPopup, self).__init__(**kwargs)
        self.select_callback = select_callback
        self.title = 'Select a file'
        self.size_hint = (0.9, 0.9)
        filechooser = FileChooser(on_selection=lambda x: self.on_file_select(x.selection))
        self.content = filechooser
    
    def on_file_select(self, selection):
        if selection:
            self.select_callback(selection[0])
            self.dismiss()

class DashboardScreen(Screen):
    pass

class DataUploadScreen(Screen):
    def __init__(self, **kwargs):
        super(DataUploadScreen, self).__init__(**kwargs)
        self.selected_file = None
        
        # Upload section
        self.upload_section = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.add_widget(self.upload_section)

        # Browse button
        self.browse_button = Button(text="Browse File", size_hint=(0.5, None), height=50, pos_hint={"center_x": 0.5, "center_y": 0.7})
        self.browse_button.bind(on_press=self.open_file_selector)
        self.upload_section.add_widget(self.browse_button)

        # Upload button
        self.upload_button = Button(text="Upload", size_hint=(0.5, None), height=50, pos_hint={"center_x": 0.5, "center_y": 0.6})
        self.upload_button.bind(on_press=self.upload_file)
        self.upload_button.disabled = True  # Initially disabled until a file is selected
        self.upload_section.add_widget(self.upload_button)

        # Progress bar and label
        self.progress_bar = ProgressBar(max=100, size_hint=(0.8, None), height=30, pos_hint={"center_x": 0.5, "center_y": 0.4})
        self.upload_section.add_widget(self.progress_bar)
        self.progress_label = Label(text="0% Completed", font_size=20, color=(1, 1, 0, 1), size_hint=(None, None), height=50, pos_hint={"center_x": 0.5, "center_y": 0.35})
        self.upload_section.add_widget(self.progress_label)

    def open_file_selector(self, instance):
        popup = FileSelectorPopup(self.on_file_selected)
        popup.open()

    def on_file_selected(self, filepath):
        self.selected_file = filepath
        self.upload_button.disabled = False
    
    def upload_file(self, instance):
        if self.selected_file:
            self.upload_button.disabled = True
            # Ensure the upload directory exists
            if not os.path.exists('upload'):
                os.makedirs('upload')
            
            # Simulate file upload process
            import threading
            import time
            def upload():
                for i in range(101):
                    time.sleep(0.05)  # Simulate time taken for upload
                    self.progress_bar.value = i
                    self.progress_label.text = f"{i}% Completed"
                # Simulate moving the file to the upload directory
                shutil.copy(self.selected_file, os.path.join('upload', os.path.basename(self.selected_file)))
            threading.Thread(target=upload).start()

class DataProcessingScreen(Screen):
    pass

class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(DashboardScreen(name='dashboard'))
        sm.add_widget(DataUploadScreen(name='data_upload'))
        sm.add_widget(DataProcessingScreen(name='data_processing'))
        return sm

if __name__ == '__main__':
    MainApp().run()
