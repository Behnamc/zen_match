from PIL import Image
from matplotlib.pyplot import close
from img import *



class Main:
    def run():
        images = [
            1,2,3,4
        ]
        last_list = []
        save_new_list = []
        new_list = []
        ans_list = []
        for i in images:
            name_dir = str(i) + '.jpg'
            im = Image.open(name_dir)
            pix = im.load()

            save_new_list = new_list = Color.color_all(pix, im.size)
            for i in range(len(new_list)):
                if new_list[i] in last_list:
                    new_list.pop(i)
            # new_list => list of new points
            ans_list.update(new_list)
            last_list = save_new_list

            im.save('x_' + name_dir)

        return ans_list

        

    

a = Main()
a.run()