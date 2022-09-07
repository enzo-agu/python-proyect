// // clase constructora

// class Remeraslicra {
//     constructor (talle,modelo,marca){
    
//         this.talle = talle,
//         this.modelo = modelo,
//         this.marca = marca

//     }
//          entregaRemeras() {

//         return this.talle +" "+ this.modelo;

//       }
    
// }

// // paso 3 parámetros (prompts) a la clase

// const licras = new Remeraslicra(prompt("ingrese talle"),prompt("ingrese tipo"),prompt("ingrese marca"));
// console.log(licras.entregaRemeras())


// // creo el array
// let arrayLycras= [];
// arrayLycras.push(licras.talle) // voy a pushear cada cosa que ingresa por prompt
// console.log(arrayLycras)


//Creo un objeto



const remerasGrappling=[{
    id:1,
    marca:"Venum",
    color:"negro",
},
{
    id:2,
    marca:"Fight-Effect",
    color:"azul",
},
{
    id:3,
    marca:"Rashguard",
    color:"gris"
},
{
    id:4,
    marca:"fullsport",
    color:"verde-claro"
},
{
    id:5,
    marca:"No-fear",
    color:"verde-oscuro"
},
{
    id:6,
    marca:"RVCA",
    color:"marron"
},
{
    id:7,
    marca:"Koral",
    color:"blanca"
}
];

//for of del array de objetos
for (const remera of remerasGrappling) {
    console.log(remera)
}


const array2=["Camila","Critian","Ignacio","Jael","Jonathan"]
console.log(array2.length)
array2.pop()
console.log(array2)

const concatenacion= array2.concat(remerasGrappling)

console.log(array2.includes("Juan"))



// const objeto1={
//     id:1,
//     nombre:"enzo",

// }



// //for in del array de objetos

// for (const r in objeto1) {
//     console.log(objeto1[r])
// }

// //prompy para implementar método find

// let pregunta=parseInt(prompt("ingrese numero de remera del 1 al 7"))
// let verId= remerasGrappling.find((r)=>r.id==pregunta)
// console.log(verId)


// //método sort para ordenar alfabéticamente

// const MarcaAutos = ["ford" ,"toyota", "volksvagen ", " chevrolet "] ;
// MarcaAutos.sort();
// console.log(MarcaAutos) ;




// //  // método sort  para ordenar de mayor a menor


// const combo = [{ numero: 1, tipo: "arroz", precio: 70 },
//     { numero: 2, tipo: "yerba", precio: 250 },
//     { numero: 3, tipo: "azucar", precio: 60 },
//     { numero: 4, tipo: "choclo", precio: 55 },
//     { numero: 5, tipo: "fideos", precio: 80 }
// ];

// const precioOrden = combo.sort((prod1, prod2) => { return prod1.precio - prod2.precio })

// console.log(precioOrden);



// const nombres = ['Rita', 'Pedro', 'Miguel', 'Ana', 'Vanesa']

// // recibo el elemento a borrar por parámetro
// const eliminar = (nombre) => {
//     // busco su índice en el array
//     let index = nombres.indexOf(nombre)

//      // si existe, o sea es distinto a -1, lo borro con splice
//     if (index != -1 ) {
//         nombres.splice(index, 1)
//         console.log(nombres)
//     } 
// }

// eliminar('Pedro')




// //  map
// let numbers = [1, 5, 10, 15];
// let doubles = numbers.map((d) => d * 2);
// console.log(doubles)

// metodo unshift de array=> agrega al principio del array
// metodo shift de array=> quita el primer elem del array
// metodo pop => quita el ultimo elem del array
// splice]=> recibe dos param (inidice, cantidad de elem a elimiar desde el indice)
// slice=> crea una copia de un array en otro array con los params que le pase
// es decir, se cuenta desde la posición que le indico hasta cierta posicion
// pero la última posición no se cuenta
// Indexof=> me devuelve la posición de un elem que le pase como param
// includes=> me inidica con un booleano si cierto elem existe o no
// reverse=> da vuelta el array

//for of para recorrer array de objetos
// for in