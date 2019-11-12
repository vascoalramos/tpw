import Feline from "./Feline";

class Cat extends Feline {
    static nCats: number = 0; // static property

     name: string;


    constructor(habitat: string, sound: string, family: string, name: string) {
        super(habitat, sound, family);
        Cat.nCats++;
        this.name = name;
    }

    show() {
        return super.show() + "\nName: " + this.name;
    }
}

export default Cat;