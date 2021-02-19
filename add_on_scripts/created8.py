bl_info = {
    "name": "Create D8",
    "category": "Add",
    "author": "Andrea Springer",
    "version": (1, 0),
    "blender": (2, 83, 0),
}

import bpy

class OBJECT_OT_create_d8(bpy.types.Operator):
    """D6 Generation Script"""     
    bl_idname = "object.create_d8"        
    bl_label = "Create D8"         
    bl_options = {'REGISTER', 'UNDO'}  

    def execute(self, context):
        
        bpy.ops.mesh.primitive_solid_add(source='8')

        bpy.context.object.rotation_euler[1] = 0.785398
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 0.61549
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.dimensions.z = 16.4
        bpy.context.object.scale.xy = 14.2026, 14.2026

        bpy.context.view_layer.objects.active = bpy.data.objects['8']

        bpy.context.object.location.xyz = 0, 0, 8.6
        bpy.context.object.dimensions.z = 2.0
        bpy.context.object.scale.xy = 1000, 1000

        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["8"]
        bpy.ops.object.modifier_apply(modifier='Boolean', report=False)

        bpy.context.object.rotation_euler[0] = -0.6154904
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[1] = -1.5707963
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 0.61549
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
            
        bpy.context.view_layer.objects.active = bpy.data.objects['6']
        bpy.context.object.location.xyz = 0, 0, 8.6
        bpy.context.object.dimensions.z = 2.0
        bpy.context.object.scale.xy = 1000, 1000

        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["6"]
        bpy.ops.object.modifier_apply(modifier='Boolean', report=False)

        bpy.context.object.rotation_euler[0] = -0.6154904
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[1] = -1.5707963
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 0.61549
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
            
        bpy.context.view_layer.objects.active = bpy.data.objects['4']
        bpy.context.object.location.xyz = 0, 0, 8.6
        bpy.context.object.dimensions.z = 2.0
        bpy.context.object.scale.xy = 1000, 1000

        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["4"]
        bpy.ops.object.modifier_apply(modifier='Boolean', report=False)

        bpy.context.object.rotation_euler[0] = -0.6154904
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[1] = -1.5707963
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 0.61549
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
            
        bpy.context.view_layer.objects.active = bpy.data.objects['2']
        bpy.context.object.location.xyz = 0, 0, 8.6
        bpy.context.object.dimensions.z = 2.0
        bpy.context.object.scale.xy = 1000, 1000

        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["2"]
        bpy.ops.object.modifier_apply(modifier='Boolean', report=False)

        bpy.context.object.rotation_euler[0] = 3.1415927
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.view_layer.objects.active = bpy.data.objects['7']
        bpy.context.object.location.xyz = 0, 0, 8.6
        bpy.context.object.dimensions.z = 2.0
        bpy.context.object.scale.xy = 1000, 1000

        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["7"]
        bpy.ops.object.modifier_apply(modifier='Boolean', report=False)

        bpy.context.object.rotation_euler[0] = -0.6154904
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[1] = -1.5707963
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 0.61549
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
            
        bpy.context.view_layer.objects.active = bpy.data.objects['5']
        bpy.context.object.location.xyz = 0, 0, 8.6
        bpy.context.object.dimensions.z = 2.0
        bpy.context.object.scale.xy = 1000, 1000

        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["5"]
        bpy.ops.object.modifier_apply(modifier='Boolean', report=False)

        bpy.context.object.rotation_euler[0] = -0.6154904
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[1] = -1.5707963
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 0.61549
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
            
        bpy.context.view_layer.objects.active = bpy.data.objects['3']
        bpy.context.object.location.xyz = 0, 0, 8.6
        bpy.context.object.dimensions.z = 2.0
        bpy.context.object.scale.xy = 1000, 1000

        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["3"]
        bpy.ops.object.modifier_apply(modifier='Boolean', report=False)

        bpy.context.object.rotation_euler[0] = -0.6154904
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[1] = -1.5707963
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 0.61549
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
            
        bpy.context.view_layer.objects.active = bpy.data.objects['1']
        bpy.context.object.location.xyz = 0, 0, 8.6
        bpy.context.object.dimensions.z = 2.0
        bpy.context.object.scale.xy = 1000, 1000

        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["1"]
        bpy.ops.object.modifier_apply(modifier='Boolean', report=False)
        
        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']        
        for obj in bpy.context.selected_objects:
            obj.name = "D8"
            obj.data.name = "D8"        
       
        
        return {'FINISHED'}

def menu_draw(self, context):
        self.layout.operator("object.create_d8")


def register():
    bpy.utils.register_class(OBJECT_OT_create_d8)
    bpy.types.VIEW3D_MT_add.prepend(menu_draw)


def unregister():
    bpy.utils.unregister_class(OBJECT_OT_create_d8)
    bpy.types.VIEW3D_MT_add.remove(menu_draw)

if __name__ == "__main__":
    register()
