import Mammal from "./Mammal";
import Animal from "./Animal";

class Canine extends Mammal {
    static nCanines: number = 0; // static property

    family: string;


    constructor(habitat: string, sound: string, family: string) {
        super(habitat, sound);
        Canine.nCanines++;
        this.family = family;
    }

    show() {
        return super.show() + "\nFamily: " + this.family;
    }
}