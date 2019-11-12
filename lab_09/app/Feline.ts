import Mammal from "./Mammal";

class Feline extends Mammal {
    static nFelines: number = 0; // static property

    family: string;


    constructor(habitat: string, sound: string, family: string) {
        super(habitat, sound);
        Feline.nFelines++;
        this.family = family;
    }

    show() {
        return super.show() + "\nFamily: " + this.family;
    }
}

export default Feline;