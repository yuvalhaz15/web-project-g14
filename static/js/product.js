let cuont;


window.onload = function(){

    const activePage = window.location.pathname;
    console.log(activePage);
    
     document.querySelectorAll('a').forEach(link => {    
      if(link.href.includes(`${activePage}`)){
        link.classList.add('active');
      }
    });
         
}
    
    
function isHeInsed(producrId) {

    cuont = 0;
    const navLinks = document.querySelectorAll('span');
    navLinks.forEach(bla);

    function bla(A) {
      if(A.textContent.includes(producrId)){
        cuont +=1;
    }
      }


    if (cuont > 0) {
        return (false)
    } else {
        return (true)
     }

}

function CLEAR() {

const list = document.getElementById("HR");
while (list.hasChildNodes()) {
 list.removeChild(list.firstChild);

}}



function newToy() {

    CLEAR()

    for (var i = 0; i < json.length; i++) {
        if (json[i].catagori === "-+4" && isHeInsed(json[i].name)) {         
            prod = new Product(json[i].name, "blabsa", json[i].pic)
            prod.addTOHtml()
        }
    }
}

function newToy1() {
    CLEAR()

    for (var i = 0; i < json.length; i++) {
        if (json[i].catagori === "-+8" && isHeInsed(json[i].name)) {
            prod = new Product(json[i].name, "blabla", json[i].pic)
            prod.addTOHtml()
        }
    }
}

function newToy2() {

    CLEAR()
    for (var i = 0; i < json.length; i++) {
        if (json[i].catagori === "-+9" && isHeInsed(json[i].name)) {
            var prod = new Product(json[i].name, "blabla", json[i].pic)
            prod.addTOHtml()
        }

    }
}
function display_image(src,width,height,alt){
    var img=document.createElement("img");
    img.src=src;
    img.width=width;
    img.height=height;
    img.alt=alt;

    document.appendChild(img);


}

function newToy3() {
    CLEAR()
   
    for (var i = 0; i < json.length; i++){
        if (isHeInsed(json[i].name)) {
        var prod = new Product(json[i].name, "blabla", json[i].pic)
        prod.addTOHtml()
    }
}
}







function checkName(name){
    var name=document.getElementById(name).value;
    if (name.length<=1){
      alert("שם חייב להכיל לפחות 2 אותיות");
      document.getElementById(name).value="";
    }
  }
  
 
  
function checkEmail (id){
    var email=document.getElementById(id).value;
    var mailformat = /^\w+([\.-]?\w+)@\w+([\.-]?\w+)(\.\w{2,3})+$/;
    if (!email.match(mailformat)){
          alert("כתובת דואר אלקטרוני שהוזנה לא תקינה");
          document.getElementById(id).value="";
    }
  }

  function checkPassword(id){
    var password=document.getElementById(id).value;
    if (password.length<6){
      alert("סיסמא צריכה לכלול לפחות 6 תווים");
      document.getElementById(id).value="";
    }
  }

  
  function submitFormContact() {
    if (document.getElementById('firstname').value.length==0 ||
        document.getElementById('lastname').value.length==0 ||
        document.getElementById('phonenumer').value.length==0 ||
        document.getElementById('emailaddress').value.length==0){
         alert("לא ניתן לשלוח את הטופס מכיוון שלא כל השדות מולאו באופן תקין");
          }
    else {
            alert("הטופס נשלח בהצלחה. הינך מועבר/ת לעמוד הבית");
            window.location="mainPage.html";
     }
}
