# Types
Color4 set g and b can be nullable
Renderer _renderObjectDirect & _createObjectPipeline pass id not null by default
TGALoader parse buffer is string
All KeyframeTrack values type are wrong (boolean, ....)
physics_ammo_break:541
physics_ammo_break:563
RapierPhysics.world export physics_rapier_joints
RapierPhysics.addHeightfield export physics_rapier_terrain
webgl_loader_nrrd.html:73 is really matrix3 ?
examples/webgl_multiple_elements_text.js(43,22): error TS2339: Property 'lattice' does not exist on type 'Element'.
examples/webgl_postprocessing_3dlut.js(126,9): error TS2339: Property 'width' does not exist on type 'GUI'.
examples/webgl_renderer_pathtracer.js(343,76): error TS2554: Expected 1 arguments, but got 2. (Math.round)
examples/webgpu_compute_birds.js(314,13): error TS2339: Property 'equal' does not exist on type 'number'.
NodeMaterial.alphaTestNode can be number
examples/webgpu_xr_native_layers.js(443,38): error TS2554: Expected 0 arguments, but got 2. Interactive group constructor takes no parameter
AnimationClipCreator construtor takes an array of booleans
WebGPUPipelineUtils.js _getColorWriteMask return a number
src/renderers/webgpu/nodes/WGSLNodeBuilder.js(633,95): error TS2554: Expected 4-5 arguments, but got 6.
examples/jsm/capabilities/WebGPU.js(5,2)
src/renderers/webgpu/utils/WebGPUPipelineUtils.js(719,70)
src/renderers/webgl-fallback/WebGLBackend.js(458,57)
src/renderers/webgl-fallback/WebGLBackend.js(186,13)
examples/jsm/tsl/display/TRAANode.js(17,14): error TS8023: JSDoc '@augments PassNode' does not match the 'extends TempNode' clause.

type LoopNodeObjectParameter can have name parameter
examples/jsm/tsl/display/TRAANode.js(355,76): error TS2353: Object literal may only specify known properties, and 'name' does not exist in type 'Node | LoopNodeObjectParameter'.
examples/jsm/tsl/display/TRAANode.js(355,93): error TS2339: Property 'x' does not exist on type '{ readonly i: number; }'.

src/loaders/FileLoader.js(242,46): error TS2345: Argument of type 'string' is not assignable to parameter of type 'DOMParserSupportedType'.

src/materials/nodes/MeshSSSNodeMaterial.js(63,65): error TS2554: Expected 1 arguments, but got 2.

src/nodes/display/ViewportTextureNode.js(94,13): error TS2314: Generic type 'WeakMap<K, V>' requires 2 type argument(s).

src/renderers/webxr/WebXRManager.js(815,5): error TS2322: Type 'undefined' is not assignable to type 'number'.

# Dev
WebGlRendere.setClearAlpha and setClearColor should not used arguments keyword
WebGPUTextureUtils._getDefaultVideoFrame could be simplified ?
Rename GPUFeatureName Supported feature
Add features to GPUFeatureName
Cleaner reset to null in HtmlMesh.dispose (clearTimeout and then set to null)


# Investigate
Find a way to generate editor\js\libs\tern-threejs\threejs.js
