# Types
Sceneoptimizer.disposeMeshes mesh is not array but a set
fix type of Shadowmapviewer.position
oculushandpointer.attached is not nullable
XRHandMeshModel.path is nullable in constructor
Better type for NodeBuilder.vars
Add Color has color type for Color4.set
Renderer.compute result is not null but undefined
Renderer.compile return a function not a promise

# Dev
Move this.trackTimestamp to parent Backend class
Sceneoptimizer ref to this.logDebugInfo
Add buildFunctionCode to NodeBuilder class (func overiten by subclasses)
AnalyticalLightNode call to .setupShadowNode does not take any parameter

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