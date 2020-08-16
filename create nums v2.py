import bpy

for i in range(0,21,1):
    obj = bpy.data.curves.new(type="FONT",name= str(i))
    num = str(i)
    myFontOb = bpy.data.objects.new(num, obj)
    myFontOb.data.body = str(i)
    bpy.context.collection.objects.link(myFontOb)
    
for i in range(30, 91, 10):
    pobj = bpy.data.curves.new(type="FONT", name= str(i))
    pnum = str(i)
    myPFontOb = bpy.data.objects.new(pnum, pobj)
    myPFontOb.data.body = str(i)
    bpy.context.collection.objects.link(myPFontOb)

zobj = bpy.data.curves.new(type="FONT",name= "00")
myZFontOb = bpy.data.objects.new("00", zobj)
myZFontOb.data.body = "00"
bpy.context.collection.objects.link(myZFontOb)

line = bpy.data.curves.new(type="FONT", name= "line")
FontLine = bpy.data.objects.new("line", line)
FontLine.data.body = "_" 
bpy.context.collection.objects.link(FontLine)
        
for i in range(0, 30, 1): 
    font_filepath = "C:\\Users\\andre\\Downloads\\noir_et_blanc\\N_E_B_B.TTF"
    bpy.data.curves[i].font = bpy.data.fonts.load(filepath= font_filepath)

bpy.ops.object.duplicate(
        {"object" : bpy.data.objects['6'],
         "selected_objects" : [bpy.data.objects['6']]},
        linked=True)
bpy.ops.object.duplicate(
        {"object" : bpy.data.objects['9'],
         "selected_objects" : [bpy.data.objects['9']]},
        linked=True)
bpy.ops.object.duplicate(
        {"object" : bpy.data.objects['line'],
         "selected_objects" : [bpy.data.objects['line']]},
        linked=True)
        
for i in range (0, 33, 1):
    obj = bpy.data.objects[i]
    bpy.ops.object.make_single_user(object=True, obdata=True, material=False, animation=False)

for i in range (0, 33, 1):
    obj = bpy.data.objects[i] 
    bpy.context.view_layer.objects.active = obj
    bpy.context.object.select_set( state = True, view_layer = None)
    bpy.ops.object.convert(target='MESH', keep_original=False)
    

bpy.ops.object.mode_set( mode   = 'EDIT'   )
bpy.ops.mesh.select_mode( type  = 'FACE'   )
bpy.ops.mesh.select_all( action = 'SELECT' )

bpy.ops.mesh.extrude_region_move(
    TRANSFORM_OT_translate={"value":(0, 0, 3)}
)

bpy.ops.object.mode_set( mode = 'OBJECT' )

for i in range (0, 33, 1):
    obj = bpy.data.objects[i]
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME')
    bpy.context.object.dimensions.z = 1
    bpy.context.object.scale.xy = 0.01, 0.01
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

