bl_info = {
    "name": "Create D6",
    "category": "Add",
    "author": "Andrea Springer"
    "description": "Creates a D6 model from user prepared numerals or symbols.",
    "tracker_url": "https://github.com/aspringer207/polyhedraldice",
    "support": "TESTING",
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
        
        objs = bpy.data.objects

        objs.remove(objs["1"], do_unlink=True)

        objs.remove(objs["2"], do_unlink=True)

        objs.remove(objs["3"], do_unlink=True)

        objs.remove(objs["4"], do_unlink=True)

        objs.remove(objs["5"], do_unlink=True)

        objs.remove(objs["6"], do_unlink=True)

        objs.remove(objs["Camera"], do_unlink=True)

        objs.remove(objs["Light"], do_unlink=True)
        

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
