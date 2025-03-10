# Types
fix type of Shadowmapviewer.position
oculushandpointer.attached is not nullable
XRHandMeshModel.path is nullable in constructor
Better type for NodeBuilder.vars
Add Color has color type for Color4.set
Renderer.compute result is not null but undefined
Renderer.compile return a function not a promise
ViewHelper.handleClick has event of type MouseEvent
Loader.requestHeader is Object<string, string> (set everywhere)
ImageBitmaploader.requestHeader is Object<string, string> (set everywhere)
NodeLoader.parseNodes json is Object<string, any>
ReflectorNode.getDepthNode and getDepthNode return ReflectorNode
ReflectorNode constructor default values for params does not exist
ReflectorBaseNode.textureNode is ReflectorNode (has getDepthNode only exists in ReflectorNode)
correct all generic errors ": Generic type "
All loaders method load onLoad params return type

# Dev
RG11B10UFloat
Use MaterialLoader.js and Material.js to fix tab of material attributes


# Investigate
RTTNode problem for width undefined, passing null, ... ??
See if https://jsdoc.app/tags-this can be used
Remove ...arguments calls
AnimationClip.toJSON broken ?
Delete as much eslint-disable-next-line as possible
Add more link to MDN doc inside the code (use dom in tsconfig)