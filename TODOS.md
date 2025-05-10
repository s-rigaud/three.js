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



# Dev
WebGlRendere.setClearAlpha and setClearColor should not used arguments keyword
WebGPUTextureUtils._getDefaultVideoFrame could be simplified ?
Rename GPUFeatureName Supported feature
Add features to GPUFeatureName
Cleaner reset to null in HtmlMesh.dispose (clearTimeout and then set to null)


# Investigate
Find a way to generate editor\js\libs\tern-threejs\threejs.js
