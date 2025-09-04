# Types
examples/jsm/tsl/display/Lut3DNode.js:63
examples/jsm/tsl/display/PixelationPassNode.js:305
every setup() { method builder argument

# Dev

# Investigate
Find a way to generate editor\js\libs\tern-threejs\threejs.js
Extract examples Js code and find TS errors inside
Find way to replcae Jsdoc types by their definitions

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
