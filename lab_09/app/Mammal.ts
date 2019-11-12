import Animal from "./Animal";

class Mammal extends Animal {
    static nMammals: number = 0; // static property

    sound: string;

    constructor(habitat: string, sound: string) {
        super(habitat);
        Mammal.nMammals++;
        this.sound = sound;
    }

    talk() {
        return this.sound;
    }

    show() {
        return "Number of Animals: " + Animal.nAnimals + "\nHabitat: " + this.habitat;
    }
}

export default Mammal;