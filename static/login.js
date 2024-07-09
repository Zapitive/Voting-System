

function fnc(x){
    lsb = document.getElementById('login-supp-btn')
    ssb = document.getElementById('signup-supp-btn')
    fd = document.getElementById('form-div')
    fl = document.getElementById('forml-div')
        if (lsb.style.display === "none") {
            fl.style.display = "none";
            fd.style.display = "block"
            ssb.style.display = "none";
            lsb.style.display = "inline-block";
        } 
        else {
            lsb.style.display = "none";
            fl.style.display = "block"
            ssb.style.display = "inline-block";
            fd.style.display = "none";
        }
}