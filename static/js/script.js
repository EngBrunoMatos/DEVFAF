function limpar(){
    window.location = window.location.pathname;
}
function cancelar() {
    window.history.back()
}
function bt_tab(z){
    document.getElementById("tab1").style.display="none";
    document.getElementById("tab2").style.display="none";
    document.getElementById("tab3").style.display="none";
    document.getElementById("tab4").style.display="none";
    document.getElementById("tab5").style.display="none";
    document.getElementById("tab6").style.display="none";
    document.getElementById("bt_tab1").classList.remove('active');
    document.getElementById("bt_tab2").classList.remove('active');
    document.getElementById("bt_tab3").classList.remove('active');
    document.getElementById("bt_tab4").classList.remove('active');
    document.getElementById("bt_tab5").classList.remove('active');
    document.getElementById("bt_tab6").classList.remove('active');
    switch (z){
        case 1:document.getElementById("bt_tab1").classList.add('active');document.getElementById("tab1").style.display="block";break;
        case 2:document.getElementById("bt_tab2").classList.add('active');document.getElementById("tab2").style.display="block";break;
        case 3:document.getElementById("bt_tab3").classList.add('active');document.getElementById("tab3").style.display="block";break;
        case 4:document.getElementById("bt_tab4").classList.add('active');document.getElementById("tab4").style.display="block";break;
        case 5:document.getElementById("bt_tab5").classList.add('active');document.getElementById("tab5").style.display="block";break;
        case 6:document.getElementById("bt_tab6").classList.add('active');document.getElementById("tab6").style.display="block";break;
    }
}
function get_Checkbox(){
    var check = document.getElementsByName('lista_responsavel');
    var check_id = document.getElementsByName('lista_responsavel_id');
    var lista_resp=[];
    var lista_resp_id=[];
    for (var i = 0; i < check.length; i++){
        if (check[i].checked){
            lista_resp.push(check[i].value);
            lista_resp_id.push(check_id[i].value);
        }
    }
    document.getElementById('Lista_Responsavel').innerHTML=lista_resp.join('<br>');
    document.getElementById('Button_Lista_Responsavel').value=lista_resp_id;
}

//Ir pra cima
var mybutton = document.getElementById("goup");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}

function goBack() {
  window.history.back()
}