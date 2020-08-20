from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivymd.uix.menu import MDDropdownMenu
from EngCal import Amountclass

from navigation_drawer import navigation_helper

Window.size = (300, 500)


class BillApp(MDApp):
    class ContentNavigationDrawer(BoxLayout):
        pass

    class DrawerList(ThemableBehavior, MDList):
        pass

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(navigation_helper)

        self.menu = MDDropdownMenu(caller=self.screen.ids.dropdown_item, items=Amountclass.menu_items,
                                   position="bottom", callback=self.set_item, width_mult=4, border_margin=1,
                                   hor_growth='left'
                                   )

    def set_item(self, instance_menu):
        self.screen.ids.dropdown_item.text = instance_menu.text
        self.menu.dismiss()

    def build(self):
        return self.screen

    def on_start(self):
        pass

    def change_screen(self, tela):
        self.screen.ids.screen_manager.current = tela

    def btn(self):
        unit_tot = float(self.screen.ids.Unit.text)
        self.screen.ids.Amount.text = Amountclass.Calculation(self.screen.ids.dropdown_item.text, unit_tot)

BillApp().run()
