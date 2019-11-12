import Animal from "./Animal";

class Reptile extends Animal {
    static nReptiles: number = 0; // static property

    sound: string;

    constructor(habitat: string, sound: string) {
        super(habitat);
        Reptile.nReptiles++;
        this.sound = sound;
    }
}

export default Reptile;