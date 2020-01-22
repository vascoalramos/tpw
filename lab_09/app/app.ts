import Animal from "./Animal";
import Mammal from "./Mammal";
import Reptile from "./Reptile";
import Cat from "./Cat";

let animal1 = new Animal("Earth");

let rep1 = new Reptile("Earth", "sound1");

let mam1 = new Mammal("Earth", "roaaahhh");
console.log(mam1.show());
console.log();
console.log(mam1.talk());
console.log("\n\n");

let cat1 = new Cat("Earth", "miau", "family", "bixano");
console.log(cat1.show());
console.log();
console.log(cat1.talk());