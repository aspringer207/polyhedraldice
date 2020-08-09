bl_info = {
    "name": "Create D20",
    "category": "Add",
    "author": "Andrea Springer",
    "version": (1, 0),
    "blender": (2, 83, 0),    
    "description": "Creates a D20 model from user prepared numerals or symbols.",
    "tracker_url": "https://github.com/aspringer207/polyhedraldice",
    "support": "TESTING",
}


import bpy


class OBJECT_OT_create_d20(bpy.types.Operator):
    """D20 Generation Script"""     
    bl_idname = "object.create_d20"        
    bl_label = "Create D20"         
    bl_options = {'REGISTER', 'UNDO'}  

    def execute(self, context):        
        bpy.ops.mesh.primitive_solid_add(source='20')
        bpy.context.object.rotation_euler[0] = 0.364861

        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.dimensions[2] = 20.7
        bpy.context.object.scale[1] = 13.024
        bpy.context.object.scale[0] = 13.024
        bpy.context.view_layer.objects.active = bpy.data.objects['20']
        bpy.context.object.location.xyz = 0, 0, 11
        bpy.context.object.dimensions.z = 2
        bpy.context.object.scale.xy = 520, 520
        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["20"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[2] = 1.04719
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 0.729722
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)


        bpy.context.view_layer.objects.active = bpy.data.objects['14']
        bpy.context.object.location.xyz = 0, 0, 11
        bpy.context.object.dimensions.z = 2
        bpy.context.object.scale.xy = 520, 520
        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["14"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[2] = 1.04719
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 0.729722

        bpy.context.view_layer.objects.active = bpy.data.objects['6']
        bpy.context.object.location.xyz = 0, 0, 11
        bpy.context.object.dimensions.z = 2
        bpy.context.object.scale.xy = 520, 520
        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["6"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[0] = 0
        bpy.context.object.rotation_euler[2] = -2.0944
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 0.729722

        bpy.context.view_layer.objects.active = bpy.data.objects['4']
        bpy.context.object.location.xyz = 0, 0, 11
        bpy.context.object.dimensions.z = 2
        bpy.context.object.scale.xy = 520, 520
        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["4"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[0] = 0
        
        bpy.context.object.rotation_euler[2] = 1.0471976
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = -0.7297222

        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.object.rotation_euler[2] = 2.0943951
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 0.729722
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)


        bpy.context.view_layer.objects.active = bpy.data.objects['8']
        bpy.context.object.location.xyz = 0, 0, 11
        bpy.context.object.dimensions.z = 2
        bpy.context.object.scale.xy = 520, 520
        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["8"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[2] = 1.04719
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 0.729722

        bpy.context.view_layer.objects.active = bpy.data.objects['10']
        bpy.context.object.location.xyz = 0, 0, 11
        bpy.context.object.dimensions.z = 2
        bpy.context.object.scale.xy = 520, 520
        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["10"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[0] = 0

        bpy.context.object.rotation_euler[2] = -2.0943951
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 0.729722

        bpy.context.view_layer.objects.active = bpy.data.objects['16']
        bpy.context.object.location.xyz = 0, 0, 11
        bpy.context.object.dimensions.z = 2
        bpy.context.object.scale.xy = 520, 520
        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["16"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[0] = 0
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.object.rotation_euler[2] = 1.0471976
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = -0.7297222

        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.object.rotation_euler[2] = 2.0944

        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.object.rotation_euler[0] = 0.729722
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.view_layer.objects.active = bpy.data.objects['2']
        bpy.context.object.location.xyz = 0, 0, 11
        bpy.context.object.dimensions.z = 2
        bpy.context.object.scale.xy = 520, 520
        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["2"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[2] = 1.04719
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 0.729722

        bpy.context.view_layer.objects.active = bpy.data.objects['18']
        bpy.context.object.location.xyz = 0, 0, 11
        bpy.context.object.dimensions.z = 2
        bpy.context.object.scale.xy = 520, 520
        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["18"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[0] = 0

        bpy.context.object.rotation_euler[2] = -2.0943951
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 0.729722

        bpy.context.view_layer.objects.active = bpy.data.objects['12']
        bpy.context.object.location.xyz = 0, 0, 11
        bpy.context.object.dimensions.z = 2
        bpy.context.object.scale.xy = 520, 520
        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["12"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[0] = 0

        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.object.rotation_euler[2] = -2.0944
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 0.729722
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.object.rotation_euler[2] = -2.0944
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.object.rotation_euler[0] = 3.14159
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)


        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.dimensions[2] = 20.7
        bpy.context.object.scale[1] = 13.024
        bpy.context.object.scale[0] = 13.024

        bpy.context.view_layer.objects.active = bpy.data.objects['1']
        bpy.context.object.location.xyz = 0, 0, 11
        bpy.context.object.dimensions.z = 2
        bpy.context.object.scale.xy = 520, 520
        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["1"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[2] = 1.04719
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 0.729722
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)


        bpy.context.view_layer.objects.active = bpy.data.objects['19']
        bpy.context.object.location.xyz = 0, 0, 11
        bpy.context.object.dimensions.z = 2
        bpy.context.object.scale.xy = 520, 520
        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["19"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[2] = 1.04719
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 0.729722

        bpy.context.view_layer.objects.active = bpy.data.objects['9']
        bpy.context.object.location.xyz = 0, 0, 11
        bpy.context.object.dimensions.z = 2
        bpy.context.object.scale.xy = 520, 520
        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["9"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[0] = 0
        bpy.context.object.rotation_euler[2] = -2.0944
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.object.rotation_euler[0] = 0.729722

        bpy.context.view_layer.objects.active = bpy.data.objects['3']
        bpy.context.object.location.xyz = 0, 0, 11
        bpy.context.object.dimensions.z = 2
        bpy.context.object.scale.xy = 520, 520
        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["3"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[0] = 0
        bpy.context.object.rotation_euler[2] = 1.0471976
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = -0.7297222

        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.object.rotation_euler[2] = 2.0943951
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.object.rotation_euler[0] = 0.729722
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)


        bpy.context.view_layer.objects.active = bpy.data.objects['13']
        bpy.context.object.location.xyz = 0, 0, 11
        bpy.context.object.dimensions.z = 2
        bpy.context.object.scale.xy = 520, 520
        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["13"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[2] = 1.04719
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 0.729722

        bpy.context.view_layer.objects.active = bpy.data.objects['5']
        bpy.context.object.location.xyz = 0, 0, 11
        bpy.context.object.dimensions.z = 2
        bpy.context.object.scale.xy = 520, 520
        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["5"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[0] = 0

        bpy.context.object.rotation_euler[2] = -2.0943951
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 0.729722

        bpy.context.view_layer.objects.active = bpy.data.objects['11']
        bpy.context.object.location.xyz = 0, 0, 11
        bpy.context.object.dimensions.z = 2
        bpy.context.object.scale.xy = 520, 520
        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["11"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[0] = 0
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.object.rotation_euler[2] = 1.0471976
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = -0.7297222

        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.object.rotation_euler[2] = 2.0944

        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.object.rotation_euler[0] = 0.729722
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.view_layer.objects.active = bpy.data.objects['7']
        bpy.context.object.location.xyz = 0, 0, 11
        bpy.context.object.dimensions.z = 2
        bpy.context.object.scale.xy = 520, 520
        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["7"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[2] = 1.04719
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 0.729722

        bpy.context.view_layer.objects.active = bpy.data.objects['17']
        bpy.context.object.location.xyz = 0, 0, 11
        bpy.context.object.dimensions.z = 2
        bpy.context.object.scale.xy = 520, 520
        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["17"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[0] = 0

        bpy.context.object.rotation_euler[2] = -2.0943951
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 0.729722

        bpy.context.view_layer.objects.active = bpy.data.objects['15']
        bpy.context.object.location.xyz = 0, 0, 11
        bpy.context.object.dimensions.z = 2
        bpy.context.object.scale.xy = 520, 520
        bpy.context.view_layer.objects.active = bpy.data.objects['Solid']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["15"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.data.objects.remove(bpy.data.objects["1"], do_unlink=True)

        bpy.data.objects.remove(bpy.data.objects["2"], do_unlink=True)

        bpy.data.objects.remove(bpy.data.objects["3"], do_unlink=True)

        bpy.data.objects.remove(bpy.data.objects["4"], do_unlink=True)

        bpy.data.objects.remove(bpy.data.objects["5"], do_unlink=True)

        bpy.data.objects.remove(bpy.data.objects["6"], do_unlink=True)

        bpy.data.objects.remove(bpy.data.objects["7"], do_unlink=True)
        bpy.data.objects.remove(bpy.data.objects["8"], do_unlink=True)

        bpy.data.objects.remove(bpy.data.objects["9"], do_unlink=True)
        bpy.data.objects.remove(bpy.data.objects["10"], do_unlink=True)
        bpy.data.objects.remove(bpy.data.objects["11"], do_unlink=True)

        bpy.data.objects.remove(bpy.data.objects["12"], do_unlink=True)

        bpy.data.objects.remove(bpy.data.objects["13"], do_unlink=True)

        bpy.data.objects.remove(bpy.data.objects["14"], do_unlink=True)

        bpy.data.objects.remove(bpy.data.objects["15"], do_unlink=True)

        bpy.data.objects.remove(bpy.data.objects["16"], do_unlink=True)

        bpy.data.objects.remove(bpy.data.objects["17"], do_unlink=True)
        bpy.data.objects.remove(bpy.data.objects["18"], do_unlink=True)

        bpy.data.objects.remove(bpy.data.objects["19"], do_unlink=True)
        bpy.data.objects.remove(bpy.data.objects["20"], do_unlink=True)

        bpy.data.objects.remove(bpy.data.objects["Cube"], do_unlink=True)

        bpy.data.objects.remove(bpy.data.objects["Camera"], do_unlink=True)

        bpy.data.objects.remove(bpy.data.objects["Light"], do_unlink=True)
        return {'FINISHED'}
    
def menu_draw(self, context):
        self.layout.operator("object.create_d20")


def register():
    bpy.utils.register_class(OBJECT_OT_create_d20)
    bpy.types.VIEW3D_MT_add.prepend(menu_draw)


def unregister():
    bpy.utils.unregister_class(OBJECT_OT_create_d20)
    bpy.types.VIEW3D_MT_add.remove(menu_draw)

if __name__ == "__main__":
    register()
