import bpy
from .visualizer import *
from bpy.props import BoolProperty

bl_info = {
    "name": "FS Material Visualizer",
    "author": "LKAMinco",
    "description": "Addon provide visualization for the Farming Simulator 22 UDIM system",
    "blender": (2, 80, 0),
    "location": "View3D",
    "warning": "",
    "category": "Generic"
}

classes = (
    MATVIS_PT_I3DioPanel,
    MATVIS_OT_GetData,
    MATVIS_OT_SetData,
)


def register():
    bpy.types.Material.enable_visualization = BoolProperty(
        name="Enable Visualisation",
        description="Enable visualization for the active material",
        default=False,
        update=update_material
    )
    bpy.types.Scene.real_time_visualization = BoolProperty(
        name="Real Time Visualisation",
        description="Enable real time update from visualizer to exported shader. May cause performance issues.",
        default=False
    )
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    del bpy.types.Material.enable_visualization
    del bpy.types.Scene.real_time_visualization
    for cls in classes:
        bpy.utils.unregister_class(cls)