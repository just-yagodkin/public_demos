const select = document.querySelector('select');
const allLang = ['en', 'ru'];

select.addEventListener('change', changeURLLanguage);


function changeURLLanguage(){
    let lang = select.value;
    location.href = window.location.pathname + '#' + lang;
    location.reload();
}

function changeLanguage(){
    let hash = window.location.hash;
    hash = hash.substr(1);
    console.log(window.location.pathname);

    if (!allLang.includes(hash)){
        location.href = window.location.pathname + '#en';
        location.reload();
    }
    select.value = hash;
    if (window.location.pathname.indexOf("Instruction", 0) != -1){                      // Если мы на странице Instruction
        document.getElementById("lng-IReadTheSlides").innerText = langArr['IReadTheSlides'][hash];
    }

    for (let key in langArr)
    {
        let elem =document.querySelector('.lng-' + key);
        if(elem){
        document.querySelector('.lng-'+key).innerHTML = langArr[key][hash];
        }

    }
}

changeLanguage();