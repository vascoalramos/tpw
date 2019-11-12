class Animal {
    static nAnimals: number = 0; // static property

    habitat: string;

    constructor(habitat: string) {
        this.habitat = habitat;
        Animal.nAnimals++;
    }
}

export default Animal;