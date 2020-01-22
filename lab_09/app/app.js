"use strict";
exports.__esModule = true;
var Animal_1 = require("./Animal");
var Mammal_1 = require("./Mammal");
var Reptile_1 = require("./Reptile");
var Cat_1 = require("./Cat");
var animal1 = new Animal_1["default"]("Earth");
var rep1 = new Reptile_1["default"]("Earth", "sound1");
var mam1 = new Mammal_1["default"]("Earth", "roaaahhh");
console.log(mam1.show());
console.log();
console.log(mam1.talk());
console.log("\n\n");
var cat1 = new Cat_1["default"]("Earth", "miau", "family", "bixano");
console.log(cat1.show());
console.log();
console.log(cat1.talk());