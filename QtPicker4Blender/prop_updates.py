import bpy
from .ui_window import bone_list

def update_target_bone_name(self, context):
    arma = context.window_manager.target_armature
    bone = arma.bones.get(self.target_bone_name)
    if bone is None:
        return None
    for b in arma.bones:
        b.select = False
    bone.select = True                            # Select the target bone
    arma.bones.active = bone            # Make the target bone the active one
    return None

def update_target_bone_index(self, context):
    arma = context.window_manager.target_armature
    bone = arma.bones[self.target_bone_index]
    for b in arma.bones:
        b.select = False
    bone.select = True                            # Select the target bone
    arma.bones.active = bone            # Make the target bone the active one
    return None

def update_target_armature(self, context):
    if self.target_armature is None:
        return None
    if context.mode == 'POSE':
        bone_list.clear()
        for bone in self.target_armature.bones:
            bone_list.append(bone.name)
    return None