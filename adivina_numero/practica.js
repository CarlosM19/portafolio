"USE STRICT"

const numero_guardado = 16;
let validar = document.getElementById('validar');
let situacion = document.getElementById('situacion');


validar.addEventListener('mouseover', ()=>{
    validar.style.backgroundColor = '#34017E';
})
validar.addEventListener('mouseout', ()=>{
    validar.style.backgroundColor = 'rgb(111, 4, 4)';
})

validar.addEventListener('click', (numero)=>{
    numero = parseInt(document.getElementById('numero').value);
    if(numero === numero_guardado){
        situacion.innerHTML = '¡¡¡ADIVINASTE!!!';
        situacion.style.fontSize = '65px'
        situacion.style.color = '#34017E'
    }else if(numero >= numero_guardado){
        alert('El número ingresado es Mayor');
    }else if(numero <= numero_guardado){
        alert('El número ingresado es Menor');
    }else if(isNaN(numero)){
        alert('El Valor Ingresado es incorrecto');
    }
})



