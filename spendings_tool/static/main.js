function Search(){
    let search = document.getElementById("search").value;
    let transactions = document.getElementsByClassName("transaction");
    for (i = 0; i < transactions.length; i++) {
        if (transactions[i].getElementsByClassName("transaction_name")[0].innerHTML.toLowerCase().includes(search.toLowerCase())) {
            transactions[i].style.display = "flex";
        } else {
            transactions[i].style.display = "none";
        }
    }
}

function showSort(){
    let sort_options = document.getElementById("sort_options")
    if (sort_options.classList.contains("show")){
        sort_options.classList.remove("show");
    } else {
        sort_options.classList.add("show");
    }
}