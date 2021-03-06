from Component import Component
from Application import Application
from Box import Box
from Button import Button
from ColorPicker import ColorPicker

sys = Component('system')

app = sys.attach(Component('app'))
app.attach(Application('main'))
app.attach(Box('box1'))
app.attach(Box('box2'))
app.attach(Button('button'))
app.attach(ColorPicker('color picker'))

app.start()
app.stop()
