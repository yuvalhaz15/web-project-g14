function Product(_name,_disci,_pic)
{
this.name = _name;
this.disci = _disci;
this.pic = _pic;
// this.makt = _makt;

}


Product.prototype.addTOHtml = function()
{
   
   this.gerger = document.createElement("div");
   this.gerger.className = "pro";

   HR.appendChild(this.gerger)


   this.ger = document.createElement("div");
   this.ger.className = "des";

   
   this.newimg = document.createElement("img")
   this.newimg.src += `/static/product/` + this.pic;
   
   this.gerger.appendChild(this.newimg)  
  
  
   this.ger.innerHTML += "<span>" + this.name  + "</span>" ;
   this.ger.innerHTML += " <h5> "  + this.disci  +   "</h5>" ;
   // this.ger.innerHTML += " <h5> "  + this.disci  +   "</h5>" ;
   // this.ger.innerHTML += " <h5> "  + this.makt  +   "</h5>" ;
   this.ger.innerHTML += `<a href="#"> <span class="material-symbols-outlined cart">add_box</span></a>`;
   this.gerger.appendChild(this.ger)
}

