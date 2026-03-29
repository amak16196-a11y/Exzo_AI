from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout

class ExzoAIApp(MDApp):
    def build(self):
        # تحديد الثيم (Theme) - لون التطبيق
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Dark" # وضع ليلي

        # واجهة الشاشة
        screen = MDScreen()

        # ترتيب العناصر عمودياً في المنتصف
        layout = MDBoxLayout(
            orientation='vertical',
            spacing=30,
            padding=50,
            size_hint=(None, None),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )

        # نص العنوان
        label = MDLabel(
            text="Exzo AI - ذكاء اصطناعي أوفلاين",
            halign="center",
            theme_text_color="Primary",
            font_style="H5"
        )

        # زرار للبدء
        btn = MDRaisedButton(
            text="تحدث الآن",
            pos_hint={'center_x': 0.5},
            md_bg_color=self.theme_cls.primary_color
        )

        # إضافة العناصر للـ layout
        layout.add_widget(label)
        layout.add_widget(btn)

        # إضافة الـ layout للشاشة
        screen.add_widget(layout)

        return screen

if __name__ == "__main__":
    ExzoAIApp().run()
