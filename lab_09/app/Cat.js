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
var Feline_1 = require("./Feline");
var Cat = /** @class */ (function (_super) {
    __extends(Cat, _super);
    function Cat(habitat, sound, family, name) {
        var _this = _super.call(this, habitat, sound, family) || this;
        Cat.nCats++;
        _this.name = name;
        return _this;
    }
    Cat.prototype.show = function () {
        return _super.prototype.show.call(this) + "\nName: " + this.name;
    };
    Cat.nCats = 0; // static property
    return Cat;
}(Feline_1["default"]));
exports["default"] = Cat;
