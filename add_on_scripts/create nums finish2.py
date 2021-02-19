bl_info = {
    "name": "Finish Numbers",
    "category": "Add",
    "author": "Andrea Springer",
    "version": (1, 0),
    "blender": (2, 90, 0),
}

import bpy

class OBJECT_OT_finish_nums(bpy.types.Operator):
    """Number Finisher Script"""     
    bl_idname = "object.finish_nums"        
    bl_label = "Finish Numbers"         
    bl_options = {'REGISTER', 'UNDO'}  

    def execute(self, context):

        ob1 = bpy.context.scene.objects["1"]       # Get the object
        bpy.ops.object.select_all(action='DESELECT') # Deselect all objects
        bpy.context.view_layer.objects.active = ob1   # Make the number 0 the active object 
        ob1.select_set(True)
        bpy.ops.object.select_all(action='SELECT') 


        bpy.ops.object.convert(target='MESH')

        bpy.ops.object.mode_set( mode   = 'EDIT'   )
        bpy.ops.mesh.select_mode( type  = 'FACE'   )
        bpy.ops.mesh.select_all( action = 'SELECT' )
        bpy.ops.mesh.extrude_region_shrink_fatten(MESH_OT_extrude_region={"use_normal_flip":False, "use_dissolve_ortho_edges":False, "mirror":False}, TRANSFORM_OT_shrink_fatten={"value":0.309797, "use_even_offset":False, "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "release_confirm":False, "use_accurate":False})
        bpy.ops.object.mode_set(mode='OBJECT')

            
        for i in range (0, 34, 1):
            obj = bpy.data.objects[i]
            bpy.context.view_layer.objects.active = obj
            bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME')
            bpy.context.object.dimensions.z = 1
            bpy.context.object.scale.xy = 0.01, 0.01, 
            bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
            
        return {'FINISHED'}

def menu_draw(self, context):
        self.layout.operator("object.finish_nums")


def register():
    bpy.utils.register_class(OBJECT_OT_finish_nums)
    bpy.types.VIEW3D_MT_add.prepend(menu_draw)


def unregister():
    bpy.utils.unregister_class(OBJECT_OT_finish_nums)
    bpy.types.VIEW3D_MT_add.remove(menu_draw)

if __name__ == "__main__":
    register()
