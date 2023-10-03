document.addEventListener("DOMContentLoaded", function () {

    const menuContainer = document.getElementById("menu");
    const listContainer = document.getElementById("list");
    const contentContainer = document.getElementById("content");

    menuContainer.addEventListener("click", (event) => {
        event.preventDefault();
        const clickedLink = event.target;
        if (clickedLink.tagName === "A") {
            const menuLinks = menuContainer.querySelectorAll("a");
            menuLinks.forEach((link) => {
                link.classList.remove("clicked");
            });
            clickedLink.classList.add("clicked");
            listContainer.innerHTML =""; 
            contentContainer.innerHTML ="";
            const href = clickedLink.getAttribute("href");
            fetch(href)
                .then(response => response.text())
                .then(data => {
                    listContainer.innerHTML = data;
                    document.getElementById("list").setAttribute("data-menu", href);
            })
        }
    });

    listContainer.addEventListener("click", (event) => {
        event.preventDefault();
        const clickedLink = event.target;
        if (clickedLink.tagName === "A") {
            contentContainer.innerHTML ="";
            const menuLinks = listContainer.querySelectorAll("a");
            menuLinks.forEach((link) => {
                link.classList.remove("highlighttext");
            });
            clickedLink.classList.add("highlighttext");
            const href = clickedLink.getAttribute("href");
            fetch(href)
            .then(response => response.text())
            .then(data => {
                if(href.match("list_contract")){
                    listContainer.innerHTML = data; 
                }else{

                    if(href.match("month/detail/")){
                        var nouvelOnglet = window.open(href, '_blank');
                    }else{
                        contentContainer.innerHTML = data; 
                        const form = contentContainer.querySelector("form");
                        form.setAttribute("data-list", href);
                    }
                }
            })
        }
    });

   contentContainer.addEventListener("submit", (event) => {
        event.preventDefault();
        const formData = new FormData(event.target);
        const href = event.target.getAttribute("data-list");
        fetch(href, {
            method: "POST",
            body: formData
        })
        .then(response => response.text())
        .then(data => {
           if(listContainer.getAttribute("data-menu")==="/month/list_contract/"){
                listContainer.innerHTML = data;
            }
            contentContainer.innerHTML = data;
            const listURL =listContainer.getAttribute("data-menu");
            updateListContainer(listURL);
        })
    });

    function updateListContainer(listURL) {
        if(listURL ==="/month/list_contract/" || listURL ==="/month/days_update/"){
            listURL ="/month/list/";
        } 
        fetch(listURL, {
            method: "GET"
        })
        .then(response => response.text())
        .then(data => {
            listContainer.innerHTML = data;
        });
    }
});
