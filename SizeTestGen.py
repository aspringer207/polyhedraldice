import bpy

bpy.ops.mesh.primitive_solid_add()
bpy.context.object.location[0] = -50
bpy.context.object.dimensions[2] = 20
bpy.context.object.scale[0] = 15
bpy.context.object.scale[1] = 15
bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
bpy.context.object.rotation_euler[2] = -0.523599
bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
bpy.context.object.rotation_euler[1] = 3.14159
bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

bpy.context.view_layer.objects.active = bpy.data.objects['4']

bpy.context.object.location[0] = -50
bpy.context.object.location[1] = 6
bpy.context.object.location[2] = 5.6
bpy.context.object.rotation_euler[0] = 0
bpy.context.object.rotation_euler[1] = 0
bpy.context.object.rotation_euler[2] = 0
bpy.context.object.scale[0] = 800
bpy.context.object.scale[1] = 800
bpy.context.object.dimensions[2] = 2

bpy.ops.mesh.primitive_cube_add(size=16, enter_editmode=False, align='WORLD', location=(-50, 50, 0))

bpy.context.view_layer.objects.active = bpy.data.objects['4.001']
bpy.context.object.location[0] = -50
bpy.context.object.location[1] = 50
bpy.context.object.location[2] = 8.6
bpy.context.object.scale[0] = 1250
bpy.context.object.scale[1] = 1250
bpy.context.object.dimensions[2] = 2

bpy.ops.mesh.primitive_solid_add(source='8')

bpy.context.object.rotation_euler[1] = 0.785398
bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
bpy.context.object.rotation_euler[0] = 0.61549
bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
bpy.context.object.dimensions[2] = 16.4
bpy.context.object.scale[1] = 14.203
bpy.context.object.scale[0] = 14.203 
bpy.context.object.location[0] = -50
bpy.context.object.location[1] = -50

bpy.context.view_layer.objects.active = bpy.data.objects['4.002']

bpy.context.object.location[0] = -50
bpy.context.object.location[1] = -50
bpy.context.object.location[2] = 8.6
bpy.context.object.rotation_euler[0] = 0
bpy.context.object.rotation_euler[1] = 0
bpy.context.object.rotation_euler[2] = 0
bpy.context.object.scale[0] = 1000
bpy.context.object.scale[1] = 1000
bpy.context.object.dimensions[2] = 2

bpy.ops.mesh.primitive_cone_add(vertices=5, radius1=2, radius2=0, depth=2.25, enter_editmode=False, align='WORLD', location=(0, -50, 0))

bpy.ops.mesh.primitive_cone_add(vertices=5, radius1=2, radius2=0, depth=2.25, enter_editmode=False, align='WORLD', location=(0, -50, 0))

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

bpy.context.view_layer.objects.active = bpy.data.objects['4.003']

bpy.context.object.location[0] = 0
bpy.context.object.location[1] = -50.75
bpy.context.object.location[2] = 9
bpy.context.object.scale[0] = 1000
bpy.context.object.scale[1] = 1000
bpy.context.object.dimensions[2] = 2

bpy.ops.mesh.primitive_cone_add(vertices=5, radius1=2, radius2=0, depth=2.25, enter_editmode=False, align='WORLD', location=(50, -50, 0))

bpy.ops.mesh.primitive_cone_add(vertices=5, radius1=2, radius2=0, depth=2.25, enter_editmode=False, align='WORLD', location=(50, -50, 0))

bpy.context.view_layer.objects.active = bpy.data.objects['Cone.003']

bpy.context.object.rotation_euler[0] = 3.14159
bpy.context.view_layer.objects.active = bpy.data.objects['Cone.003']

bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
bpy.ops.object.modifier_add(type='BOOLEAN')
bpy.context.object.modifiers["Boolean"].operation = 'INTERSECT'
bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["Cone.002"]
bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

bpy.context.object.rotation_euler[0] = -0.947714
bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

bpy.context.object.dimensions[2] = 17
bpy.context.object.scale[1] = 12.937 
bpy.context.object.scale[0] = 12.937

bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

bpy.context.view_layer.objects.active = bpy.data.objects['40']

bpy.context.object.location[0] = 50
bpy.context.object.location[1] = -52.5
bpy.context.object.location[2] = 9
bpy.context.object.scale[0] = 750
bpy.context.object.scale[1] = 750
bpy.context.object.dimensions[2] = 2

bpy.ops.mesh.primitive_solid_add(source='12')
bpy.context.object.rotation_euler[0] = -1.01727
bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
bpy.context.object.dimensions[2] = 18.5
bpy.context.object.scale[1] = 11.64
bpy.context.object.scale[0] = 11.64
bpy.context.object.location[1] = 50
bpy.context.view_layer.objects.active = bpy.data.objects['4.004']
bpy.context.object.location[0] = 0
bpy.context.object.location[1] = 50
bpy.context.object.location[2] = 9.5
bpy.context.object.scale[0] = 1000
bpy.context.object.scale[1] = 1000
bpy.context.object.dimensions[2] = 2

bpy.ops.mesh.primitive_solid_add(source='20')
bpy.context.object.location[0] = 50
bpy.context.object.rotation_euler[0] = 0.364861

bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
bpy.context.object.dimensions[2] = 20.7
bpy.context.object.scale[1] = 13.024
bpy.context.object.scale[0] = 13.024
bpy.context.view_layer.objects.active = bpy.data.objects['4.005']
bpy.context.object.location[0] = 50
bpy.context.object.location[1] = 0
bpy.context.object.location[2] = 11
bpy.context.object.scale[0] = 520
bpy.context.object.scale[1] = 520
bpy.context.object.dimensions[2] = 2

