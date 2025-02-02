let list = [];

document.getElementById('button').addEventListener('click', function stringFrom(){
    let text =  document.getElementById('input').value;

    list.push(text);
    text =  document.getElementById('input').value= "";
})



document.getElementById('button2').addEventListener('click', function stringFrom(){


    const massage = document.getElementById('massage');
    
    massage.textContent = `Минимальное число ${Math.min(...list)}`

})



