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
var Mammal_1 = require("./Mammal");
var Feline = /** @class */ (function (_super) {
    __extends(Feline, _super);
    function Feline(habitat, sound, family) {
        var _this = _super.call(this, habitat, sound) || this;
        Feline.nFelines++;
        _this.family = family;
        return _this;
    }
    Feline.prototype.show = function () {
        return _super.prototype.show.call(this) + "\nFamily: " + this.family;
    };
    Feline.nFelines = 0; // static property
    return Feline;
}(Mammal_1["default"]));
exports["default"] = Feline;
