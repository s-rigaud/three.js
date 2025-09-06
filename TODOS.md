# Types
examples/jsm/tsl/display/Lut3DNode.js:63
examples/jsm/tsl/display/PixelationPassNode.js:305
every setup() { method builder argument
examples/physics_ammo_break.js:513 - error TS2554: Expected 5 arguments, but got 6.
examples/physics_ammo_break.js:535 - error TS2554: Expected 5 arguments, but got 6.
examples/webgl_gpgpu_birds_gltf.js:23 - replace by MathUtils.js lerp ?
examples/webgl_gpgpu_water.js:194 - 195 - props on mesh not geometry
examples/webgl_lines_fat_raycasting.js:63 - use 0 no threshold
examples/webgpu_lines_fat_raycasting.js:63 - use 0 no threshold
examples/webgl_loader_ldraw.js:340
examples/webgpu_camera_logarithmicdepthbuffer.js:125 - error TS2322: Type 'Color' is not assignable to type 'number'. - Type consistency always color
examples/webgpu_compute_birds.js:302 - error TS2339: Property 'equal' does not exist on type 'number'.
examples/webgpu_compute_reduce.js:750 - error TS2554: Expected 1-2 arguments, but got 3.
examples/webgpu_compute_reduce.js:761 - error TS2554: Expected 1-2 arguments, but got 3.
examples/webgpu_compute_reduce.js:763 - error TS2554: Expected 1-2 arguments, but got 3.
examples/webgpu_instance_uniform.js:127 - error TS2339: Property 'color' does not exist on type 'Mesh<any, any, Object3DEventMap>'.
examples/webgpu_loader_texture_ktx2.js:88 - error TS2339: Property 'supported' does not exist on type '{ path: string; }'.
examples/webgl_loader_nrrd.js:48 - error TS2345: Argument of type 'Matrix3' is not assignable to parameter of type 'Matrix4'. - NRRDLoader :443 can use Matrix4 for Volume

# Dev

# Investigate
examples/webgl_loader_nrrd.js:89 - error TS2339: Property 'min' does not exist on type 'Volume'.
examples/webgl_loader_nrrd.js:89 - error TS2345: Argument of type '"windowLow"' is not assignable to parameter of type 'KeyToValueOfType<Volume, number>'.
examples/webgl_loader_nrrd.js:94 - error TS2345: Argument of type '"windowHigh"' is not assignable to parameter of type 'KeyToValueOfType<Volume, number>'.

Find a way to generate editor\js\libs\tern-threejs\threejs.js

Automate this process:

* extract Js examples script code
* Replace Jsdocs types by their definitions
* compute TS errors
* Filter results
* checkout everything except type-errors

# Easy type error search

@augments
Type 'null' is not assignable to type
Generic type '
regex " (\w+) - .*\n .*\[(\1)"
regex " ([a-zA-Z]+?) (\1) "

# Removing JSdoc type regex
\/\*\*\n( \*.*\n)*( \*(\*)?/\n)\n
