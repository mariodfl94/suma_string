const num="256";
let suma= 0;
let mult=1;
let resta = 0;
let sumadeimpares = 0;
let sumadepares = 0;
let divisor=1;
let d = 1;
for (let i = 0; i < num.length; i++) {
    suma= parseInt(num[i]) + suma;
    mult= parseInt(num[i]) * mult;
    if (parseInt(num[i]) % 2 != 0) {
        sumadeimpares = sumadeimpares + parseInt(num[i]);
    } else {
        sumadepares = sumadepares + parseInt(num[i]);
    }
    resta=  sumadepares-sumadeimpares
    if (parseInt(num.length-d==0)) {
        divisor = parseInt(num[i]);
        d = d-1;
    }else{
        divisor = parseInt(num[i])  
        div= suma / divisor;  
    }
}
console.log(resta);
console.log(suma);
console.log(mult);
console.log(div);
