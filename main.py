import json
import os
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.utils import platform

# مكتبات الصوت (ستعمل إذا تم تثبيت الموديلات)
try:
    import pyttsx3
    import speech_recognition as sr
except ImportError:
    print("Libraries not found, running in text-only mode")

class ExzoAI(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        
        # تحميل الذاكرة
        try:
            with open('brain.json', 'r', encoding='utf-8') as f:
                self.brain = json.load(f)
        except:
            self.brain = {"arabic": {"مرحبا": "أهلاً بك في إكزو"}, "english": {}}

        layout = MDBoxLayout(orientation='vertical', padding=40, spacing=20)
        
        self.status_label = MDLabel(
            text="Exzo AI\nاضغط وتحدث معي", 
            halign="center", 
            font_style="H5",
            theme_text_color="Primary"
        )
        
        mic_btn = MDFillRoundFlatButton(
            text="🎤 Start Listening / ابدأ التحدث", 
            pos_hint={'center_x': 0.5},
            on_release=self.start_listening
        )

        layout.add_widget(self.status_label)
        layout.add_widget(mic_btn)
        
        screen = MDScreen()
        screen.add_widget(layout)
        return screen

    def start_listening(self, *args):
        self.status_label.text = "Listening... / جاري الاستماع"
        # ملاحظة: في أندرويد نحتاج لربط الـ Permissions أولاً
        # حالياً سنضع الرد كـ Simulation لضمان عدم الكراش
        self.process_logic("مرحبا")

    def process_logic(self, query):
        response = self.brain['arabic'].get(query, "سأبحث عن حل لهذا الأمر معقداً..")
        self.status_label.text = f"Exzo: {response}"

if __name__ == "__main__":
    ExzoAI().run()
if __name__ == "__main__":
    ExzoAI().run()
