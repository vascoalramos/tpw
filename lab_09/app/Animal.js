"use strict";
exports.__esModule = true;
var Animal = /** @class */ (function () {
    function Animal(habitat) {
        this.habitat = habitat;
        Animal.nAnimals++;
    }
    Animal.nAnimals = 0; // static property
    return Animal;
}());
exports["default"] = Animal;
