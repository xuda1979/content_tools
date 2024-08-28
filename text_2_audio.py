# import kivy
# from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.textinput import TextInput
# from kivy.uix.button import Button
# from kivy.uix.progressbar import ProgressBar
# from kivy.uix.popup import Popup
# from kivy.uix.filechooser import FileChooserIconView
# from kivy.clock import Clock
# import pyttsx3
# import os
# import pygame
# import threading

# # Initialize the text-to-speech engine
# engine = pyttsx3.init()
# engine.setProperty('rate', 150)  # Set speaking speed

# class SimpleTTSApp(App):
#     def build(self):
#         # Main layout
#         layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

#         # Text input box
#         self.text_input = TextInput(hint_text="Enter your text here", multiline=True)
#         layout.add_widget(self.text_input)

#         # Progress Bar
#         self.progress_bar = ProgressBar(max=100, size_hint_y=None, height=30)
#         layout.add_widget(self.progress_bar)

#         # Generate Button
#         generate_button = Button(text="Generate Audio", size_hint_y=None, height=40)
#         generate_button.bind(on_press=self.generate_audio)
#         layout.add_widget(generate_button)

#         # Listen Button
#         self.listen_button = Button(text="Listen", size_hint_y=None, height=40, disabled=True)
#         self.listen_button.bind(on_press=self.listen_audio)
#         layout.add_widget(self.listen_button)

#         # Save Button
#         self.save_button = Button(text="Save to File", size_hint_y=None, height=40, disabled=True)
#         self.save_button.bind(on_press=self.show_save_dialog)
#         layout.add_widget(self.save_button)

#         return layout

#     def update_progress(self, progress):
#         self.progress_bar.value = progress

#     def generate_audio(self, instance):
#         threading.Thread(target=self._generate_audio).start()

#     def _generate_audio(self):
#         text = self.text_input.text
#         self.temp_filename = "temp_audio.mp3"

#         engine.save_to_file(text, self.temp_filename)
#         engine.runAndWait()

#         # Update progress bar to 100%
#         for i in range(1, 101):
#             Clock.schedule_once(lambda dt, p=i: self.update_progress(p), 0.02 * i)

#         # Enable the listen and save buttons
#         Clock.schedule_once(lambda dt: self.enable_buttons())

#     def enable_buttons(self):
#         self.listen_button.disabled = False
#         self.save_button.disabled = False

#     def listen_audio(self, instance):
#         pygame.mixer.init()
#         pygame.mixer.music.load(self.temp_filename)
#         pygame.mixer.music.play()

#     def show_save_dialog(self, instance):
#         content = SaveDialog(save=self.save_file, cancel=self.dismiss_popup)
#         self._popup = Popup(title="Save file", content=content, size_hint=(0.9, 0.9))
#         self._popup.open()

#     def dismiss_popup(self, instance):
#         self._popup.dismiss()

#     def save_file(self, path, filename):
#         if not filename.endswith('.mp3'):
#             filename += '.mp3'
#         full_path = os.path.join(path, filename)
#         os.rename(self.temp_filename, full_path)
#         print(f"Audio saved to {full_path}")
#         self.dismiss_popup(None)

# class SaveDialog(BoxLayout):
#     def __init__(self, save, cancel, **kwargs):
#         super(SaveDialog, self).__init__(**kwargs)
#         self.orientation = 'vertical'
#         self.filechooser = FileChooserIconView()
#         self.add_widget(self.filechooser)
#         self.filename_input = TextInput(hint_text="Enter file name", size_hint_y=None, height=30)
#         self.add_widget(self.filename_input)
#         buttons_layout = BoxLayout(size_hint_y=None, height=30)
#         save_button = Button(text="Save", on_press=lambda x: save(self.filechooser.path, self.filename_input.text))
#         cancel_button = Button(text="Cancel", on_press=cancel)
#         buttons_layout.add_widget(save_button)
#         buttons_layout.add_widget(cancel_button)
#         self.add_widget(buttons_layout)

# if __name__ == '__main__':
#     SimpleTTSApp().run()

from gtts import gTTS
import os

# The Russian text to be converted to speech
text =  """Заголовок: Важность физической активности для здоровья

Физическая активность играет важную роль в поддержании здоровья и благополучия. Регулярные упражнения способствуют укреплению сердечно-сосудистой системы, улучшению настроения и снижению риска развития различных хронических заболеваний. Врачи рекомендуют заниматься физическими упражнениями не менее 150 минут в неделю, включая аэробные нагрузки и упражнения на силу.

Кроме того, физическая активность помогает поддерживать здоровый вес и повышает общую выносливость организма. Люди, ведущие активный образ жизни, реже сталкиваются с проблемами, связанными с ожирением, диабетом и гипертонией.

Начать заниматься спортом можно с простых прогулок на свежем воздухе, постепенно увеличивая интенсивность и продолжительность тренировок. Важно помнить, что регулярность является ключом к успеху в поддержании здоровья и долгосрочного благополучия.


"""

# Create a gTTS object
tts = gTTS(text=text, lang='ru', slow=False)

# Save the speech to a file
output_file = "output_audio_russian.mp3"
tts.save(output_file)

print(f"Audio file '{output_file}' has been created successfully.")

# Optionally, play the file using the default media player
os.system(f"start {output_file}")  # On Windows
# os.system(f"open {output_file}")  # On macOS
# os.system(f"xdg-open {output_file}")  # On Linux

