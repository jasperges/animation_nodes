import bpy
from .. base_types.socket import AnimationNodeSocket

class PolygonIndicesListSocket(bpy.types.NodeSocket, AnimationNodeSocket):
    bl_idname = "mn_PolygonIndicesListSocket"
    bl_label = "Polygon Indices List Socket"
    dataType = "Polygon Indices List"
    allowedInputTypes = ["Polygon Indices List"]
    drawColor = (0.4, 0.2, 1.0, 1)

    def drawInput(self, layout, node, text):
        layout.label(text)

    def getValue(self):
        return []

    def getCopyValueFunctionString(self):
        return "return [polygonIndices[:] for polygonIndices in value]"
