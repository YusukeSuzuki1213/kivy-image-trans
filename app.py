'''
[WARN]
    This code is fuckin shit.

'''

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from PIL import Image
import numpy as np
from kivy.graphics.texture import Texture
from kivy.graphics import Rectangle

# 読み込むファイルのリスト
FILES = [
    'result.csv',
    'result.csv',
    'result.csv',
    'result.csv',
    'result.csv',
    'result.csv',
    'result.csv',
    'result.csv',
    'result.csv',
    'result.csv',
    
    
    #'10-20kV.csv'    
]

# csvファイルをndarrayに変換しリスト化したもの
array_list = []
# csvファイルをpillowのオブジェクトとしてリスト化したもの(多分不要)
pillow_list = []

class AppBox(BoxLayout):
    def __init__(self, **kwargs):
        super(AppBox, self).__init__(**kwargs)

    # 10個のファイルの画素値を合計して画像にして保存        
<<<<<<< HEAD
    def save_image(self):
=======
    def save_image(self):        
>>>>>>> 58008a311b9a1537c8b0235a5b63eca23a634d52
        sum_image = Image.fromarray(sum(array_list)).convert('RGB')
        sum_image.save('result.jpg')
    
    # 10個のファイルの画素値を合計して保存
    def save_array(self):
        print("====")
        print(array_list[0])
        print("====")
        print(array_list[1])
        print("要素の足し算結果↓")
        print(sum(array_list))
        np.savetxt('result.csv', sum(array_list), delimiter=',')
<<<<<<< HEAD
        print("要素の終了")
=======

>>>>>>> 58008a311b9a1537c8b0235a5b63eca23a634d52
    # スライドバーが更新されたら
    def on_value(self, id, prop):
        # .kvファイル上のidが'slider_1'だったら
        if(id == "slider_1"):
            # 表示パーセンテージ変更
            self.ids.label_1.text = self.prop_text(prop)
            # 画像の更新＆画素値更新
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
    
    # 画像値の更新＆GUI上の画像更新
    def change_image(self, index, prop):
        # 画素値更新
        array_list[index] = calc_csv(array_list[index], prop)            
        pillow_list[index] = Image.fromarray(array_list[index]).convert('RGB')

        # GUI上の画像更新        
        sum_image = Image.fromarray(sum(array_list)).convert('RGB').resize((512, 286))
        texture = Texture.create(size=sum_image.size)
        texture.blit_buffer(sum_image.tobytes())
        texture.flip_vertical()
        
        self.ids.right_widget.canvas.add(
            Rectangle(texture=texture, size=sum_image.size)
        )            
    
    # GUI上のパーセント表示 (e.g 56%)
    def prop_text(self, prop):
        return "{}%".format(str(prop))

# csvをひらく
def open_csv(file_name): 
    with open(file_name , 'r' , encoding='utf8') as f:        
        input_data = np.genfromtxt(file_name, delimiter=',', dtype=np.float)    
    return input_data

# TODO: propが0だとエラー
def calc_csv(input_data, prop=0.0001):
    calc1 = input_data - 0
    print(np.max(input_data))
    calc2 = np.max(input_data) - 0
    print(calc2)
    calc3 = 4095
    calc4 = calc1 / calc2
    print(calc4)
    scaled_data = calc4 * calc3
    return scaled_data * prop * 0.01

class MyApp(App):
    def build(self):
        layout = AppBox()
<<<<<<< HEAD

        return layout

=======

        return layout

>>>>>>> 58008a311b9a1537c8b0235a5b63eca23a634d52
if __name__ == '__main__':
    # FILESのcsvを全て開いてndarrayに変換
    array_list = list(map(calc_csv, list(map(open_csv, FILES))))
    # array_listをpillowに変換
    for elem in array_list:
        pillow_list.append(Image.fromarray(elem).convert('RGB'))
    # kivvy app start
    MyApp().run()