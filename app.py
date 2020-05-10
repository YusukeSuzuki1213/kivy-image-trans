from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from PIL import Image
import numpy as np
from kivy.graphics.texture import Texture
from kivy.graphics import Rectangle

FILES = [
    '10-20kV.csv',
    #'10-30kV.csv',
]    

CHAR_PERCENT = "%"
class AppBox(BoxLayout):
    def __init__(self, **kwargs):
        super(AppBox, self).__init__(**kwargs)
    
    def on_value(self, id, value):
        if(id == "slider_1"): 
            self.ids.label_1.text = str(value) + CHAR_PERCENT
        elif (id == "slider_2"):
            self.ids.label_2.text = str(value) + CHAR_PERCENT
        

class MyApp(App):
    def build(self):
        layout = AppBox()
        
        # csv読み出し
        data_list = list(map(open_csv, FILES))
        # 読み出したcsv -> pillow
        data_list_pil = list(map(Image.fromarray, data_list))
        """ texture = Texture.create(size=data_list_pil[0].size)         
        texture.blit_buffer(data_list_pil[0].tobytes())
        texture.flip_vertical()
        with widget.canvas:
            Rectangle(texture=texture ,pos=(800, 0), size=data_list_pil[0].size)   """

        return layout


def open_csv(file_name): 
    with open(file_name , 'r' , encoding='utf8') as f:
        input_data = np.genfromtxt(file_name, delimiter=',', dtype=np.float)    
    return input_data

if __name__ == '__main__':
    MyApp().run()