from .ui_window import Invoke
from bpy.types import Operator

class PICKER_OT_Open_Widget_Window(Operator):
    bl_idname = "picker.open_widget_window"
    bl_label = ""
    bl_description = "Open Widget Window"

    def execute(self, context):
        Invoke()
        return {'FINISHED'}