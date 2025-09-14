from Inheritance_19 import Chef

class ChineseChef(Chef):
    def make_fried_rice(self):
        print("This Chef makes fried rice.")

    def make_special_dish(self):
        # return super().make_special_dish()
        print("Virtual class function overrided the base class function.")