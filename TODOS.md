# Types
Better type for NodeBuilder.vars
NodeLoader.parseNodes json is Object<string, any>
ReflectorNode.getDepthNode and getDepthNode return ReflectorNode
ReflectorNode constructor default values for params does not exist
ReflectorBaseNode.textureNode is ReflectorNode (has getDepthNode only exists in ReflectorNode)
correct all generic errors ": Generic type "
All loaders method load onLoad params return type
For all pass, update uniforms type to Object<string, any>
TAARenderPass render render param (hould add commented input or just remove ?)
RTTNode problem for width being null instead of undefined (fix also for rttNode TSL function)

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
Remove ...arguments calls (only if PR for Object3D pass)
Delete as much eslint-disable-next-line as possible
