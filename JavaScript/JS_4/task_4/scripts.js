
document.getElementById('button').addEventListener('click', function createHeaders(){
    
    const pass = document.getElementById('input').value;
    const massage = document.getElementById('massage')

    if (pass == 'Step' ||pass == 'Web' ||pass == 'JavaScript'){
        massage.textContent = true;
    }else{
        massage.textContent = false;

    }
    
    
    
})