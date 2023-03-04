import Movement
from pyPS4Controller.controller import Controller


Move = Movement

x = 50


class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self,**kwargs)

    def on_up_arrow_press(self):
        Move.forward(x)

    def on_down_arrow_press(self):
        Move.reverse(x)

    def on_right_arrow_press(self):
        Move.right_turn(x)

    def on_left_arrow_press(self):
        Move.left_turn(x)


    def on_left_right_arrow_release(self):
        Move.stop()

    def on_up_down_arrow_release(self):
        Move.stop()


controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen()