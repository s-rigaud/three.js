# Types
ReflectorNode.getDepthNode and getDepthNode return ReflectorNode
ReflectorNode constructor default values for params does not exist
ReflectorBaseNode.textureNode is ReflectorNode (has getDepthNode only exists in ReflectorNode)
correct all generic errors ": Generic type " only for lists
All loaders method load onLoad params return type
RTTNode problem for width being null instead of undefined (fix also for rttNode TSL function)

# Dev
LWOLoadr :354 additonal argument
LWOLoadr :538 additonal argument
LWOLoadr :825 additonal argument
MD2Loader.js :144 should be BufferGeo as input
VolumeSlice add default value in constructor for ctx and ctxBuffer (doesn't seem to change)
Volume.header not defined (set in NRRDLoader)
WebGPUTimestampquery dispose can return undefined
FBXLoader :174

# Investigate
Find a way to generate editor\js\libs\tern-threejs\threejs.js
