document.getElementById('button').addEventListener('click', function(){

    const text = 
    document.getElementById('xz').value;

    const message =
    document.getElementById('message');



    if (Number(text) >= 0 && Number(text) <= 100){
        message.textContent = `Число ${text} принадлежит диапазону 0 - 100`;
    }else if (Number(text) >= 101 && Number(text) <= 200){
        message.textContent = `Число ${text} принадлежит диапазону 101 - 200`;
    }else if (Number(text) >= 201 && Number(text) <= 300){
        message.textContent = `Число ${text} принадлежит диапазону 201 - 300`;
    
    }else{
        message.textContent = `Число ${text} не принадлежит никакому диапазону`;
    }
})