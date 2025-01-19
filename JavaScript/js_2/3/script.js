document.getElementById('button').addEventListener('click', function(){

    const text = 
    document.getElementById('xz').value;
    const message =
    document.getElementById('message');



    if (Number(text) >=0 && Number(text) <= 100){
        message.textContent = `Число ${text} принадлежит диапазону 0-100`;
    }else{
        message.textContent = `Число ${text} не принадлежит диапазону 0-100`;
    }
})