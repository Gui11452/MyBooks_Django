(function main(){

    const seta = document.querySelector('body>i');
    const nav1 = document.querySelector('#cabecalho-interno nav a');
    const botao = document.querySelector('#botao-interno');
    const botaoSpan = document.querySelectorAll('#botao-interno span');
    const [a, b, c] = botaoSpan;
    const cabecalhoOculto = document.querySelector(' header.cabecalho');

    document.addEventListener('click', e => {

        const element = e.target;
        let top;

        if(element == seta){
            scroll({
                top: 0,
                behavior: 'smooth'
            })
        }
        else if(element == nav1){
            e.preventDefault();
            
            const atributo = nav1.getAttribute('href');
            to = document.querySelector(atributo).offsetTop;

            scroll({
                top: to - 110,
                behavior: 'smooth'
            })
        }

        else if(element == botao || element == a || element == b || element == c){

            cabecalhoOculto.classList.toggle('cabecalho-oculto-mostrar');

        }

    })

})();