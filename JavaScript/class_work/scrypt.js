document.getElementById('button').addEventListener('click', function() {
    
    const name =
    document.getElementById('name').value;
    
    const massage = 
    document.getElementById('massage');

    if (name) {
        massage.textContent = `Привет, ${name}!`;
    }else{
        massage.textContent = 'Пожалуйста, введите свое имя!'
    }
});