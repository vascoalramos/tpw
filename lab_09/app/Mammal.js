"use strict";
var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
exports.__esModule = true;
var Animal_1 = require("./Animal");
var Mammal = /** @class */ (function (_super) {
    __extends(Mammal, _super);
    function Mammal(habitat, sound) {
        var _this = _super.call(this, habitat) || this;
        Mammal.nMammals++;
        _this.sound = sound;
        return _this;
    }
    Mammal.prototype.talk = function () {
        return this.sound;
    };
    Mammal.prototype.show = function () {
        return "Number of Animals: " + Animal_1["default"].nAnimals + "\nHabitat: " + this.habitat;
    };
    Mammal.nMammals = 0; // static property
    return Mammal;
}(Animal_1["default"]));
exports["default"] = Mammal;
