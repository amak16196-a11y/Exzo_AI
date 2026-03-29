from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout

class ExzoAI(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Dark"
        
        self.screen = MDScreen()
        self.layout = MDBoxLayout(orientation='vertical', spacing=20, padding=50, pos_hint={'center_y': .5})

        # نص الترحيب
        self.label = MDLabel(text="Choose Language / اختر اللغة", halign="center", font_style="H5")
        
        # أزرار اللغة
        btn_ar = MDRaisedButton(text="العربية", pos_hint={'center_x': .5}, on_release=self.set_arabic)
        btn_en = MDRaisedButton(text="English", pos_hint={'center_x': .5}, on_release=self.set_english)

        self.layout.add_widget(self.label)
        self.layout.add_widget(btn_ar)
        self.layout.add_widget(btn_en)
        
        self.screen.add_widget(self.layout)
        return self.screen

    def set_arabic(self, instance):
        self.label.text = "مرحباً بك في Exzo AI\nأنا جاهز لمساعدتك"
        # هنا حنربط "المخ" العربي لاحقاً

    def set_english(self, instance):
        self.label.text = "Welcome to Exzo AI\nI am ready to help you"
        # هنا حنربط "المخ" الإنجليزي لاحقاً

if __name__ == "__main__":
    ExzoAI().run()
