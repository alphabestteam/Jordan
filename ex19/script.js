function sequenceA() {
    setTimeout(_ => console.log('Sponge'), 0);
    console.log("Bob");
}

function sequenceB(){
    setTimeout(_ => console.log(`🍅 Timeout at B`), 0);
    Promise.resolve().then(_ => console.log('🍍 Promise at B'));
}

function sequenceC(){
    setTimeout(_ => console.log(`🍅 Timeout at C`), 0);
    Promise.resolve().then(_ => setTimeout(console.log('🍍 Promise at C'), 1000));
}

function sequenceD(){
    console.log('Sponge');
    setTimeout(_ => console.log('Square'), 0);
    Promise.resolve().then(_ => console.log('Pants'));
    console.log('Bob');
}

function questionA(){
    sequenceA();
}

function questionB(){
    sequenceB();
}

function questionC(){
    sequenceC();
}

function questionD(){
    sequenceD();
}

function questionE(){
    sequenceB();
    sequenceC();
}

// questionA(): bob will be first. sequenceA` logs "Bob" immediately because it's a regular synchronous function. The `setTimeout` with a delay of 0 still queues the "Sponge" log in the event loop, but it is logged after "Bob."
// questionB(): Promise.resolve().then() logs Promise at B in the microtask queue, and it is executed before The `setTimeout` method 
// questionC():Promise.resolve().then() logs Promise at C in the microtask queue, and it is executed before The `setTimeout` method 
// questionD():"Sponge" is logged immediately because it's a regular synchronous function. "Bob" comes after because it's also a regular synchronous function, than Promise.resolve().then(...) that prints pants and square will be in the end 
// questionE():sequenceB and sequenceC are executed in order. For both `sequenceB` and `sequenceC`, the " Promise" logs are executed in the microtask queue before the " Timeout" logs in the task queue




