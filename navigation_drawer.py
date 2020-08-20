navigation_helper = """

NavigationLayout:
    
    ScreenManager:
        id : screen_manager
        Screen:
            id: NavScreen
            name: "NavScreen"
            BoxLayout:
                orientation: 'vertical'
                MDToolbar:
                    title: 'Electricity Tariff'
                    left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                    elevation:5
                Widget:
                
            MDCard:
                size_hint: None, None
                size: "130dp", "50dp"
                radius:[20,]
                border_radius:20
                md_bg_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .6, "center_y": .25}
            
            MDLabel:
                font_size : 17
                pos_hint: {'center_x': 0.55, 'center_y': 0.8}
                text: "Domestic Consumer (Single Phase)"
                color : 0, 0, 1, 1
                #font_style : "H6"

            MDLabel:
                font_size : 15
                pos_hint: {'center_x': 0.6, 'center_y': 0.7}
                text: "Approved load :"
                color : 0, 0, 0, 1
        
            MDLabel:
                font_size : 18
                pos_hint: {'center_x': 0.58, 'center_y': 0.25}
                text: "Total NRs : "
                color : 0, 0, 0, 1
        
            MDLabel:
                id : Amount
                font_size : 18
                pos_hint: {'center_x': 0.95, 'center_y': 0.25}
                text: "00.00"
                color : 0, 0, 0, 1
        
            MDDropDownItem:
                id: dropdown_item
                text: "5 Ampere"
                font_size : 15
                #user_font_size: "16sp"
                pos_hint: {'center_x': 0.7, 'center_y': 0.7}
                #dropdown_bg: [1, 1, 1, 1]
                on_release: app.menu.open()
        
            MDTextField:
                id : Unit
                hint_text: "Consume Unit"
                helper_text: "Unit/kWh"
                helper_text_mode: "on_focus"
                icon_right: "home-lightbulb"
                icon_right_color: app.theme_cls.primary_color
                pos_hint:{'center_x': 0.5, 'center_y': 0.5}
                size_hint_x:None
                width:150
        
            MDRectangleFlatButton:
                pos_hint: {'center_x': 0.5, 'center_y': 0.4}
                text: "Calculate"
                on_release: app.btn()
            
            

        Screen :
            id: tariffscreen
            name: "tariffscreen"
            FloatLayout:
                Image:
                    size: root.width, root.height*.8
                    source: 'BidhutMahasul2077.png'
                    id: imageWid     
            BoxLayout:
                orientation: 'vertical'
                MDToolbar:
                    title: 'Tariff Rates'
                    left_action_items: [["keyboard-backspace", lambda x: app.change_screen("NavScreen")]]
                    elevation:5
                Widget:
                       
    
        Screen :
            id: Contactscreen
            name: "Contactscreen"
            BoxLayout:
                orientation: 'vertical'
                MDToolbar:
                    title: 'Contact (NEA)'
                    left_action_items: [["keyboard-backspace", lambda x: app.change_screen("NavScreen")]]
                    elevation:5
                Widget:
            ScrollView:
                pos_hint: {"center_x": .45, "center_y": .2}
                MDList:
                    padding: 0
                    
                    TwoLineAvatarIconListItem:
                        text: "Central Office"
                        secondary_text: "Durbarmarg, Kathmandu"
                        secondary_font_style: "Caption"
                        IconLeftWidget:
                            icon: "map-marker"
                    OneLineIconListItem:
                        text: "info@nea.org.np"
                        IconLeftWidget:
                            icon: "email"
                    OneLineIconListItem:
                        text: "www.nea.org.np"
                        IconLeftWidget:
                            icon: "web"  
                    OneLineIconListItem:
                        text: "977-1-415305"
                        IconLeftWidget:
                            icon: "phone" 
                    OneLineIconListItem:
                        text: "+977-1-4153009"
                        IconLeftWidget:
                            icon: "fax"  
    

    MDNavigationDrawer:
        id: nav_drawer
        ContentNavigationDrawer:
            orientation: 'vertical'
            padding: "8dp"
            spacing: "8dp"
            Image:
                id: avatar
                size_hint: (1,1)
                source: "NEA-logo.jpg"
            MDLabel:
                text: "Nepal Electricity Authority"
                font_style: "Subtitle1"
                size_hint_y: None
                height: self.texture_size[1]
            MDLabel:
                text: "DarbarMarge, Kathmandu"
                size_hint_y: None
                font_style: "Caption"
                height: self.texture_size[1]
            ScrollView:
                DrawerList:
                    id: md_list
                    MDList:
                        OneLineIconListItem:
                            on_release: 
                                nav_drawer.set_state("close")
                                screen_manager.current = "tariffscreen"
                            text: "Tariff Rates"
                            IconLeftWidget:
                                icon: "cash"
                        OneLineIconListItem:
                            on_release: 
                                nav_drawer.set_state("close")
                                screen_manager.current = "Contactscreen"
                            text: "Contact NEA"
                            IconLeftWidget:
                                icon: "information-variant"
                        OneLineIconListItem:
                            on_release: 
                                nav_drawer.set_state("close")
                                exit(0)
                            text: "Exit"
                            IconLeftWidget:
                                icon: "exit-to-app"


"""
