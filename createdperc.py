bl_info = {
    "name": "Create Percentile Die",
    "category": "Add",
    "author": "Andrea Springer",
    "version": (1, 0),
    "blender": (2, 83, 0),
    "description": "Creates a percentile die model from user prepared numerals or symbols.",
    "tracker_url": "https://github.com/aspringer207/polyhedraldice",
    "support": "TESTING",
}


import bpy

class OBJECT_OT_create_dpct(bpy.types.Operator):
    """Pecentile Generation Script"""     
    bl_idname = "object.create_dpct"        
    bl_label = "Create Percentile Die"         
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

        bpy.context.view_layer.objects.active = bpy.data.objects['00']

        bpy.context.object.location[0] = 0
        bpy.context.object.location[1] = -2.5
        bpy.context.object.location[2] = 9
        bpy.context.object.dimensions[2] = 2
        bpy.context.object.scale[0] = 750
        bpy.context.object.scale[1] = 750

        bpy.context.view_layer.objects.active = bpy.data.objects['Cone.001']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["00"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[0] = -0.6230825
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[1] = -1.2566371
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 0.6230825
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.view_layer.objects.active = bpy.data.objects['80']

        bpy.context.object.location[0] = 0
        bpy.context.object.location[1] = -2.5
        bpy.context.object.location[2] = 9
        bpy.context.object.dimensions[2] = 2
        bpy.context.object.scale[0] = 750
        bpy.context.object.scale[1] = 750

        bpy.context.view_layer.objects.active = bpy.data.objects['Cone.001']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["80"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[0] = -0.6230825
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[1] = -1.2566371
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 0.6230825
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.view_layer.objects.active = bpy.data.objects['20']

        bpy.context.object.location[0] = 0
        bpy.context.object.location[1] = -2.5
        bpy.context.object.location[2] = 9
        bpy.context.object.dimensions[2] = 2
        bpy.context.object.scale[0] = 750
        bpy.context.object.scale[1] = 750

        bpy.context.view_layer.objects.active = bpy.data.objects['Cone.001']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["20"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[0] = -0.6230825
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[1] = -1.2566371
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 0.6230825
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.view_layer.objects.active = bpy.data.objects['60']

        bpy.context.object.location[0] = 0
        bpy.context.object.location[1] = -2.5
        bpy.context.object.location[2] = 9
        bpy.context.object.dimensions[2] = 2
        bpy.context.object.scale[0] = 750
        bpy.context.object.scale[1] = 750

        bpy.context.view_layer.objects.active = bpy.data.objects['Cone.001']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["60"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[0] = -0.6230825
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[1] = -1.2566371
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 0.6230825
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.view_layer.objects.active = bpy.data.objects['40']

        bpy.context.object.location[0] = 0
        bpy.context.object.location[1] = -2.5
        bpy.context.object.location[2] = 9
        bpy.context.object.dimensions[2] = 2
        bpy.context.object.scale[0] = 750
        bpy.context.object.scale[1] = 750

        bpy.context.view_layer.objects.active = bpy.data.objects['Cone.001']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["40"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[0] = 3.1415927
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.view_layer.objects.active = bpy.data.objects['50']

        bpy.context.object.location[0] = 0
        bpy.context.object.location[1] = -2.5
        bpy.context.object.location[2] = 9
        bpy.context.object.dimensions[2] = 2
        bpy.context.object.scale[0] = 750
        bpy.context.object.scale[1] = 750


        bpy.context.view_layer.objects.active = bpy.data.objects['Cone.001']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["50"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[0] = -0.6230825
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[1] = -1.2566371
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 0.6230825
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.view_layer.objects.active = bpy.data.objects['30']

        bpy.context.object.location[0] = 0
        bpy.context.object.location[1] = -2.5
        bpy.context.object.location[2] = 9
        bpy.context.object.dimensions[2] = 2
        bpy.context.object.scale[0] = 750
        bpy.context.object.scale[1] = 750

        bpy.context.view_layer.objects.active = bpy.data.objects['Cone.001']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["30"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[0] = -0.6230825
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[1] = -1.2566371
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 0.6230825
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.view_layer.objects.active = bpy.data.objects['70']

        bpy.context.object.location[0] = 0
        bpy.context.object.location[1] = -2.5
        bpy.context.object.location[2] = 9
        bpy.context.object.dimensions[2] = 2
        bpy.context.object.scale[0] = 750
        bpy.context.object.scale[1] = 750

        bpy.context.view_layer.objects.active = bpy.data.objects['Cone.001']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["70"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[0] = -0.6230825
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[1] = -1.2566371
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 0.6230825
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.view_layer.objects.active = bpy.data.objects['10']

        bpy.context.object.location[0] = 0
        bpy.context.object.location[1] = -2.5
        bpy.context.object.location[2] = 9
        bpy.context.object.dimensions[2] = 2
        bpy.context.object.scale[0] = 750
        bpy.context.object.scale[1] = 750

        bpy.context.view_layer.objects.active = bpy.data.objects['Cone.001']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["10"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        bpy.context.object.rotation_euler[0] = -0.6230825
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[1] = -1.2566371
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler[0] = 0.6230825
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.view_layer.objects.active = bpy.data.objects['90']

        bpy.context.object.location[0] = 0
        bpy.context.object.location[1] = -2.5
        bpy.context.object.location[2] = 9
        bpy.context.object.dimensions[2] = 2
        bpy.context.object.scale[0] = 750
        bpy.context.object.scale[1] = 750

        bpy.context.view_layer.objects.active = bpy.data.objects['Cone.001']
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["90"]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

        objs = bpy.data.objects

        objs.remove(objs["00"], do_unlink=True)

        objs.remove(objs["10"], do_unlink=True)

        objs.remove(objs["20"], do_unlink=True)

        objs.remove(objs["30"], do_unlink=True)

        objs.remove(objs["40"], do_unlink=True)

        objs.remove(objs["50"], do_unlink=True)
        
        objs.remove(objs["60"], do_unlink=True)
        objs.remove(objs["70"], do_unlink=True)

        objs.remove(objs["80"], do_unlink=True)
        objs.remove(objs["90"], do_unlink=True)
        objs.remove(objs["Cone"], do_unlink=True)
        
        objs.remove(objs["Camera"], do_unlink=True)

        objs.remove(objs["Light"], do_unlink=True)

        return {'FINISHED'}

def menu_draw(self, context):
        self.layout.operator("object.create_dpct")


def register():
    bpy.utils.register_class(OBJECT_OT_create_dpct)
    bpy.types.VIEW3D_MT_add.prepend(menu_draw)


def unregister():
    bpy.utils.unregister_class(OBJECT_OT_create_dpct)
    bpy.types.VIEW3D_MT_add.remove(menu_draw)

if __name__ == "__main__":
    register()
