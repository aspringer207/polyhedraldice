bl_info = {
    "name": "Create D12",
    "category": "Add",
    "author": "Andrea Springer",
    "version": (1, 0),
    "blender": (2, 83, 0),
}


import bpy
import bmesh


class OBJECT_OT_create_d12(bpy.types.Operator):
    """D12 Generation Script"""     
    bl_idname = "object.create_d12"        
    bl_label = "Create D12"         
    bl_options = {'REGISTER', 'UNDO'}  
    



    def execute(self, context):

        bpy.ops.mesh.primitive_solid_add(source = '12')

        bpy.context.object.rotation_euler.x = -1.01727
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.object.dimensions.z = 18.5
        bpy.context.object.scale.yx = 11.64

        bpy.context.view_layer.objects.active = bpy.data.objects['12']
        bpy.context.object.location.xyz = 0, 0, 9.5
        bpy.context.object.dimensions.z = 2
        bpy.context.object.scale.xy = 1000, 1000


        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']

        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["12"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier='Boolean')

        bpy.context.object.rotation_euler.z = 0.628319
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler.x = 1.10706

        bpy.context.view_layer.objects.active = bpy.data.objects['8']
        bpy.context.object.location.xyz = 0, 0, 9.5
        bpy.context.object.dimensions.z = 2
        bpy.context.object.scale.xy = 1000, 1000

        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["8"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[0] = 0
        bpy.context.object.rotation_euler[2] = 1.25664
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 1.10706

        bpy.context.view_layer.objects.active = bpy.data.objects['7']
        bpy.context.object.location.xyz = 0, 0, 9.5
        bpy.context.object.dimensions.z = 2
        bpy.context.object.scale.xy = 1000, 1000

        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["7"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[0] = 0
        bpy.context.object.rotation_euler[2] = 1.25664
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 1.10706

        bpy.context.view_layer.objects.active = bpy.data.objects['9']
        bpy.context.object.location.xyz = 0, 0, 9.5
        bpy.context.object.dimensions.z = 2
        bpy.context.object.scale.xy = 1000, 1000

        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["9"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[0] = 0
        bpy.context.object.rotation_euler[2] = 1.25664
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 1.10706

        bpy.context.view_layer.objects.active = bpy.data.objects['11']
        bpy.context.object.location.xyz = 0, 0, 9.5
        bpy.context.object.dimensions.z = 2
        bpy.context.object.scale.xy = 1000, 1000

        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["11"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[0] = 0
        bpy.context.object.rotation_euler[2] = 1.25664
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 1.10706

        bpy.context.view_layer.objects.active = bpy.data.objects['3']
        bpy.context.object.location.xyz = 0, 0, 9.5
        bpy.context.object.dimensions.z = 2
        bpy.context.object.scale.xy = 1000, 1000

        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["3"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")
        bpy.context.object.rotation_euler[0] = 0
        bpy.context.object.rotation_euler[2] = 0.628319
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 3.14159
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.view_layer.objects.active = bpy.data.objects['1']
        bpy.context.object.location.xyz = 0, 0, 9.5
        bpy.context.object.dimensions.z = 2
        bpy.context.object.scale.xy = 1000, 1000

        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["1"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[2] = 0.628319
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 1.10706

        bpy.context.view_layer.objects.active = bpy.data.objects['10']
        bpy.context.object.location.xyz = 0, 0, 9.5
        bpy.context.object.dimensions.z = 2
        bpy.context.object.scale.xy = 1000, 1000

        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["10"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")
        bpy.context.object.rotation_euler[0] = 0
        bpy.context.object.rotation_euler[2] = 1.25664
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 1.10706

        bpy.context.view_layer.objects.active = bpy.data.objects['2']
        bpy.context.object.location.xyz = 0, 0, 9.5
        bpy.context.object.dimensions.z = 2
        bpy.context.object.scale.xy = 1000, 1000

        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["2"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[0] = 0
        bpy.context.object.rotation_euler[2] = 1.25664
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 1.10706

        bpy.context.view_layer.objects.active = bpy.data.objects['4']
        bpy.context.object.location.xyz = 0, 0, 9.5
        bpy.context.object.dimensions.z = 2
        bpy.context.object.scale.xy = 1000, 1000

        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["4"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[0] = 0
        bpy.context.object.rotation_euler[2] = 1.25664
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 1.10706

        bpy.context.view_layer.objects.active = bpy.data.objects['6']
        bpy.context.object.location.xyz = 0, 0, 9.5
        bpy.context.object.dimensions.z = 2
        bpy.context.object.scale.xy = 1000, 1000

        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["6"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")
        bpy.context.object.rotation_euler[0] = 0
        bpy.context.object.rotation_euler[2] = 1.25664
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 1.10706

        bpy.context.view_layer.objects.active = bpy.data.objects['5']
        bpy.context.object.location.xyz = 0, 0, 9.5
        bpy.context.object.dimensions.z = 2
        bpy.context.object.scale.xy = 1000, 1000

        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["5"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")
       
        return {'FINISHED'}

def menu_draw(self, context):
        self.layout.operator("object.create_d12")


def register():
    bpy.utils.register_class(OBJECT_OT_create_d12)
    bpy.types.VIEW3D_MT_add.prepend(menu_draw)


def unregister():
    bpy.utils.unregister_class(OBJECT_OT_create_d12)
    bpy.types.VIEW3D_MT_add.remove(menu_draw)

if __name__ == "__main__":
    register()
