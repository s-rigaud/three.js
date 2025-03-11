# Types
fix type of Shadowmapviewer.position
oculushandpointer.attached is not nullable
XRHandMeshModel.path is nullable in constructor
Better type for NodeBuilder.vars
Add Color has color type for Color4.set
Renderer.compute result is not null but undefined
Renderer.compile return a function not a promise
ViewHelper.handleClick has event of type MouseEvent
FileLoader :122 .requestHeader is Object<string, string> (set everywhere)
ImageBitmaploader.requestHeader is Object<string, string> (set everywhere)
NodeLoader.parseNodes json is Object<string, any>
ReflectorNode.getDepthNode and getDepthNode return ReflectorNode
ReflectorNode constructor default values for params does not exist
ReflectorBaseNode.textureNode is ReflectorNode (has getDepthNode only exists in ReflectorNode)
correct all generic errors ": Generic type "
All loaders method load onLoad params return type
UltraHDRLoader.js :350 type of function is wrong
MD2Loader.load can have undefined functions


# Dev
Use MaterialLoader.js and Material.js to fix tab of material attributes
webgl_geometry_extrude_shapes .link remove
webgl_geometry_nurbs event param missing for onPointerUp
webgl_geometry_shapes event param missing for onPointerUp
webgl_geometry_text event param missing for onPointerUp
webgl_loader_ttf event param missing for onPointerUp
webgl_panorama_equirectangular event param missing for onPointerUp
webgl_loader_ldraw :172 no tone mapping on Material
webgl_loader_ldraw bad usage of Math.round (multiple)
webgl_loader_texture_pvrtc no encoding param for texture
webgl_materials_cubemap_render_to_mipmaps :92  is array instanciated but {} no valid value
webgl_mesh_batch ref to this.maxInstanceCount
webgl_multiple_views :236 there is no mouseY param
webgl_postprocessing_3dlut :116 needs {} for lut pass
webgl_renderer_pathtracer Math.round only take one param
webgpu_compute_sort_bitonic :478 comparison ??
webgpu_multisampled_renderbuffers Array.fill not empty, use Array.from instead
webgpu_tsl_compute_attractors_particles accessing TransformControls.visible
webgpu_tsl_halftone :180 setSclar takes only one param
ColladaLoader : 2104 distance not ok on DirectionalLight
LDrawLoader :2264 don't use class but object
LWOLoadr :354 additonal argument
LWOLoadr :538 additonal argument
LWOLoadr :825 additonal argument
MD2Loader.js :144 should be BufferGeo as input
RGBMLoader.setMaxRange is 7 or 16

# Investigate
RTTNode problem for width undefined, passing null, ... ??
See if https://jsdoc.app/tags-this can be used
Remove ...arguments calls
Delete as much eslint-disable-next-line as possible
