const num="256";
let suma= 0;
let mult=1;
for (let i = 0; i < num.length; i++) {
    suma= parseInt(num[i]) + suma;
    mult= parseInt(num[i]) * mult;
}
console.log(suma);
console.log(mult);
