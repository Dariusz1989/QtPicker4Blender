# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "QtPicker4Blender",
    "author" : "JFranMatheu, SavMartin",
    "description" : "",
    "blender" : (2, 82, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

from . import auto_load

auto_load.init()

def register():
    auto_load.register()
    from bpy.types import WindowManager as wm, Armature
    from .prop_updates import update_target_bone_name, update_target_armature, update_target_bone_index
    from bpy.props import StringProperty, PointerProperty, IntProperty
    wm.target_bone_name = StringProperty(default="", update=update_target_bone_name)
    wm.target_bone_index = IntProperty(default=0, update=update_target_bone_index)
    wm.target_armature = PointerProperty(type=Armature, name="Armature Target", update=update_target_armature)

def unregister():
    auto_load.unregister()
    from bpy.types import WindowManager as wm
    del wm.target_bone_name