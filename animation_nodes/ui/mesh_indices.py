import bpy
from .. draw_handler import drawHandler
from .. preferences import getMeshIndicesSettings
from .. graphics.mesh_indices import (
    drawVertexIndices_ObjectMode,
    drawEdgeIndices_ObjectMode,
    drawPolygonIndices_ObjectMode
)

@drawHandler("SpaceView3D", "WINDOW")
def drawIndicesOfSelectedObjects():
    prefs = getMeshIndicesSettings()
    if not (prefs.drawVertices or prefs.drawEdges or prefs.drawPolygons):
        return

    for object in bpy.context.selected_objects:
        if object.type == "MESH" and object.mode == "OBJECT":
            if prefs.drawVertices:
                drawVertexIndices_ObjectMode(object,
                    color = prefs.verticesColor,
                    fontSize = prefs.fontSize)
            if prefs.drawEdges:
                drawEdgeIndices_ObjectMode(object,
                    color = prefs.edgesColor,
                    fontSize = prefs.fontSize)
            if prefs.drawPolygons:
                drawPolygonIndices_ObjectMode(object,
                    color = prefs.polygonsColor,
                    fontSize = prefs.fontSize)

def drawPanel(self, context):
    if context.mode != "OBJECT":
        return

    prefs = getMeshIndicesSettings()

    col = self.layout.column()

    row = col.row()
    row.prop(prefs, "drawVertices", text = "Vertex Indices")
    subRow = row.row()
    subRow.active = prefs.drawVertices
    subRow.prop(prefs, "verticesColor", text = "")

    row = col.row()
    row.prop(prefs, "drawEdges", text = "Edge Indices")
    subRow = row.row()
    subRow.active = prefs.drawEdges
    subRow.prop(prefs, "edgesColor", text = "")

    row = col.row()
    row.prop(prefs, "drawPolygons", text = "Polygons Indices")
    subRow = row.row()
    subRow.active = prefs.drawPolygons
    subRow.prop(prefs, "polygonsColor", text = "")

def register():
    bpy.types.VIEW3D_PT_view3d_display.append(drawPanel)

def unregister():
    bpy.types.VIEW3D_PT_view3d_display.remove(drawPanel)
