bl_info = {
    "name": "Create D10",
    "version": (1, 0),
    "blender": (2, 65, 0),
    "category": "Add",
    "author": "Andrea Springer"
}


import bpy

class OBJECT_OT_create_d10(bpy.types.Operator):
    """D6 Generation Script"""     
    bl_idname = "object.create_d10"        
    bl_label = "Create D10"         
    bl_options = {'REGISTER', 'UNDO'}  

    def execute(self, context):

        bpy.ops.mesh.primitive_cone_add(vertices=5, radius1=2, radius2=0, depth=2.25, enter_editmode=False, align='WORLD', location=(0, 0, 0))

        bpy.ops.mesh.primitive_cone_add(vertices=5, radius1=2, radius2=0, depth=2.25, enter_editmode=False, align='WORLD', location=(0, 0, 0))

        bpy.context.view_layer.objects.active = bpy.data.objects['Cone.001']

        bpy.context.object.rotation_euler[0] = 3.14159
        bpy.context.view_layer.objects.active = bpy.data.objects['Cone.001']

        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].operation = 'INTERSECT'
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["Cone"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[0] = -0.947714
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.object.dimensions[2] = 17
        bpy.context.object.scale[1] = 12.937 
        bpy.context.object.scale[0] = 12.937

        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

        bpy.context.view_layer.objects.active = bpy.data.objects['6']

        bpy.context.object.location[0] = 0
        bpy.context.object.location[1] = -.75
        bpy.context.object.location[2] = 9
        bpy.context.object.dimensions[2] = 2
        bpy.context.object.scale[0] = 1000
        bpy.context.object.scale[1] = 1000

        bpy.context.view_layer.objects.active = bpy.data.objects['Cone.001']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["6"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[0] = -0.6230825
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[1] = -1.2566371
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 0.6230825
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.view_layer.objects.active = bpy.data.objects['4']

        bpy.context.object.location[0] = 0
        bpy.context.object.location[1] = -.75
        bpy.context.object.location[2] = 9
        bpy.context.object.dimensions[2] = 2
        bpy.context.object.scale[0] = 1000
        bpy.context.object.scale[1] = 1000

        bpy.context.view_layer.objects.active = bpy.data.objects['Cone.001']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["4"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[0] = -0.6230825
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[1] = -1.2566371
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 0.6230825
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.view_layer.objects.active = bpy.data.objects['0']

        bpy.context.object.location[0] = 0
        bpy.context.object.location[1] = -.75
        bpy.context.object.location[2] = 9
        bpy.context.object.dimensions[2] = 2
        bpy.context.object.scale[0] = 1000
        bpy.context.object.scale[1] = 1000

        bpy.context.view_layer.objects.active = bpy.data.objects['Cone.001']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["0"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[0] = -0.6230825
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[1] = -1.2566371
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 0.6230825
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.view_layer.objects.active = bpy.data.objects['8']

        bpy.context.object.location[0] = 0
        bpy.context.object.location[1] = -.75
        bpy.context.object.location[2] = 9
        bpy.context.object.dimensions[2] = 2
        bpy.context.object.scale[0] = 1000
        bpy.context.object.scale[1] = 1000

        bpy.context.view_layer.objects.active = bpy.data.objects['Cone.001']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["8"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[0] = -0.6230825
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[1] = -1.2566371
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 0.6230825
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.view_layer.objects.active = bpy.data.objects['2']

        bpy.context.object.location[0] = 0
        bpy.context.object.location[1] = -.75
        bpy.context.object.location[2] = 9
        bpy.context.object.dimensions[2] = 2
        bpy.context.object.scale[0] = 1000
        bpy.context.object.scale[1] = 1000

        bpy.context.view_layer.objects.active = bpy.data.objects['Cone.001']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["2"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[0] = 3.1415927
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.view_layer.objects.active = bpy.data.objects['7']

        bpy.context.object.location[0] = 0
        bpy.context.object.location[1] = -.75
        bpy.context.object.location[2] = 9
        bpy.context.object.dimensions[2] = 2
        bpy.context.object.scale[0] = 1000
        bpy.context.object.scale[1] = 1000


        bpy.context.view_layer.objects.active = bpy.data.objects['Cone.001']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["7"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[0] = -0.6230825
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[1] = -1.2566371
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 0.6230825
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.view_layer.objects.active = bpy.data.objects['1']

        bpy.context.object.location[0] = 0
        bpy.context.object.location[1] = -.75
        bpy.context.object.location[2] = 9
        bpy.context.object.dimensions[2] = 2
        bpy.context.object.scale[0] = 1000
        bpy.context.object.scale[1] = 1000

        bpy.context.view_layer.objects.active = bpy.data.objects['Cone.001']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["1"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[0] = -0.6230825
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[1] = -1.2566371
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 0.6230825
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.view_layer.objects.active = bpy.data.objects['9']

        bpy.context.object.location[0] = 0
        bpy.context.object.location[1] = -.75
        bpy.context.object.location[2] = 9
        bpy.context.object.dimensions[2] = 2
        bpy.context.object.scale[0] = 1000
        bpy.context.object.scale[1] = 1000

        bpy.context.view_layer.objects.active = bpy.data.objects['Cone.001']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["9"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[0] = -0.6230825
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[1] = -1.2566371
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 0.6230825
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.view_layer.objects.active = bpy.data.objects['5']

        bpy.context.object.location[0] = 0
        bpy.context.object.location[1] = -.75
        bpy.context.object.location[2] = 9
        bpy.context.object.dimensions[2] = 2
        bpy.context.object.scale[0] = 1000
        bpy.context.object.scale[1] = 1000

        bpy.context.view_layer.objects.active = bpy.data.objects['Cone.001']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["5"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[0] = -0.6230825
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[1] = -1.2566371
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 0.6230825
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.view_layer.objects.active = bpy.data.objects['3']

        bpy.context.object.location[0] = 0
        bpy.context.object.location[1] = -.75
        bpy.context.object.location[2] = 9
        bpy.context.object.dimensions[2] = 2
        bpy.context.object.scale[0] = 1000
        bpy.context.object.scale[1] = 1000

        bpy.context.view_layer.objects.active = bpy.data.objects['Cone.001']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["3"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")
        
        objs = bpy.data.objects

        objs.remove(objs["1"], do_unlink=True)

        objs.remove(objs["2"], do_unlink=True)

        objs.remove(objs["3"], do_unlink=True)

        objs.remove(objs["4"], do_unlink=True)

        objs.remove(objs["5"], do_unlink=True)

        objs.remove(objs["6"], do_unlink=True)
        
        objs.remove(objs["7"], do_unlink=True)
        objs.remove(objs["8"], do_unlink=True)

        objs.remove(objs["9"], do_unlink=True)
        objs.remove(objs["0"], do_unlink=True)
        objs.remove(objs["Cone"], do_unlink=True)
        
        objs.remove(objs["Camera"], do_unlink=True)
        

        objs.remove(objs["Light"], do_unlink=True)

        return {'FINISHED'}

def menu_draw(self, context):
        self.layout.operator("object.create_d10")


def register():
    bpy.utils.register_class(OBJECT_OT_create_d10)
    bpy.types.VIEW3D_MT_add.prepend(menu_draw)


def unregister():
    bpy.utils.unregister_class(OBJECT_OT_create_d10)
    bpy.types.VIEW3D_MT_add.remove(menu_draw)

if __name__ == "__main__":
    register()

