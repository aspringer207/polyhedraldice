bl_info = {
    "name": "Create D6",
    "category": "Add",
    "author": "Andrea Springer",
    "version": (1, 0),
    "blender": (2, 83, 0),
}

import bpy


class OBJECT_OT_create_d6(bpy.types.Operator):
    """D6 Generation Script"""     
    bl_idname = "object.create_d6"        
    bl_label = "Create D6"         
    bl_options = {'REGISTER', 'UNDO'}  

    def execute(self, context):        

        bpy.ops.mesh.primitive_cube_add(size=16, enter_editmode=False, align='WORLD', location=(0, 0, 0))

        bpy.context.view_layer.objects.active = bpy.data.objects['6']

        bpy.context.object.location.xy = 0.0, 0.0
        bpy.context.object.location.z = 8.6

        bpy.context.object.dimensions.z = 2.0
        bpy.context.object.scale.xy = 1250, 1250

        bpy.context.view_layer.objects.active = bpy.data.objects['Cube']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects['6']
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[2] = 1.5708
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[1] = -1.5708
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.view_layer.objects.active = bpy.data.objects['2']

        bpy.context.object.location.xy = 0.0, 0.0
        bpy.context.object.location.z = 8.6

        bpy.context.object.dimensions.z = 2.0
        bpy.context.object.scale.xy = 1250, 1250

        bpy.context.view_layer.objects.active = bpy.data.objects['Cube']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects['2']
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[2] = 1.5708
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[1] = -1.5708
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.view_layer.objects.active = bpy.data.objects['4']

        bpy.context.object.location.xy = 0.0, 0.0
        bpy.context.object.location.z = 8.6

        bpy.context.object.dimensions.z = 2.0
        bpy.context.object.scale.xy = 1250, 1250

        bpy.context.view_layer.objects.active = bpy.data.objects['Cube']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects['4']
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[0] = 3.14159
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.view_layer.objects.active = bpy.data.objects['3']

        bpy.context.object.location.xy = 0.0, 0.0
        bpy.context.object.location.z = 8.6

        bpy.context.object.dimensions.z = 2.0
        bpy.context.object.scale.xy = 1250, 1250

        bpy.context.view_layer.objects.active = bpy.data.objects['Cube']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects['3']
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[2] = -1.5708
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[1] = 1.5708
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.view_layer.objects.active = bpy.data.objects['1']

        bpy.context.object.location.xy = 0.0, 0.0
        bpy.context.object.location.z = 8.6

        bpy.context.object.dimensions.z = 2.0
        bpy.context.object.scale.xy = 1250, 1250

        bpy.context.view_layer.objects.active = bpy.data.objects['Cube']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects['1']
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[2] = -1.5708
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[1] = 1.5708
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.view_layer.objects.active = bpy.data.objects['5']

        bpy.context.object.location.xy = 0.0, 0.0
        bpy.context.object.location.z = 8.6

        bpy.context.object.dimensions.z = 2.0
        bpy.context.object.scale.xy = 1250, 1250

        bpy.context.view_layer.objects.active = bpy.data.objects['Cube']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects['5']
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")      

        bpy.context.view_layer.objects.active = bpy.data.objects['Cube']        
        for obj in bpy.context.selected_objects:
            obj.name = "D6"
            obj.data.name = "D6"        
        
        return {'FINISHED'}

def menu_draw(self, context):
        self.layout.operator("object.create_d6")


def register():
    bpy.utils.register_class(OBJECT_OT_create_d6)
    bpy.types.VIEW3D_MT_add.prepend(menu_draw)


def unregister():
    bpy.utils.unregister_class(OBJECT_OT_create_d6)
    bpy.types.VIEW3D_MT_add.remove(menu_draw)

if __name__ == "__main__":
    register()
