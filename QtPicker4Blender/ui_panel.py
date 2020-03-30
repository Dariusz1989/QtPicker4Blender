import bpy
from bpy.types import Panel

class PICKER_PT_Picker_Widget(Panel):
    bl_label = "Picker"
    bl_category = 'RIG'
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        col = self.layout.column()
        if context.mode == 'POSE':
            wm = context.window_manager
            col.prop(wm, "target_armature", text="Armature")
            col.operator('picker.open_widget_window', text="Open Picker Widget")
        else:
            col.alert = True
            col.label(text="You should be in Pose Mode", icon='INFO')