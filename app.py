from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from PIL import Image
import numpy as np
from kivy.graphics.texture import Texture
from kivy.graphics import Rectangle

FILES = [
    'sinogram3.csv',
    'sinogram3.csv',
    'sinogram3.csv',
    'sinogram3.csv',
    'sinogram3.csv',
    'sinogram3.csv',
    'sinogram3.csv',
    'sinogram3.csv',
    'sinogram3.csv',
    'sinogram3.csv'
    #'10-30kV.csv',
]

array_list = []
pillow_list = []

class AppBox(BoxLayout):
    def __init__(self, **kwargs):
        super(AppBox, self).__init__(**kwargs)
        
    def save_image(self):        
        sum_image = Image.fromarray(sum(array_list)).convert('RGB')
        sum_image.save('result.jpg')
                       
    def save_array(self):
        print("====")
        print(array_list[0])
        print("====")
        print(array_list[1])
        print("要素の足し算結果↓")
        print(sum(array_list))
        np.savetxt('result.csv', sum(array_list), delimiter=',')

    def on_value(self, id, prop):
        if(id == "slider_1"):
            self.ids.label_1.text = self.prop_text(prop)
            self.change_image(0, prop)
            
        elif (id == "slider_2"):
            self.ids.label_2.text = self.prop_text(prop)
            self.change_image(1, prop)
        
        elif (id == "slider_3"):
            self.ids.label_3.text = self.prop_text(prop)
            self.change_image(2, prop)

        elif (id == "slider_4"):
            self.ids.label_4.text = self.prop_text(prop)
            self.change_image(3, prop)

        elif (id == "slider_5"):
            self.ids.label_5.text = self.prop_text(prop)
            self.change_image(4, prop)

        elif (id == "slider_6"):
            self.ids.label_6.text = self.prop_text(prop)
            self.change_image(5, prop)

        elif (id == "slider_7"):
            self.ids.label_7.text = self.prop_text(prop)
            self.change_image(6, prop)

        elif (id == "slider_8"):
            self.ids.label_8.text = self.prop_text(prop)
            self.change_image(7, prop)

        elif (id == "slider_9"):
            self.ids.label_9.text = self.prop_text(prop)
            self.change_image(8, prop)

        elif (id == "slider_10"):
            self.ids.label_10.text = self.prop_text(prop)
            self.change_image(9, prop)
    
    def change_image(self, index, prop):
        array_list[index] = calc_csv(array_list[index], prop)            
        pillow_list[index] = Image.fromarray(array_list[index]).convert('RGB')
        texture = Texture.create(size=pillow_list[index].size)
        texture.blit_buffer(pillow_list[index].tobytes())
        texture.flip_vertical()

        self.ids.right_widget.canvas.add(
            Rectangle(texture=texture, size=pillow_list[index].size)
        )            

    def prop_text(self, prop):
        return "{}%".format(str(prop))

class MyApp(App):
    def build(self):
        layout = AppBox()

        return layout


def open_csv(file_name): 
    with open(file_name , 'r' , encoding='utf8') as f:
        input_data = np.genfromtxt(file_name, delimiter=',', dtype=np.float)    
    return input_data

# TODO: propが0だとエラー
def calc_csv(input_data, prop=0.0001):
    calc_input_data = input_data - np.min(input_data)
    factor = 255 / np.max(calc_input_data)
    scaled_data = calc_input_data * factor
    
    return scaled_data * prop *0.01

if __name__ == '__main__':

    array_list = list(map(calc_csv, list(map(open_csv, FILES))))
    for elem in array_list:
        pillow_list.append(Image.fromarray(elem).convert('RGB'))
    
    MyApp().run()