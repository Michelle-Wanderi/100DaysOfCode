// Variables

let btn = document.querySelector('#new-quote');
let quote = document.querySelector('.quote');
let person = document.querySelector('.person');


const quotes  = [{
    quote : `"The best way to find yourself is to lose yourself in the service of others"`,
    person : `Mahatma Gandhi`
},{
    quote : `"Take care of your mind and body`,
    person : `Michelle Wangari`
}, {
    quote : `"At his best, main is noblest of all animals`,
    person : `"Arisostle"`

},{
    quote : `"Take care of your mind and body`,
    person : `Michelle Wangari`
}

];

btn.addEventListener('click', function(){

    let random = Math.floor(Math.random() * quotes.length );

    quote.innerText = quotes[random].quote;
    person.innerText = quotes[random].person;
})