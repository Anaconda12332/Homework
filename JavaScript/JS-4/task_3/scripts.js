
document.getElementById('button').addEventListener('click', function createHeaders(){
    
    const n = document.getElementById('input').value;
    
    // const header = document.createElement('h2');
    // const p =document.getElementById('massage');
    
        for (let i = 1; i <= n; i++){
    
            document.write('<h2> Header '+i+'</h2>')
            // header.innerHTML = `Header${i}`;
            // p.appendChild(header);
        }

    
})