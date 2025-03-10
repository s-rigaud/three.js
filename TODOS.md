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

# Dev


# Investigate
Use MaterialLoader.js and Material.js to fix tab of material attributes
All loaders method load onLoad params return type
correct all generic errors ": Generic type "
RTTNode problem for width undefined, passing null, ... ??
See if https://jsdoc.app/tags-this can be used
Remove ...arguments calls
Test reflectorNode .getDepthNode (type problem)
Investigate more on TS2322
Reread line like "Did you mean" (one mistake found like that)
AnimationClip.toJSON broken ?
Delete as much eslint-disable-next-line as possible
Add more link to MDN doc inside the code (use dom in tsconfig)