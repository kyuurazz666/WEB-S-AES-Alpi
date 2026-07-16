// ======================================
// Copy Text to Clipboard
// ======================================

function copyText(id){

    let value = document.getElementById(id).innerText;

    navigator.clipboard.writeText(value);

    showToast("Berhasil disalin : " + value);

}

// ======================================
// Toast Notification
// ======================================

function showToast(message){

    let toast = document.getElementById("toast");

    toast.innerHTML = message;

    toast.classList.add("show");

    setTimeout(function(){

        toast.classList.remove("show");

    },2000);

}