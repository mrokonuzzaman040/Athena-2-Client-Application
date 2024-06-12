from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.progressbar import ProgressBar
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup

# Set the window size
Window.size = (1280, 720)

class DragAndDropBox(FloatLayout):
    def __init__(self, **kwargs):
        super(DragAndDropBox, self).__init__(**kwargs)
        self.progress_bar = ProgressBar(max=100, size_hint=(0.6, None), height=30, pos_hint={"center_x": 0.5, "center_y": 0.4})
        self.add_widget(self.progress_bar)
        self.progress_label = Label(text="0% Completed", font_size=20, color=(1, 1, 0, 1), size_hint=(None, None), height=50, pos_hint={"center_x": 0.5, "center_y": 0.35})
        self.add_widget(self.progress_label)
    
    def update_progress(self, value):
        self.progress_bar.value = value
        self.progress_label.text = f"{int(value)}% Completed"

class FileSelectorPopup(Popup):
    def __init__(self, upload_callback, **kwargs):
        super(FileSelectorPopup, self).__init__(**kwargs)
        self.upload_callback = upload_callback
        self.title = 'Select a file'
        self.size_hint = (0.9, 0.9)
        self.content = FileChooserIconView(on_selection=lambda x: self.on_file_select(x.selection))
    
    def on_file_select(self, selection):
        if selection:
            self.upload_callback(selection[0])
            self.dismiss()

class DashboardScreen(Screen):
    pass

class DataUploadScreen(Screen):
    def __init__(self, **kwargs):
        super(DataUploadScreen, self).__init__(**kwargs)
        self.drag_and_drop_box = DragAndDropBox(size_hint=(0.8, 0.5), pos_hint={"center_x": 0.5, "center_y": 0.5})
        self.add_widget(self.drag_and_drop_box)
        self.filechooser = FileChooserIconView(size_hint=(1, 0.6), pos_hint={"top": 0.8}, filters=["*.txt", "*.csv"])
        self.filechooser.bind(on_selection=lambda *x: self.on_file_drop(self.filechooser.selection))
        self.add_widget(self.filechooser)

    def on_file_drop(self, files):
        if files:
            self.upload_file(files[0])
    
    def open_file_selector(self):
        popup = FileSelectorPopup(self.upload_file)
        popup.open()
    
    def upload_file(self, filepath):
        # Simulate file upload process
        import threading
        import time
        def upload():
            for i in range(101):
                time.sleep(0.05)  # Simulate time taken for upload
                self.drag_and_drop_box.update_progress(i)
        threading.Thread(target=upload).start()

class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(DashboardScreen(name='dashboard'))
        sm.add_widget(DataUploadScreen(name='data_upload'))
        return sm

if __name__ == '__main__':
    MainApp().run()
