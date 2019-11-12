import Mammal from "./Mammal";

class Bovine extends Mammal {
    static nBovines: number = 0; // static property

    family: string;


    constructor(habitat: string, sound: string, family: string) {
        super(habitat, sound);
        Bovine.nBovines++;
        this.family = family;
    }

    show() {
        return super.show() + "\nFamily: " + this.family;
    }
}