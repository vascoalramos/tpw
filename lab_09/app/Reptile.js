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
var Reptile = /** @class */ (function (_super) {
    __extends(Reptile, _super);
    function Reptile(habitat, sound) {
        var _this = _super.call(this, habitat) || this;
        Reptile.nReptiles++;
        _this.sound = sound;
        return _this;
    }
    Reptile.nReptiles = 0; // static property
    return Reptile;
}(Animal_1["default"]));
exports["default"] = Reptile;
