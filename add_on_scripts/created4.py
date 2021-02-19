bl_info = {
    "name": "Create D4",
    "category": "Add",
    "author": "Andrea Springer",
    "version": (1, 0),
    "blender": (2, 83, 0),
}

import bpy

class OBJECT_OT_create_d4(bpy.types.Operator):
    """D4 Generation Script"""     
    bl_idname = "object.create_d4"        
    bl_label = "Create D4"         
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        
        
        bpy.ops.mesh.primitive_solid_add()

        bpy.context.object.dimensions.z = 20
        bpy.context.object.scale.xy = 15, 15

        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
        bpy.context.object.rotation_euler[2] = -0.523599
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[1] = 3.14159
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.view_layer.objects.active = bpy.data.objects['4']
        bpy.context.object.location.xyz = 0, 6, 5.6
        bpy.context.object.dimensions.z = 2
        bpy.context.object.scale.xy = 800, 800


        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["4"]
        bpy.ops.object.modifier_apply(modifier='Boolean', report=False)

        bpy.context.object.rotation_euler[0] = -0.339816
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[1] = 2.0944
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 0.339816
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["4"]
        bpy.ops.object.modifier_apply(modifier='Boolean', report=False)

        bpy.context.object.rotation_euler[0] = -0.339816
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[1] = 2.0944
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 0.339816
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["4"]
        bpy.ops.object.modifier_apply(modifier='Boolean', report=False)

        bpy.context.object.rotation_euler[2] = 2.0944
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.view_layer.objects.active = bpy.data.objects['3']
        bpy.context.object.location.xyz = 0, 6, 5.6
        bpy.context.object.dimensions.z = 2
        bpy.context.object.scale.xy = 800, 800

        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["3"]
        bpy.ops.object.modifier_apply(modifier='Boolean', report=False)


        bpy.context.object.rotation_euler[0] = -0.339816
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[1] = 2.0944
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 0.339816
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["3"]
        bpy.ops.object.modifier_apply(modifier='Boolean', report=False)

        bpy.context.object.rotation_euler[0] = -0.339816
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[1] = 2.0944
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 0.339816
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["3"]
        bpy.ops.object.modifier_apply(modifier='Boolean', report=False)

        bpy.context.object.rotation_euler[2] = 2.0944
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.view_layer.objects.active = bpy.data.objects['2']
        bpy.context.object.location.xyz = 0, 6, 5.6
        bpy.context.object.dimensions.z = 2
        bpy.context.object.scale.xy = 800, 800

        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["2"]
        bpy.ops.object.modifier_apply(modifier='Boolean', report=False)


        bpy.context.object.rotation_euler[0] = -0.339816
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[1] = 2.0944
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 0.339816
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["2"]
        bpy.ops.object.modifier_apply(modifier='Boolean', report=False)

        bpy.context.object.rotation_euler[0] = -0.339816
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[1] = 2.0944
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 0.339816
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["2"]
        bpy.ops.object.modifier_apply(modifier='Boolean', report=False)


        bpy.context.object.rotation_euler[2] = 2.0944
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.object.rotation_euler[2] = 2.0944
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.view_layer.objects.active = bpy.data.objects['1']

        bpy.context.object.location.xyz = 0, 6, 5.6
        bpy.context.object.dimensions.z = 2
        bpy.context.object.scale.xy = 800, 800

        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["1"]
        bpy.ops.object.modifier_apply(modifier='Boolean', report=False)


        bpy.context.object.rotation_euler[0] = -0.339816
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[1] = 2.0944
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 0.339816
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["1"]
        bpy.ops.object.modifier_apply(modifier='Boolean', report=False)

        bpy.context.object.rotation_euler[0] = -0.339816
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[1] = 2.0944
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 0.339816
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["1"]
        bpy.ops.object.modifier_apply(modifier='Boolean', report=False)
        
        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']        
        for obj in bpy.context.selected_objects:
            obj.name = "D4"
            obj.data.name = "D4"        
        

        return {'FINISHED'}

def menu_draw(self, context):
        self.layout.operator("object.create_d4")


def register():
    bpy.utils.register_class(OBJECT_OT_create_d4)
    bpy.types.VIEW3D_MT_add.prepend(menu_draw)


def unregister():
    bpy.utils.unregister_class(OBJECT_OT_create_d4)
    bpy.types.VIEW3D_MT_add.remove(menu_draw)

if __name__ == "__main__":
    register()
