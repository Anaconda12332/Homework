document.getElementById('button').addEventListener('click', function(){

    const text = 
    document.getElementById('xz').value;
    const message =
    document.getElementById('message');


    // result = confirm('Продолжить?');

    if (text == 'Step' || text == 'Web' ||text == 'JavaScript'){
        message.textContent = 'Подтверждено'
    }else{
        message.textContent = 'Отменено'
    }
})