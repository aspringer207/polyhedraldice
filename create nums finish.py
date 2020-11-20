import bpy
bpy.ops.object.mode_set( mode   = 'EDIT'   )
bpy.ops.mesh.select_mode( type  = 'FACE'   )
bpy.ops.mesh.select_all( action = 'SELECT' )

bpy.ops.mesh.extrude_region_move(
    TRANSFORM_OT_translate={"value":(0, 0, 3)}
)

bpy.ops.object.mode_set( mode = 'OBJECT' )

for i in range (0, 29, 1):
    obj = bpy.data.objects[i]
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME')
    bpy.context.object.dimensions.z = 1
    bpy.context.object.scale.xy = 0.01, 0.01
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)