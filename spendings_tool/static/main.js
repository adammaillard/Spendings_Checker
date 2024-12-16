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

function sortCategory() {
    let transactions = document.getElementsByClassName("transaction");
    let all_categories = document.getElementsByClassName("container");
    let categories = [];

    for (i = 0; i < all_categories.length; i++) {
        if (all_categories[i].getElementsByClassName("check")[0].checked) {
            categories.push(all_categories[i].getElementsByClassName("description_name")[0].id.toLowerCase());
        }
    }

    for (i = 0; i < transactions.length; i++) {
        if (categories.includes(transactions[i].getElementsByClassName("transaction_category")[0].innerHTML.toLowerCase()) || categories.length == 0) {
            transactions[i].style.display = "flex";
        } else {
            transactions[i].style.display = "none";
        }
    }
}

function ValidDate(date) {
    pattern = /\d{2}\/\d{2}\/\d{4}/;
    result = date.match(pattern);
    return result != null && CreateDate(date) != "Invalid Date";
}

function CreateDate(date) {
    split_date = date.split("/");
    return new Date(split_date[1]+"/"+split_date[0]+"/"+split_date[2])
}

function DateSearch(){
    let before_date = document.getElementById("before_date").value;
    if (ValidDate(before_date)){
        before_date = CreateDate(before_date);
    } else {
        before_date = new Date("2200-01-01");
    }
    let after_date = document.getElementById("after_date").value;
    if (ValidDate(after_date)){
        after_date = CreateDate(after_date);
    } else {
        after_date = new Date("0000-01-01");
    }
    console.log(before_date)
    console.log(after_date)
    let transactions = document.getElementsByClassName("transaction");
    for (i = 0; i < transactions.length; i++) {
        const date = CreateDate(transactions[i].getElementsByClassName("transaction_date")[0].innerHTML);
        if (date <= before_date && date >= after_date) {
            transactions[i].style.display = "flex";
        } else {
            transactions[i].style.display = "none";
        }
    }
}